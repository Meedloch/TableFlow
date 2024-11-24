from flask import Blueprint, request, redirect, render_template
from app.models import Reservation
from app import db

bp = Blueprint('main', __name__)

@bp.route("/submit-reservation", methods=["POST"])
def submit_reservation():
    # Récupération des données du formulaire
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

    # Calcul du prix total
    total_price = (classic_count * 40) + (tasting_count * 60) + (wine_count * 20)

    # Enregistrement en base de données
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

    # Redirection vers la page de résultat dans le frontend
    frontend_result_url = "{{ frontend_url }}/result"
    return redirect(frontend_result_url)

@bp.route("/")
def index():
    return render_template("index.html")
