from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Configuration de la base de données
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@db/reservations'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Activer CORS
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # Importer les routes
    from app.routes import bp
    app.register_blueprint(bp)

    return app
