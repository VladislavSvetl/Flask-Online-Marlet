from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    tags = db.Column(db.String(75), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, default=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)


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