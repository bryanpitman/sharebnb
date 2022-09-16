from sqlalchemy import or_
import os
from dotenv import load_dotenv
from forms import ListingAddForm, UserAddForm, CSRFProtection, LoginForm
from sqlalchemy.exc import IntegrityError

from flask import (
    Flask, render_template, request, flash, redirect, session, g
)

from models import (
    db, connect_db, User, Listing)

load_dotenv()

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sharebnb'
# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     os.environ['DATABASE_URL'].replace("postgres://", "postgresql://"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
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

    if g.user:
        return redirect("/")

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

    if g.user:
        return redirect("/")

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


@app.post('/listings/<int:listing_id>/delete')
def delete_listing(listing_id):
    """Delete listing."""

    form = g.csrf_form

    listing = Listing.query.get_or_404(listing_id)

    if not form.validate_on_submit() or (g.user.username != listing.created_by):
        flash("Access unauthorized.", "danger")
        return redirect("/")

    db.session.delete(listing)
    db.session.commit()

    flash("Listing deleted.", "success")
    return redirect("/listings")


@app.post('/listings/<int:listing_id>/reserve')
def reserve_listing(listing_id):
    """Reserve a listing."""

    form = g.csrf_form

    listing = Listing.query.get_or_404(listing_id)
    curr_user = g.user.username

    if not form.validate_on_submit() or not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/listings/{listing_id}")

    listing.rented_by = curr_user
    #TODO: booking = Booking(listing_id, user)
    # TODO: add logic if property is already book
    # TODO: add status to listing
    db.session.commit()

    flash("Booking Confirmed!", "success")
    return redirect(f"/listings/{listing_id}")


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
        return redirect(f"/users/{username}")

    return render_template('add-listing.html', form=form)

##############################################################################
# General user routes:


@app.get('/users/<username>')
def user_profile(username):
    """Page with listing of properties rented by logged-in user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    listings = Listing.query.filter_by(created_by=username)
    user = User.query.get_or_404(username)

    return render_template('/user-page.html', user=user, listings=listings)


@app.get('/users/<username>/reservations')
def user_reservations(username):
    """Page with listing of properties rented by logged-in user."""

    curr_user = g.user.username

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    if curr_user != username:
        return redirect(f"/users/{curr_user}/reservations")

    listings = Listing.query.filter_by(rented_by=username)
    user = User.query.get_or_404(username)

    return render_template('/my-reservations.html', user=user, listings=listings)


##############################################################################
# General routes:

@app.get('/')
def homepage():
    """ show listings page."""

    return redirect("/listings")


@app.errorhandler(404)
def page_not_found(e):
    """404 NOT FOUND page."""

    return render_template('404.html'), 404
