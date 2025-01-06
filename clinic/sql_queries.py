from django.db import connection

# Patient


def add_patient(name, email, phone, age):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Patient (Name, Email, Phone, Age) VALUES (%s, %s, %s, %s)",
            [name, email, phone, age],
        )


def get_all_patients():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Patient")
        rows = cursor.fetchall()
    return rows


def update_patient(patient_id, name, email, phone, age):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Patient SET Name=%s, Email=%s, Phone=%s, Age=%s WHERE Patient_ID=%s",
            [name, email, phone, age, patient_id],
        )


def delete_patient(patient_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM Patient WHERE Patient_ID=%s", [patient_id])

# Doctor


def add_doctor(name, specialty, phone, fee):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Doctor (Name, Specialty, Phone, Fee) VALUES (%s, %s, %s, %s)",
            [name, specialty, phone, fee],
        )


def get_all_doctors():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Doctor")
        rows = cursor.fetchall()
    return rows


def update_doctor(doctor_id, name, specialty, phone, fee):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Doctor SET Name=%s, Specialty=%s, Phone=%s, Fee=%s WHERE Doctor_ID=%s",
            [name, specialty, phone, fee, doctor_id],
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

# Department

def add_department(name, head, floor):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Department (Name, Head, Floor) VALUES (%s, %s, %s)",
            [name, head, floor],
        )


def get_all_departments():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Department")
        rows = cursor.fetchall()
    return rows


def update_department(department_id, name, head, floor):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Department SET Name=%s, Head=%s, Floor=%s WHERE Department_ID=%s",
            [name, head, floor, department_id],
        )


def delete_department(department_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM Department WHERE Department_ID=%s", [department_id])

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
            SELECT a.Appointment_ID, p.Patient_ID, p.Name as Patient, 
                   d.Doctor_ID, d.Name as Doctor, a.Date, a.Time 
            FROM Appointment a
            JOIN Patient p ON a.Patient_ID = p.Patient_ID
            JOIN Doctor d ON a.Doctor_ID = d.Doctor_ID
        """)
        return cursor.fetchall()


# Prescription

def add_prescription(appointment_id, department_id, medicines, notes):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Prescription (Appointment_ID, Department_ID, Medicines, Notes) VALUES (%s, %s, %s, %s)",
            [appointment_id, department_id, medicines, notes],
        )

def update_prescription(prescription_id, appointment_id, department_id, medicines, notes):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Prescription SET Appointment_ID=%s, Department_ID=%s, Medicines=%s, Notes=%s WHERE Prescription_ID=%s",
            [appointment_id, department_id, medicines, notes, prescription_id],
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
            SELECT p.Prescription_ID, a.Appointment_ID, pt.Name as Patient, 
                   d.Name as Doctor, a.Date, dp.Department_ID, dp.Name as Department,
                   p.Medicines, p.Notes
            FROM Prescription p
            JOIN Appointment a ON p.Appointment_ID = a.Appointment_ID
            JOIN Patient pt ON a.Patient_ID = pt.Patient_ID
            JOIN Doctor d ON a.Doctor_ID = d.Doctor_ID
            JOIN Department dp ON p.Department_ID = dp.Department_ID
        """)
        return cursor.fetchall()