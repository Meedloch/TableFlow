from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@db/reservations'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importer les routes
    from app.routes import bp
    app.register_blueprint(bp)

    return app
