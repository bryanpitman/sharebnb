"""User model tests."""

from app import app
import os
from unittest import TestCase

from models import db, User

os.environ['DATABASE_URL'] = "postgresql:///sharebnb_test"


class UserModelTestCase(TestCase):
    def setUp(self):
        User.query.delete()

        u1 = User.signup("u1", "password", "u1@email.com", "hello")
        u2 = User.signup("u2", "password", "u2@email.com", "hello")

        db.session.commit()
        self.u1_username = u1.username
        self.u2_username = u2.username

        self.client = app.test_client()

    def tearDown(self):
        db.session.rollback()

    def test_user_model(self):
        u1 = User.query.get(self.u1_username)

        self.assertEqual(len(u1.created_listings), 0)

    # #################### Signup Tests

    def test_valid_signup(self):
        u1 = User.query.get(self.u1_username)

        self.assertEqual(u1.username, "u1")
        self.assertEqual(u1.email, "u1@email.com")
        self.assertNotEqual(u1.password, "password")
        # Bcrypt strings should start with $2b$
        self.assertTrue(u1.password.startswith("$2b$"))

    # # #################### Authentication Tests

    def test_valid_authentication(self):
        u1 = User.query.get(self.u1_username)

        u = User.authenticate("u1", "password")
        self.assertEqual(u, u1)

    def test_invalid_username(self):
        self.assertFalse(User.authenticate("bad-username", "password"))

    def test_wrong_password(self):
        self.assertFalse(User.authenticate("u1", "bad-password"))
