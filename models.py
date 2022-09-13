from datetime import datetime
from email.quoprimime import body_check
from pyexpat.errors import messages
from termios import TIOCPKT_FLUSHREAD

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


DEFAULT_IMAGE_URL = "/url.com"

# User


class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    username = db.Column(
        db.String(length=50),
        primary_key=True,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    location = db.Column(
        db.Text,
        nullable=False
    )

    is_admin = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    messages = db.relationship('Message', backref="user")

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"

    @classmethod
    def signup(cls, username, email, password, image_url=DEFAULT_IMAGE_URL):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            image_url=image_url,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If this can't find matching user (or if password is wrong), returns
        False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False


# Listing
class Listing(db.Model):
    """Listing in the system."""

    __tablename__ = 'listings'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    title = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_LOCATION_IMAGE,
    )

    description = db.Column(
        db.Text,
        nullable=False,
        default="",
    )

    photo = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_LOCATION_IMAGE,
    )

    price = db.Column(
        db.Float,
        nullable=False,
    )

    created_by = db.Column(
        db.String,
        db.ForeignKey(  # TODO:),
        nullable=False
    )

    @ classmethod
    def find_all()

    @ classmethod
    def create()
