from operator import or_
import os
from dotenv import load_dotenv
from forms import ListingAddForm
from helpers import upload_file_to_s3

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


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login and redirect to homepage on success."""


@app.post('/logout')
def logout():
    """Handle logout of user and redirect to homepage."""


##############################################################################
# Standard restful routes for listings:

@app.get('/listings')
def list_listings():
    """Page with listing of listings."""

    # if not g.user:
    #     flash("Access unauthorized.", "danger")
    #     return redirect("/")

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

# TODO:
# TODO:
# TODO:
# TODO:
# TODO:


@app.route('/listings/add', methods=["GET", "POST"])
def add_listings():
    """add a listing to listings."""
    form = ListingAddForm()

    if form.validate_on_submit():

        data = form.data
        file = request.files['photo_url']

        Listing.create(data, file)
        db.session.commit()
        return redirect('/listings')

    return render_template('add-listing.html', form=form)


##############################################################################
# General routes:

@app.get('/')
def homepage():
    """ show home page."""

    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    """404 NOT FOUND page."""

    return render_template('404.html'), 404
