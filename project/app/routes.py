from flask import Blueprint, render_template, request, jsonify
import datetime

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("form.html")

@bp.route("/submit-reservation", methods=["POST"])
def submit_reservation():
    data = request.form
    people_count = int(data.get("peopleCount"))
    classic_count = int(data.get("classicCount"))
    tasting_count = int(data.get("tastingCount"))
    wine_count = int(data.get("wineSupplementCount"))

    allergies = data.get("allergies")
    allergy_details = data.get("allergyText") if allergies == "yes" else "Aucune"
    reservation_date = data.get("reservationDate")
    reservation_time = data.get("reservationTime")
    first_name = data.get("firstName")
    last_name = data.get("lastName")
    email = data.get("email")
    phone = data.get("phone")

    # Validation du total des personnes et des choix de menu
    if classic_count + tasting_count != people_count:
        return render_template("error.html", message="Le total des choix de menu doit correspondre au nombre de personnes."), 400

    # Validation des horaires et dates
    if not is_valid_date(reservation_date):
        return render_template("error.html", message="La date choisie n'est pas valide ou en dehors des jours d'ouverture."), 400
    if not is_valid_time(reservation_date, reservation_time):
        return render_template("error.html", message="L'heure choisie n'est pas valide pour ce jour."), 400

    # Calcul du coût total
    total_price = (classic_count * 40) + (tasting_count * 60) + (wine_count * 20)

    # Préparation des détails pour affichage
    reservation = {
        "Nombre de personnes": people_count,
        "Option classique (40€)": classic_count,
        "Option dégustation (60€)": tasting_count,
        "Supplément vin (20€)": wine_count,
        "Allergies": allergy_details,
        "Date": reservation_date,
        "Heure": reservation_time,
        "Prénom": first_name,
        "Nom": last_name,
        "Email": email,
        "Téléphone": phone,
        "Prix total (€)": total_price,
    }

    return render_template("reservation_success.html", reservation=reservation)

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
