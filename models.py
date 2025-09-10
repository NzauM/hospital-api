from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Patient(db.Model, SerializerMixin):
    '''
    Patient Class created with name, age, next_of_kin, patient_no
    '''
    serialize_rules = ('-appointments.patient',)
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    next_of_kin = db.Column(db.String)
    patient_no = db.Column(db.String)

    appointments = db.relationship('Appointment',backref='patient')
    # {appointments:[]}

    pass

class Appointment(db.Model, SerializerMixin):
    '''
    Appointment instances to be created with patient_id, notes, doctor_id, day
    '''

    # serialize_only = ('patient_id','day')
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id')) 
    # doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    notes = db.Column(db.String, nullable=True)
    day = db.Column(db.String)

    # {id:1, patient_id:1, notes:'', day:'Tuesday'}





# Doctor 1 Doctor treats how many patients? Many. 
        #1 Patient can be treated by how many doctors? Many. 
# Appointment
        # 1 Appointment has how many doctors? One
        # 1 Doctor can have how many appointments? Many


        # 1 Appointment has how many patients? One
        # 1 Patient can have how many appointments? Many
# Staff
