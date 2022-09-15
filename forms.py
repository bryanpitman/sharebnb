from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
# from flask.ext.uploads import UploadSet, IMAGES

# Signup
# Login
# Add Properties (AWS)


# Messages (bonus)

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
    created_by = StringField('Created by', validators=[DataRequired()])
