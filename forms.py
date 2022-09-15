from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
# from flask.ext.uploads import UploadSet, IMAGES

# Signup
# Login
# Add Properties (AWS)


# Messages (bonus)

class CSRFProtection(FlaskForm):
    """CSRFProtection form, intentionally left blank."""

class ListingAddForm(FlaskForm):
    """Form to add a listing."""

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo_url = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Upload Image')
    ])
    price = IntegerField('Price per Night', validators=[DataRequired()])
    # created_by = StringField('Created by', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    bio = TextAreaField('Bio', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])