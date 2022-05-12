from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


person_event = db.Table('person_event',
    db.Column('id_person', db.Integer, db.ForeignKey('persons.id')),
    db.Column('id_event', db.Integer, db.ForeignKey('events.id'))
)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    persons = db.relationship('Event', secondary=person_event, backref=db.backref('persons'))

    def __repr__(self):
        return f'<Person {self.surname}>'


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    month = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Event {self.name}>'


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'Person': Person, 'Event': Event, 'person_event': person_event, create_persons: 'create_persons'}
#
# def create_persons():
#     guest1 = Person(surname='Иванов', age='23', phone_number='123456')
#     guest2 = Person(surname='Сидоров', age='30', phone_number='654321')
#     guest3 = Person(surname='Петров', age='18', phone_number='789654')
#     guest4 = Person(surname='Смирнов', age='33', phone_number='456987')
#     event1 = Event(name='Выставка', month='Август')
#     event2 = Event(name='Концерт', month='Июль')
#     event3 = Event(name='Салют', month='Июнь')
#     guest1.persons.append(event1, event2)
#     guest2.persons.append(event3)
#     guest3.persons.append(event1, event2, event3)
#     guest4.persons.append(event2, event3)
#
#     db.session.add_all(guest1, guest2, guest3, guest4, event1, event2, event3)
#     db.session.commit()

