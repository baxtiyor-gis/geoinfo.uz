from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField

from wtforms import StringField, SubmitField, TextAreaField, FileField, SelectField
from flask_wtf.file import FileRequired, FileAllowed




class CategoryForm(FlaskForm):
    name = StringField('Bo`lim nomi')
    photo = FileField('Bo`lim uchun rasm', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    description = TextAreaField('Bo`lim tarifi')
    submit = SubmitField()




class PostForm(FlaskForm):
    title = StringField('Maqola nomi')
    content = CKEditorField('Maqola matni')
    photo = FileField("Maqola rasmi")
    category = SelectField()
    
    submit = SubmitField()
