from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    medical_history = db.Column(db.Text)
    prescriptions = db.Column(db.Text)
    lab_results = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "medical_history": self.medical_history,
            "prescriptions": self.prescriptions,
            "lab_results": self.lab_results
        }
