# import the Flask class
from flask import Flask, make_response, request
from flask_migrate import Migrate
from models import db, Patient, Appointment
# create an instance of this class, mostly called app, this is the instance responsible for runnin/starting our flask application
app = Flask(__name__)
# app["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospital.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospital.db"
db.init_app(app)
migrate = Migrate(app, db)
# 

@app.route('/')
def welcomefunction():
    return '<h3>Welcome to My App</h3>', 200

@app.route('/login')
def login():
    my_resp = make_response('<h1>You are now logged in. Karibu</h1>',201, {'token':"Mercy's token"})
    return my_resp

@app.route('/create_patient', methods=['POST'])
def create_patient():
    # receive patient details from the client request
    client_data = request.get_json() 

    # and save this patient to the database 
    new_patient = Patient(name=client_data['name'], age=client_data['age'], next_of_kin=client_data['next_of_kin'], patient_no=client_data['patient_no'])
    db.session.add(new_patient)
    db.session.commit()
    resp = make_response({'message':"Patient created successfully"}, 201)
    return resp

# get all patients
@app.route('/list_patients')
def list_patients():
    # selecting all patients in the patients table and return them.
    all_patients = db.session.query(Patient).all()
    # print(all_patients)
    # querying using sqlalchemy will return instances of the class
    # we need to format these instances to a more generic format, e.g JSON/Dictionary
    # hence comes serializers, they enable us to convert an instance to a dictionary, in just one line
    # {id:1, name:"Patient1"}
    patient_list = []
    for patient in all_patients:
        # patient_dict= {"id":patient.id, "name":patient.name}
        patient_dict= patient.to_dict()
        patient_list.append(patient_dict)
    resp = make_response({'data':patient_list}, 200)
    return resp

# url path for creating a new appointment
@app.route('/create_appointment', methods=['POST'])
def create_appointment():
    # receiving appointment details from client request
    appt_details = request.get_json()
    print(appt_details)
    # create an instance of the Appointment class and save it to the DB.
    new_appt = Appointment(patient_id = appt_details['patient_id'], day=appt_details['day'])
    db.session.add(new_appt)
    db.session.commit()
    resp = make_response({'message':"Appointment created successfully"}, 201)
    return resp



