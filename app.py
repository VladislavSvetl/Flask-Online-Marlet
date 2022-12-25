from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/account')
def account_main():
    return render_template('account_main.html')


@app.route('/account/create')
def create():
    return render_template('account_create.html')


if __name__ == '__main__':
    app.run(debug=True)