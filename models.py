from datetime import datetime
from app import db, login_manager

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    departure_point = db.Column(db.String(100), nullable=False)
    destination_point = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
