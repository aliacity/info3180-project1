from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class ContactForm(FlaskForm):
    fname = StringField('First Name',
    validators=[DataRequired(), Length (max=20)])
    
    lname = StringField('Last Name',
    validators=[DataRequired()])
    
    gender = SelectField('Gender', choices=[('s',"Select Gender"),('m', 'Male'), ('f', 'Female')])
    
    email = StringField('Email',
    validators=[DataRequired()])
    
    location= StringField('Location',
    validators=[DataRequired()])
    
    biography = StringField('Biography',
    validators=[DataRequired()])
    
    profpic = FileField('ProfilePic', validators=[FileRequired('This field cannot be left empty'),FileAllowed(['jpg','png','jpeg'],'File format not allowed')])
    
    