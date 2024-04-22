"""Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован."""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Length


# class Register(FlaskForm):
#     user_name = StringField('User_name', validators=[DataRequired()])
#     user_surname = StringField('User_surname', validators=[DataRequired()])
#     user_email = StringField('User_email', validators=[DataRequired(), Email()])
#     # user_email = EmailField('User_email', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
#     confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(), EqualTo('password')])

class Register(FlaskForm):
    user_name = StringField('User_name', [validators.DataRequired(message=None)])
    user_surname = StringField('User_surname', [validators.DataRequired(message=None)])
    user_email = StringField('User_email', [validators.Email(message='Enter a valid Email ID')])
    # user_email = EmailField('User_email', validators=[DataRequired()])
    password = PasswordField('Password', [validators.Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm_Password', [validators.DataRequired(),validators.EqualTo('password',message='пароли должны совпадать')])