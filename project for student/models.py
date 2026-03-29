from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    passenger_name = db.Column(db.String(100), nullable=False)
    bus_number = db.Column(db.String(20), nullable=False)
    seat_number = db.Column(db.String(10), nullable=False)
    date = db.Column(db.String(20), nullable=False)