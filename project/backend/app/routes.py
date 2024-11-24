import os
from flask import Blueprint, request, redirect, render_template
from app.models import Reservation
from app import db

bp = Blueprint('main', __name__)

# URL du frontend
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://ec2-51-20-132-244.eu-north-1.compute.amazonaws.com:8080')

@bp.route("/submit-reservation", methods=["POST"])
def submit_reservation():
    try:
        # Récupération et traitement des données
        data = request.get_json()  # Utilisez request.get_json() pour les requêtes POST JSON
        people_count = int(data["peopleCount"])
        classic_count = int(data["classicCount"])
        tasting_count = int(data["tastingCount"])
        wine_count = int(data["wineSupplementCount"])
        reservation_date = data["reservationDate"]
        reservation_time = data["reservationTime"]
        first_name = data["firstName"]
        last_name = data["lastName"]
        email = data["email"]
        phone = data["phone"]

        # Calcul du coût total
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
            phone=phone,
        )
        db.session.add(reservation)
        db.session.commit()

        # Retourner les détails de la réservation
        return jsonify({
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
            },
        }), 200
    except Exception as e:
        # En cas d'erreur, renvoyer un statut HTTP 400 avec un message
        return jsonify({"status": "error", "message": str(e)}), 400


@bp.route("/")
def index():
    return render_template("index.html")
