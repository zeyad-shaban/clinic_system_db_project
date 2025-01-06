from django.db import migrations


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunSQL(
            """
            CREATE TABLE Patient (
                Patient_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Email TEXT UNIQUE NOT NULL,
                Phone TEXT NOT NULL,
                Age INTEGER NOT NULL
            );

            CREATE TABLE Doctor (
                Doctor_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Specialty TEXT NOT NULL,
                Phone TEXT NOT NULL,
                Fee INTEGER NOT NULL
            );
            
            CREATE TABLE Appointment (
                Appointment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Patient_ID INTEGER,
                Doctor_ID INTEGER,
                Date TEXT NOT NULL,
                Time TEXT NOT NULL,
                FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID) ON DELETE CASCADE,
                FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID) ON DELETE CASCADE
            );

            CREATE TABLE Insurance (
                Insurance_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Provider TEXT NOT NULL,
                Coverage INTEGER NOT NULL
            );

            CREATE TABLE Prescription (
                Prescription_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Appointment_ID INTEGER,
                Insurance_ID INTEGER NULL,
                Medicines TEXT NOT NULL,
                Notes TEXT,
                FOREIGN KEY (Appointment_ID) REFERENCES Appointment(Appointment_ID) ON DELETE CASCADE,
                FOREIGN KEY (Insurance_ID) REFERENCES Insurance(Insurance_ID) ON DELETE CASCADE
            );
    """
        )
    ]
