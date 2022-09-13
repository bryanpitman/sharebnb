from flask import (
    Flask, render_template, request, flash, redirect, session, g, abort,
)

from forms import (
    UserAddForm, UserEditForm, LoginForm, MessageForm, CSRFProtection,
)

from models import (
    db, connect_db, User, Listing, DEFAULT_IMAGE_URL, )

app = Flask(__name__)









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


app.get('/listings/<int:listing_id>')
def show_listing(listing_id):
    """Show listing details."""

app.patch('/listings/<int:listing_id>/edit')
def edit_listing(listing_id):
    """Show listing details."""

app.post('/listings/<int:listing_id>/delete')
def delete_listing(listing_id):
    """Show listing details."""


@app.post('/listings')
def add_listings():
    """add a listing to listings."""


##############################################################################
# General routes:

@app.get('/')
def home_page():
    """ show home page."""

@app.errorhandler(404)
def page_not_found(e):
    """404 NOT FOUND page."""

    return render_template('404.html'), 404