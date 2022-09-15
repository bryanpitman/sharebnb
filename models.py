from werkzeug.utils import secure_filename
import os
import botocore
import boto3
from flask_sqlalchemy import SQLAlchemy
import dotenv
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()


dotenv.load_dotenv()


db = SQLAlchemy()


LOCATION_IMAGE_URL = os.getenv('IMAGE_URL')


class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    username = db.Column(
        db.String(length=50),
        primary_key=True,
        unique=True,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    bio = db.Column(
        db.Text,
        default=""
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    created_listings = db.relationship(
        'Listing', foreign_keys='Listing.created_by', backref='user')

    def __repr__(self):
        return f"<User # {self.username}, {self.email}>"

    @classmethod
    def signup(cls, username, password, email, bio):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            password=hashed_pwd,
            email=email,
            bio=bio
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
        autoincrement=True
    )

    title = db.Column(
        db.Text,
        nullable=False,
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
    )

    price = db.Column(
        db.Numeric(10, 0),
        nullable=False,
        default=0,
    )

    created_by = db.Column(
        db.String,
        db.ForeignKey('users.username', ondelete='CASCADE'),
        nullable=False
    )

    @classmethod
    def create(cls, data, file, username):
        """
        Creates a new listing. 
        Establishes connection to AWS server and uploads. 
        Adds new listing in the db.
        Returns new listing.
        """

        filename = secure_filename(file.filename)

        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )

        s3.upload_fileobj(
            file,
            os.getenv("AWS_BUCKET_NAME"),
            file.filename,
            ExtraArgs={"ACL": "public-read"}
        )

        new_listing = Listing(
            title=data['title'],
            description=data['description'],
            location=data['location'],
            photo_url=f"{LOCATION_IMAGE_URL}{filename}",
            price=data['price'],
            created_by=username
        )

        db.session.add(new_listing)
        return new_listing


def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)
