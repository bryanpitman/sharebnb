from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length


# Signup
# Login
# Add Properties (AWS)


# Messages (bonus)

class ListingAddForm(FlaskForm):
    """Form to add a listing."""

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo_url = StringField('Photo URL', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    created_by = StringField('Created by', validators=[DataRequired()])


