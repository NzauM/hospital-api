from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    '''
    Patient Class created with name, age, next_of_kin, patient_no
    '''

    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    next_of_kin = db.Column(db.String)
    patient_no = db.Column(db.String)