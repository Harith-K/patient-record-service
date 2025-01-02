from flask import Flask
from app.models import db
from app.routes import patient_blueprint

def create_app():
    app = Flask(__name__)
    
    # MySQL database URI
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:Harith1673@healthsync-db.c1c4ousc21sc.us-east-1.rds.amazonaws.com:3306/healthsync"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Ensure tables are created
    with app.app_context():
        db.create_all()

    app.register_blueprint(patient_blueprint)
    return app
