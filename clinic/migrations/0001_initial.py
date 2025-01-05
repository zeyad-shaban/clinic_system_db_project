from django.db import migrations


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunSQL(
            """
            CREATE TABLE Patients (
                Patient_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Email TEXT UNIQUE NOT NULL,
                Phone TEXT NOT NULL,
                Age INTEGER NOT NULL
            );

            CREATE TABLE Doctors (
                Doctor_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Specialty TEXT NOT NULL,
                Phone TEXT NOT NULL,
                Fee INTEGER NOT NULL
            );

            CREATE TABLE Departments (
                Department_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Head TEXT NOT NULL,
                Floor INTEGER NOT NULL
            );

            CREATE TABLE Appointments (
                Appointment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Patient_ID INTEGER,
                Doctor_ID INTEGER,
                Date TEXT NOT NULL,
                Time TEXT NOT NULL,
                FOREIGN KEY (Patient_ID) REFERENCES Patients(Patient_ID),
                FOREIGN KEY (Doctor_ID) REFERENCES Doctors(Doctor_ID)
            );

            CREATE TABLE Prescriptions (
                Prescription_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Appointment_ID INTEGER,
                Medicines TEXT NOT NULL,
                Notes TEXT,
                FOREIGN KEY (Appointment_ID) REFERENCES Appointments(Appointment_ID)
            );
            """
        )
    ]