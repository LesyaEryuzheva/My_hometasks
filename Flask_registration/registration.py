from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


registration = Flask(__name__)
registration.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guests.db'
registration.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(registration)


class Persone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(15), nullable=True)
    age = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Persone {self.id}>'


@registration.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        surname = request.form['surname']
        name = request.form['name']
        age = request.form['age']
        phone_number = request.form['phone_number']

        persone = Persone(surname=surname, name=name, age=age, phone_number=phone_number)

        try:
            db.session.add(persone)
            db.session.commit()
            return redirect('/')
        except Exception as exc:
            return f'Произошла ошибка: {exc}'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    registration.run(debug=True)

