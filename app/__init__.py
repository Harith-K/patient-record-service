from flask import Flask
from app.models import db
from app.routes import patient_blueprint

def create_app():
    app = Flask(__name__)
    
    # PostgreSQL database URI
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@ec2-52-71-203-176.compute-1.amazonaws.com:5432/meditrack"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Ensure tables are created
    with app.app_context():
        db.create_all()

    app.register_blueprint(patient_blueprint)
    return app
