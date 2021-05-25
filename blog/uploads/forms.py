from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    file_allowed = ['jpg', 'png', 'jpeg','pdf','doc','docx','odt','xls']
    title = StringField('Title', validators=[DataRequired()])
    name = StringField('File Name')
    data = FileField('Upload', validators=[FileRequired(), FileAllowed(file_allowed)])

    submit = SubmitField('Upload')
