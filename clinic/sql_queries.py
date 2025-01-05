from django.db import connection

# Patients


def add_patient(name, email, phone, age):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Patients (Name, Email, Phone, Age) VALUES (%s, %s, %s, %s)",
            [name, email, phone, age],
        )


def get_all_patients():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Patients")
        rows = cursor.fetchall()
    return rows


def update_patient(patient_id, name, email, phone, age):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Patients SET Name=%s, Email=%s, Phone=%s, Age=%s WHERE Patient_ID=%s",
            [name, email, phone, age, patient_id],
        )


def delete_patient(patient_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM Patients WHERE Patient_ID=%s", [patient_id])

# Doctors


def add_doctor(name, specialty, phone, fee):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Doctors (Name, Specialty, Phone, Fee) VALUES (%s, %s, %s, %s)",
            [name, specialty, phone, fee],
        )


def get_all_doctors():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Doctors")
        rows = cursor.fetchall()
    return rows


def update_doctor(doctor_id, name, specialty, phone, fee):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Doctors SET Name=%s, Specialty=%s, Phone=%s, Fee=%s WHERE Doctor_ID=%s",
            [name, specialty, phone, fee, doctor_id],
        )


def delete_doctor(doctor_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Doctors WHERE Doctor_ID=%s", [doctor_id])


def get_doctors_count_by_specialty():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT Specialty, COUNT(*) FROM Doctors GROUP BY Specialty")
        return cursor.fetchall()


def get_average_doctor_fee():
    with connection.cursor() as cursor:
        cursor.execute("SELECT AVG(Fee) FROM Doctors")
        return cursor.fetchone()

# Departments


def add_department(name, head, floor):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Departments (Name, Head, Floor) VALUES (%s, %s, %s)",
            [name, head, floor],
        )


def get_all_departments():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Departments")
        rows = cursor.fetchall()
    return rows


def update_department(department_id, name, head, floor):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Departments SET Name=%s, Head=%s, Floor=%s WHERE Department_ID=%s",
            [name, head, floor, department_id],
        )


def delete_department(department_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM Departments WHERE Department_ID=%s", [department_id])

# Appointments


def add_appointment(patient_id, doctor_id, date, time):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Appointments (Patient_ID, Doctor_ID, Date, Time) VALUES (%s, %s, %s, %s)",
            [patient_id, doctor_id, date, time],
        )


def get_all_appointments():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Appointments")
        rows = cursor.fetchall()
    return rows


def update_appointment(appointment_id, patient_id, doctor_id, date, time):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Appointments SET Patient_ID=%s, Doctor_ID=%s, Date=%s, Time=%s WHERE Appointment_ID=%s",
            [patient_id, doctor_id, date, time, appointment_id],
        )


def delete_appointment(appointment_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Appointments WHERE Appointment_ID=%s", [
                       appointment_id])


def get_appointments_with_details():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT a.Appointment_ID, p.Patient_ID, p.Name as Patient, 
                   d.Doctor_ID, d.Name as Doctor, a.Date, a.Time 
            FROM Appointments a
            JOIN Patients p ON a.Patient_ID = p.Patient_ID
            JOIN Doctors d ON a.Doctor_ID = d.Doctor_ID
        """)
        return cursor.fetchall()
# Prescriptions


def add_prescription(appointment_id, medicines, notes):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Prescriptions (Appointment_ID, Medicines, Notes) VALUES (%s, %s, %s)",
            [appointment_id, medicines, notes],
        )


def get_all_prescriptions():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Prescriptions")
        rows = cursor.fetchall()
    return rows


def update_prescription(prescription_id, appointment_id, medicines, notes):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Prescriptions SET Appointment_ID=%s, Medicines=%s, Notes=%s WHERE Prescription_ID=%s",
            [appointment_id, medicines, notes, prescription_id],
        )


def delete_prescription(prescription_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Prescriptions WHERE Prescription_ID=%s", [
                       prescription_id])


def get_prescriptions_with_appointment_details():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.Prescription_ID, a.Appointment_ID, pt.Name as Patient, 
                   d.Name as Doctor, a.Date, p.Medicines, p.Notes
            FROM Prescriptions p
            JOIN Appointments a ON p.Appointment_ID = a.Appointment_ID
            JOIN Patients pt ON a.Patient_ID = pt.Patient_ID
            JOIN Doctors d ON a.Doctor_ID = d.Doctor_ID
        """)
        return cursor.fetchall()
