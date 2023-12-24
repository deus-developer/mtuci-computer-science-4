import psycopg2
from flask import Flask, render_template, request

from validators import username_validator, password_validator

app = Flask(__name__)
connection = psycopg2.connect(
    database="service_db",
    user="postgres",
    password="пароль",
    host="localhost",
    port="5432"
)


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    if not username_validator(username):
        return

    password = request.form.get('password')
    if not password_validator(password):
        return

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT full_name FROM service.users WHERE login=%s AND password=%s",
            (username, password)
        )
        row = cursor.fetchone()

    if row is None:
        return

    full_name, = row
    return render_template('account.html', full_name=full_name)
