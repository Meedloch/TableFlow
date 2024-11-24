import os
from flask import Blueprint, request, redirect, render_template
from app.models import Reservation
from app import db

bp = Blueprint('main', __name__)

# URL du frontend
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://ec2-51-20-132-244.eu-north-1.compute.amazonaws.com:8080')

@bp.route("/submit-reservation", methods=["POST"])
def submit_reservation():
    # Récupérer les données du formulaire
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

    # Préparer les données pour le template
    reservation = {
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

    # Retourner la page result.html avec les données
    return render_template("result.html", reservation=reservation)


@bp.route("/")
def index():
    return render_template("index.html")
