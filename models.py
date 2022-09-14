from flask_sqlalchemy import SQLAlchemy
import dotenv
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

dotenv.load_dotenv()


db = SQLAlchemy()


DEFAULT_IMAGE_URL = "https://fc-hosted-content.s3.us-west-2.amazonaws.com/share-bnb/evgenia-basyrova.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMSJGMEQCIGETgiNzmp1fHbTCR40guAvt6GuA32%2FJMDQtvC9S3jbfAiAOpghVr53tsS%2BZN8PxgfZvuNa2oFMvtkUN9dLBiW3VFSrtAgir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDU1ODIxNDI1NDg4MyIM4k46mJ7vcHpmAo35KsEChZoS91b1qy8M2ZzVAuEGuZ7yfzqwVF2gaBbHPHAUYNQbRiAjYBJmsmMyM0bUUhPe2ZWKLIYjWySCtjNkUFb4JymN9k7Lwb08aNK%2B4%2BWj59S1uoyePNM4%2F0N26PED04g%2FNDo0AwLilwHJIivy7AswWWRuG3tWygq11yrdfIqwhDcbzpWhbrP3R9eZDX3uCinrcnRoPvly82v6SiZ9uOUVeX9aShIOb5%2BN%2Bl%2F%2FEGfuXslWRv%2Bi1rTrqFmrePBjFXkfNNFfrkY7aA2SZ%2F9zdwTpsVqkZjjFIQO0mxBiSr4K2LMmy08uTiD9kyxNtFBqloIzLzF7%2FKgXA7FIoYYp%2BVPmJClHhNUwCAOMxJ31lW%2BOlktu2zwZOiSo3NI%2BxdBmy3iaonA56EDVFtEsj%2FmvwnH%2FNf%2BHtQOlOYSxBMYurrj7bsOaMK%2BPg5kGOrQC0ooeUnEMeXPodLjXksJmLWincUhr8%2F%2Bk%2BmhrlfhZYFJpEJma8lCH2i1LCqEswIDTJgcAL7L5hknfjoO8jnqH9W6Z3maC55BBLbGMu7F8ckD1PHZmp%2FjdWAsWHfjnHhCRXEfk%2BYT1vZAoSQUnAhuBggJhtVk4O3VRv1afnAKh%2Ba2WItTNovbmhjcoeohFl%2FxvyS7mptxz%2FsdiU8l6c%2F3qvwg9gWvxV2VdvyR2SqxHjJvD%2BS1Vh4QeWv6AENS4DytoDmrqxXu%2Fhb02KmnEn%2FM%2FXk1%2B8CMdAGstS8Ur4slqO3sU68o2AwugAc6u297G%2Bicn5dj4qiJZpOw%2BmV%2FVXOZkvbmG%2FajpsY0GAzsboQXwqbT7iQ1uNFG6gJ%2BvmyKc%2B8w2Kqsb%2FV%2F5iq4nYW8hd1hMIKLLfJs%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220913T230247Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAYD6BJSERQ2BBWHEE%2F20220913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=b725cac7d775c20f6fb577b5e2ee9795b27d28353e3afa8da85034860f693b1e"


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
        'Listing', foreign_keys='Listing.created_by', backref='created_by')

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

    def serialize(self):
        """Serialize User object to dictionary"""

        return {
            "username": self.username,
            "email": self.email,
            "bio": self.bio,
        }


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
        db.Numeric(10, 2),
        nullable=False,
        default=0,
    )

    created_by = db.Column(
        db.String,
        db.ForeignKey('users.username', ondelete='CASCADE'),
        nullable=False
    )

    rented_by = db.Column(
        db.String,
        db.ForeignKey('users.username', ondelete='CASCADE'),
    )

    # @ classmethod
    # def find_all()

    # @ classmethod
    # def create()

    def serialize(self):
        """Serialize to dictionary."""

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "photo_url": self.photo_url,
            "price": str(self.price),
            "created_by": self.created_by,
            "rented_by": self.rented_by
        }

# class Booking(db.Model):
#     """Join table between users and messages (the join represents a like)."""

#     __tablename__ = 'bookings'

#     booking_id = db.Column(
#         db.Integer,
#         nullable=False,
#         primary_key=True,
#         autoincrement=True
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
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)
