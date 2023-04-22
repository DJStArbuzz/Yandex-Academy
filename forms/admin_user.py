from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    father_name = StringField('Отчество', validators=[DataRequired()])
    role = StringField('Роль', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Применить')