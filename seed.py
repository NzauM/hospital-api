# provide starter data for our DB.
from models import Patient, db
from faker import Faker
from app import app
import random


fake = Faker()

with app.app_context():
    all_patients = []
    # patient1 = Patient(name="John Doe", age=30, next_of_kin="Jane Doe", patient_no='NWH0023M')
    for i in range(10):
        patient = Patient(name=fake.name(), age = random.randint(1,100), next_of_kin=fake.name(), patient_no=f'NWH{random.randint(1,100)}F')
        all_patients.append(patient)
    db.session.add_all(all_patients)
    db.session.commit()