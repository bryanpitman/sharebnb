# """Listing Model Tests"""


# from app import app
# import os
# from unittest import TestCase
# from sqlalchemy import exc

# from models import db, User, Listing

# os.environ['DATABASE_URL'] = "postgresql:///sharebnb_test"


# db.create_all()


# class ListingModelTestCase(TestCase):
#     def setUp(self):
#         db.drop_all()
#         db.create_all()

#         u1 = User.signup("u1", "password", "u1@email.com", "hello")
#         l1 = Listing("title", "description", "location", "photo.com", 200, u1)

#         db.session.commit()

#         self.u1_username = u1.username
#         self.l1_id = l1.id

#         self.client = app.test_client()

#     def tearDown(self):
#         db.session.rollback()

#     def test_listing_model(self):
#         u = User.query.get(self.u1_username)
#         l1 = Listing.query.get(self.l1_id)

#         # db.session.add_all()

#         # db.session.commit()

#         # User should have 1 listing
#         self.assertEqual(len(u.created_listings), 1)
#         # Listing creator should be User
#         self.assertEqual(l1.created_by, u)
