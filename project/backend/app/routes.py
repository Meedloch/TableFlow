from flask import Blueprint, request, jsonify
from app.models import Reservation
from app import db

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("form.html")

@bp.route("/submit-reservation", methods=["POST"])
def submit_reservation():
    data = request.form
    reservation = Reservation(
        people_count=data.get("peopleCount"),
        classic_count=data.get("classicCount"),
        tasting_count=data.get("tastingCount"),
        wine_count=data.get("wineSupplementCount"),
        reservation_date=data.get("reservationDate"),
        reservation_time=data.get("reservationTime"),
        first_name=data.get("firstName"),
        last_name=data.get("lastName"),
        email=data.get("email"),
        phone=data.get("phone")
    )
    db.session.add(reservation)
    db.session.commit()
    return jsonify({"message": "Réservation enregistrée avec succès."})

def is_valid_date(date_str):
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        if date.weekday() not in [1, 2, 3, 4, 5]:  # Mardi à samedi
            return False
        return True
    except ValueError:
        return False

def is_valid_time(date_str, time_str):
    try:
        time = datetime.datetime.strptime(time_str, "%H:%M").time()
        return datetime.time(11, 30) <= time <= datetime.time(13, 30) or datetime.time(19, 30) <= time <= datetime.time(21, 30)
    except ValueError:
        return False
