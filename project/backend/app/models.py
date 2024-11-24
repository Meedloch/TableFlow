from app import db

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people_count = db.Column(db.Integer, nullable=False)
    classic_count = db.Column(db.Integer, nullable=False)
    tasting_count = db.Column(db.Integer, nullable=False)
    wine_count = db.Column(db.Integer, nullable=False)
    reservation_date = db.Column(db.String(10), nullable=False)
    reservation_time = db.Column(db.String(5), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
