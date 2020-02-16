from flask_wtf import FlaskForm
from wtforms.fields import TextField 
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    username = TextField('Please enter your full name', validators=[DataRequired()])
    email = TextField('Please enter your e-mail address', validators=[DataRequired(), Email()]) 
    textarea = TextField('Please enter the message you would like to send', validators=[DataRequired()])
    subject = TextField('Please enter the subject for your message', validators=[DataRequired()])