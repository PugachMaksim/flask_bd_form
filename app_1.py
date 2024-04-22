"""Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован."""

from flask import Flask, render_template, request, url_for
from flask_wtf import CSRFProtect
from form import Register
from sqlalchemy import exc
from model import db, Account

app = Flask(__name__)
app.config['SECRET_KEY'] = '1168184684684cse4fs684gs4gbz6dga6g4a64x8b4zb4d68fz6ag'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


# @app.route('/')
# def index():
#     db = get_db()
#     dbase = FDataBase(db)
#     return render_template('index.html', menu=dbase.getMenu())

@app.route('/')
def index():
    return "Hello"


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('ok')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = Register()
    if request.method == 'POST' and form.validate():
        u = Account()
        u.user_name = form.user_name.data
        u.user_surname = form.user_surname.data
        u.user_email = form.user_email.data
        u.password = form.password.data
        try:
            db.session.add(u)
            return db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
