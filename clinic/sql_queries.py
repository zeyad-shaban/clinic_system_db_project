from django.db import connection

# Patient


def add_patient(first_name, last_name, email, phone, age):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Patient (FirstName, LastName, Email, Phone, Age) VALUES (%s, %s, %s, %s, %s)",
            [first_name, last_name, email, phone, age],
        )


def get_all_patients():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Patient")
        rows = cursor.fetchall()
    return rows


def update_patient(patient_id, first_name, last_name, email, phone, age):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Patient SET FirstName=%s, LastName=%s, Email=%s, Phone=%s, Age=%s WHERE Patient_ID=%s",
            [first_name, last_name, email, phone, age, patient_id],
        )


def delete_patient(patient_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM Patient WHERE Patient_ID=%s", [patient_id])

# Doctor


def add_doctor(first_name, last_name, specialty, phone, fee):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Doctor (FirstName, LastName, Specialty, Phone, Fee) VALUES (%s, %s, %s, %s, %s)",
            [first_name, last_name, specialty, phone, fee],
        )


def get_all_doctors():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Doctor")
        rows = cursor.fetchall()
    return rows


def update_doctor(doctor_id, first_name, last_name, specialty, phone, fee):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Doctor SET FirstName=%s, LastName=%s, Specialty=%s, Phone=%s, Fee=%s WHERE Doctor_ID=%s",
            [first_name, last_name, specialty, phone, fee, doctor_id],
        )


def delete_doctor(doctor_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Doctor WHERE Doctor_ID=%s", [doctor_id])


def get_doctors_count_by_specialty():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT Specialty, COUNT(*) FROM Doctor GROUP BY Specialty")
        return cursor.fetchall()


def get_average_doctor_fee():
    with connection.cursor() as cursor:
        cursor.execute("SELECT AVG(Fee) FROM Doctor")
        return cursor.fetchone()


# Appointment

def add_appointment(patient_id, doctor_id, date, time):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Appointment (Patient_ID, Doctor_ID, Date, Time) VALUES (%s, %s, %s, %s)",
            [patient_id, doctor_id, date, time],
        )


def get_all_appointments():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Appointment")
        rows = cursor.fetchall()
    return rows


def update_appointment(appointment_id, patient_id, doctor_id, date, time):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Appointment SET Patient_ID=%s, Doctor_ID=%s, Date=%s, Time=%s WHERE Appointment_ID=%s",
            [patient_id, doctor_id, date, time, appointment_id],
        )


def delete_appointment(appointment_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Appointment WHERE Appointment_ID=%s", [
                       appointment_id])


def get_appointments_with_details():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT Appointment.Appointment_ID, 
                   Patient.Patient_ID,
                   Patient.FirstName || ' ' || Patient.LastName as Patient, 
                   Doctor.Doctor_ID,
                   Doctor.FirstName || ' ' || Doctor.LastName as Doctor,
                   Appointment.Date, 
                   Appointment.Time,
                   julianday('now') - julianday(Appointment.Date || ' ' || Appointment.Time) AS TimeElapsed
            FROM Appointment
            JOIN Patient ON Appointment.Patient_ID = Patient.Patient_ID
            JOIN Doctor ON Appointment.Doctor_ID = Doctor.Doctor_ID
        """)
        return cursor.fetchall()

# Prescription


def add_prescription(appointment_id, insurance_id, medicines, notes):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Prescription (Appointment_ID, Insurance_ID, Medicines, Notes) VALUES (%s, %s, %s, %s)",
            [appointment_id, insurance_id, medicines, notes],
        )


def update_prescription(prescription_id, appointment_id, insurance_id, medicines, notes):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Prescription SET Appointment_ID=%s, Insurance_ID=%s, Medicines=%s, Notes=%s WHERE Prescription_ID=%s",
            [appointment_id, insurance_id, medicines, notes, prescription_id],
        )


def get_all_prescriptions():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Prescription")
        rows = cursor.fetchall()
    return rows


def delete_prescription(prescription_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Prescription WHERE Prescription_ID=%s", [
                       prescription_id])


def get_prescriptions_with_appointment_details():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT Prescription.Prescription_ID, 
                   Appointment.Appointment_ID,
                   Patient.FirstName || ' ' || Patient.LastName as Patient,
                   Doctor.FirstName || ' ' || Doctor.LastName as Doctor,
                   Appointment.Date,
                   Insurance.Insurance_ID,
                   Insurance.Name as Insurance,
                   Prescription.Medicines,
                   Prescription.Notes
            FROM Prescription
            JOIN Appointment ON Prescription.Appointment_ID = Appointment.Appointment_ID
            JOIN Patient ON Appointment.Patient_ID = Patient.Patient_ID
            JOIN Doctor ON Appointment.Doctor_ID = Doctor.Doctor_ID
            LEFT JOIN Insurance ON Prescription.Insurance_ID = Insurance.Insurance_ID
        """)
        return cursor.fetchall()

# Insurance CRUD


def add_insurance(name, provider, coverage):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Insurance (Name, Provider, Coverage) VALUES (%s, %s, %s)",
            [name, provider, coverage],
        )


def get_all_insurance():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Insurance")
        rows = cursor.fetchall()
    return rows


def update_insurance(insurance_id, name, provider, coverage):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Insurance SET Name=%s, Provider=%s, Coverage=%s WHERE Insurance_ID=%s",
            [name, provider, coverage, insurance_id],
        )


def delete_insurance(insurance_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM Insurance WHERE Insurance_ID=%s", [insurance_id])
