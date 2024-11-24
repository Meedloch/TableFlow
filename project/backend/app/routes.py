from flask import Blueprint, request, jsonify
from app.models import Reservation
from app import db

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("form.html")

@bp.route("/submit-reservation", methods=["POST"])
def submit_reservation():
    # Récupération et traitement des données
    data = request.form
    reservation = {
        "Nombre de personnes": data.get("peopleCount"),
        "Option classique (40€)": data.get("classicCount"),
        "Option dégustation (60€)": data.get("tastingCount"),
        "Supplément vin (20€)": data.get("wineSupplementCount"),
        "Date": data.get("reservationDate"),
        "Heure": data.get("reservationTime"),
        "Prénom": data.get("firstName"),
        "Nom": data.get("lastName"),
        "Email": data.get("email"),
        "Téléphone": data.get("phone"),
        "Prix total (€)": (
            int(data.get("classicCount")) * 40 +
            int(data.get("tastingCount")) * 60 +
            int(data.get("wineSupplementCount")) * 20
        ),
    }

    # Afficher la page result.html avec les détails
    return render_template("result.html", reservation=reservation)


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
