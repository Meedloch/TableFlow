from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# Routes
@app.route("/")
def index():
    return render_template("form.html")  # Le formulaire HTML (modifiez avec le bon chemin si nécessaire)

@app.route("/submit-reservation", methods=["POST"])
def submit_reservation():
    # Récupérer les données du formulaire
    data = request.form
    people_count = data.get("peopleCount")
    allergies = data.get("allergies")
    allergy_details = data.get("allergyText") if allergies == "yes" else "Aucune"
    reservation_date = data.get("reservationDate")
    reservation_time = data.get("reservationTime")
    first_name = data.get("firstName")
    last_name = data.get("lastName")
    email = data.get("email")
    phone = data.get("phone")

    # Validation côté serveur
    if not is_valid_date(reservation_date):
        return jsonify({"error": "La date choisie n'est pas valide ou en dehors des jours d'ouverture."}), 400
    if not is_valid_time(reservation_date, reservation_time):
        return jsonify({"error": "L'heure choisie n'est pas valide pour ce jour."}), 400

    # Simuler l'enregistrement dans une base de données ou autre traitement
    # Par exemple, sauvegarde des données dans un fichier ou une DB
    reservation = {
        "Nombre de personnes": people_count,
        "Allergies": allergy_details,
        "Date": reservation_date,
        "Heure": reservation_time,
        "Prénom": first_name,
        "Nom": last_name,
        "Email": email,
        "Téléphone": phone,
    }
    print("Nouvelle réservation : ", reservation)  # À remplacer par un stockage réel

    # Réponse pour confirmer la réservation
    return jsonify({
        "message": "Réservation reçue avec succès.",
        "details": reservation
    })

# Fonctions utilitaires pour les validations
def is_valid_date(date_str):
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        # Vérifier les jours d'ouverture : Mardi (1) à Samedi (5)
        if date.weekday() not in [1, 2, 3, 4, 5]:  # Lundi (0), Dimanche (6)
            return False
        # Vérifier que le samedi soir est ouvert, mais pas samedi midi
        if date.weekday() == 5 and datetime.datetime.now().time() < datetime.time(13, 30):
            return False
        return True
    except ValueError:
        return False

def is_valid_time(date_str, time_str):
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        time = datetime.datetime.strptime(time_str, "%H:%M").time()
        # Heures d'ouverture
        if date.weekday() == 5:  # Samedi
            return datetime.time(19, 30) <= time <= datetime.time(21, 30)
        else:  # Mardi à vendredi
            return (datetime.time(11, 30) <= time <= datetime.time(13, 30) or
                    datetime.time(19, 30) <= time <= datetime.time(21, 30))
    except ValueError:
        return False

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
