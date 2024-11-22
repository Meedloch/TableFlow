from app import create_app

# Créer une instance de l'application Flask.
app = create_app()

if __name__ == "__main__":
    # Lancer l'application.
    app.run(debug=True, host="0.0.0.0", port=5000)
