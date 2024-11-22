from app import app, db
from app.models import Menu

# Créer les tables
with app.app_context():
    db.create_all()
    # Ajouter des menus
    if not Menu.query.first():
        db.session.add(Menu(name="Menu Classique", description="Entrée, Plat, Dessert", price_per_person=25.0))
        db.session.add(Menu(name="Menu Gourmet", description="Entrée, Plat, Dessert + Vin", price_per_person=40.0))
        db.session.commit()

# Lancer le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)
