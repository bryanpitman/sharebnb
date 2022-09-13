from collections import UserString
from datetime import datetime


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

    created_listings = db.relationship('Listing', foreign_keys='Listing.created_by', backref='created_by')

    def __repr__(self):
        return f"<User # {self.username}, {self.email}>"

    @classmethod
    def signup(cls, username, email, password):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd
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
        default=DEFAULT_IMAGE_URL,
    )

    description = db.Column(
        db.Text,
        nullable=False,
        default="",
    )

    location = db.Column(
        db.Text,
        nullable=False,
        default="",
    )

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_IMAGE_URL,
    )

    price = db.Column(
        db.Float,
        nullable=False,
    )

    created_by = db.Column(
        db.String,
        db.ForeignKey('users.username', ondelete='CASCADE'),
        nullable=False
    )

    # @ classmethod
    # def find_all()

    # @ classmethod
    # def create()

# class Booking(db.Model):
#     """Join table between users and messages (the join represents a like)."""

#     __tablename__ = 'bookings'

#     booking_id = db.Column(
#         db.Integer,
#         nullable=False,
#         primary_key=True,
#     )

#     listing_id = db.Column(
#         db.Integer,
#         db.ForeignKey('listings.id', ondelete='CASCADE'),
#         nullable=False,
#     )

#     owner_id = db.Column(
#         db.String,
#         db.ForeignKey('users.username', ondelete='CASCADE'),
#         nullable=False,
#     )

#     renter_id = db.Column(
#         db.String,
#         db.ForeignKey('users.username', ondelete='CASCADE'),
#         nullable=False,
#     )


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
