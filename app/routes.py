from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app.models import db, Patient

patient_blueprint = Blueprint("patients", __name__)

# API Routes
@patient_blueprint.route("/api/patients", methods=["POST"])
def add_patient_api():
    data = request.get_json()
    new_patient = Patient(
        name=data["name"],
        age=data["age"],
        medical_history=data.get("medical_history", ""),
        prescriptions=data.get("prescriptions", ""),
        lab_results=data.get("lab_results", "")
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient added successfully", "patient": new_patient.to_dict()}), 201

@patient_blueprint.route("/api/patients/<int:id>", methods=["GET"])
def get_patient_api(id):
    patient = Patient.query.get_or_404(id)
    return jsonify(patient.to_dict())

# UI Routes
@patient_blueprint.route("/")
def index():
    patients = Patient.query.all()
    return render_template("index.html", patients=patients)

@patient_blueprint.route("/add", methods=["GET", "POST"])
def add_patient():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        medical_history = request.form["medical_history"]
        prescriptions = request.form["prescriptions"]
        lab_results = request.form["lab_results"]

        new_patient = Patient(
            name=name,
            age=age,
            medical_history=medical_history,
            prescriptions=prescriptions,
            lab_results=lab_results
        )
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for("patients.index"))

    return render_template("add_patient.html")

@patient_blueprint.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_patient(id):
    patient = Patient.query.get_or_404(id)

    if request.method == "POST":
        patient.name = request.form["name"]
        patient.age = request.form["age"]
        patient.medical_history = request.form["medical_history"]
        patient.prescriptions = request.form["prescriptions"]
        patient.lab_results = request.form["lab_results"]

        db.session.commit()
        return redirect(url_for("patients.index"))

    return render_template("edit_patient.html", patient=patient)

@patient_blueprint.route("/delete/<int:id>", methods=["POST"])
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for("patients.index"))
