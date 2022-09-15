from operator import or_
import os
from dotenv import load_dotenv
from forms import ListingAddForm, UserAddForm, CSRFProtection, LoginForm
from helpers import upload_file_to_s3
from sqlalchemy.exc import IntegrityError


from flask import (
    Flask, render_template, request, flash, redirect, session, g, abort,
)
# from flask_debugtoolbar import DebugToolbarExtension

# from forms import (
#     UserAddForm, UserEditForm, LoginForm, MessageForm, CSRFProtection,
# )

from models import (
    db, connect_db, User, Listing)

from sqlalchemy import or_

load_dotenv()

CURR_USER_KEY = "curr_user"

app = Flask(__name__)


# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sharebnb'
# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     os.environ['DATABASE_URL'].replace("postgres://", "postgresql://"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']  # TODO: move to S3
# toolbar = DebugToolbarExtension(app)

connect_db(app)


##############################################################################
# User signup/login/logout

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


@app.before_request
def add_csrf_only_form():
    """Add a CSRF-only form so that every route can use it."""

    g.csrf_form = CSRFProtection()


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.username


def do_logout():
    """Log out user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
                bio=form.bio.data
            )
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('user_signup.html', form=form)

        do_login(user)
        return redirect("/")

    else:
        return render_template('/user_signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login and redirect to homepage on success."""
    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(
            form.username.data,
            form.password.data)

        if user:
            do_login(user)
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('/login-form.html', form=form)


@app.post('/logout')
def logout():
    """Handle logout of user and redirect to homepage."""

    form = g.csrf_form

    if not form.validate_on_submit() or not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    do_logout()

    flash("You have successfully logged out.", 'success')
    return redirect("/login")

##############################################################################
# Standard restful routes for listings:


@app.get('/listings')
def list_listings():
    """Page with listing of listings."""

    search = request.args.get('q')

    listings = Listing.query.all()

    if not search:
        listings = Listing.query.all()
    else:
        listings = Listing.query.filter(or_(Listing.location.ilike(f"%{search}%"),
                                            Listing.title.ilike(f"%{search}%"),
                                            Listing.description.ilike(f"%{search}%"))
                                        ).all()

    return render_template('listings.html', listings=listings)


@app.get('/listings/<int:listing_id>')
def show_listing(listing_id):
    """Show listing details."""

    listing = Listing.query.get_or_404(listing_id)

    return render_template('listing-details.html', listing=listing)


@app.post('/listings/<int:listing_id>/edit')
def edit_listing(listing_id):
    """Show listing details."""

    # TODO: FORM


@app.post('/listings/<int:listing_id>/delete')
def delete_listing(listing_id):
    """Show listing details."""

    listing = Listing.query.get_or_404(listing_id)
    db.session.delete(listing)
    db.session.commit()

    return redirect("/listings")


@app.route('/listings/add', methods=["GET", "POST"])
def add_listings():
    """add a listing to listings."""
    if not g.user:
        flash("Please sign-up to create a listing", "warning")
        return redirect("/")

    form = ListingAddForm()

    if form.validate_on_submit():

        data = form.data
        file = request.files['photo_url']
        username = g.user.username

        Listing.create(data, file, username)
        db.session.commit()
        return redirect('/listings')

    return render_template('add-listing.html', form=form)


##############################################################################
# General routes:

@app.get('/')
def homepage():
    """ show home page."""

    return redirect("/listings")


@app.errorhandler(404)
def page_not_found(e):
    """404 NOT FOUND page."""

    return render_template('404.html'), 404


##############################################################################
# General user routes:

@app.get('/users/<username>')
def user_profile(username):
    """Page with listing of properties rented by logged-in user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    listings = Listing.query.filter_by(created_by = username)

    return render_template('/user-page.html', user=g.user, listings = listings)

