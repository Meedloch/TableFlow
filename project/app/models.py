from app import db

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price_per_person = db.Column(db.Float, nullable=False)

# Exemple de table pour stocker les devis
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_size = db.Column(db.Integer, nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
