import os
from flask import Blueprint, request, redirect, render_template
from app.models import Reservation
from app import db

bp = Blueprint('main', __name__)

# URL du frontend
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://ec2-51-20-132-244.eu-north-1.compute.amazonaws.com:8080')

@bp.route("/submit-reservation", methods=["POST"])
def submit_reservation():
    # Récupération et traitement des données
    data = request.form
    people_count = int(data.get("peopleCount"))
    classic_count = int(data.get("classicCount"))
    tasting_count = int(data.get("tastingCount"))
    wine_count = int(data.get("wineSupplementCount"))
    reservation_date = data.get("reservationDate")
    reservation_time = data.get("reservationTime")
    first_name = data.get("firstName")
    last_name = data.get("lastName")
    email = data.get("email")
    phone = data.get("phone")

    # Calculer le coût total
    total_price = (classic_count * 40) + (tasting_count * 60) + (wine_count * 20)

    # Enregistrer en base de données
    reservation = Reservation(
        people_count=people_count,
        classic_count=classic_count,
        tasting_count=tasting_count,
        wine_count=wine_count,
        reservation_date=reservation_date,
        reservation_time=reservation_time,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone
    )
    db.session.add(reservation)
    db.session.commit()

    # Retourner les détails de la réservation en JSON
    return {
        "status": "success",
        "reservation": {
            "Nombre de personnes": people_count,
            "Option classique (40€)": classic_count,
            "Option dégustation (60€)": tasting_count,
            "Supplément vin (20€)": wine_count,
            "Date": reservation_date,
            "Heure": reservation_time,
            "Prénom": first_name,
            "Nom": last_name,
            "Email": email,
            "Téléphone": phone,
            "Prix total (€)": total_price,
        }
    }, 200


@bp.route("/")
def index():
    return render_template("index.html")
