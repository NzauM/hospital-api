# import the Flask class
from flask import Flask, make_response, request
from flask_migrate import Migrate
from models import db, Patient
# create an instance of this class, mostly called app, this is the instance responsible for runnin/starting our flask application
app = Flask(__name__)
# app["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospital.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospital.db"
db.init_app(app)
migrate = Migrate(app, db)
# 

@app.route('/welcome')
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
