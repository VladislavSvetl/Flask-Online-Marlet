from flask import Flask, render_template, request, redirect
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

    def __repr__(self):
        return '<Item %r' %self.id


@app.route('/')
@app.route('/index')
def index():
    items = Item.query.order_by(-Item.id).all()
    return render_template('index.html', items=items)


@app.route('/account')
def account_main():
    return render_template('account_main.html')


@app.route('/success_add')
def success_add():
    return render_template('success_add.html')


@app.route('/account/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        tags = request.form['tags']
        description = request.form['description']
        price = request.form['price']
        amount = request.form['amount']

        item = Item(title=title,tags=tags, description=description, price=price, amount=amount)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/success_add')
        except:
            return 'При добавлении произошла ошибка...'

    else:
        return render_template('account_create.html')


if __name__ == '__main__':
    app.run(debug=True)