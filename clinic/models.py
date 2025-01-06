from django.db import models

class Patient(models.Model):
    Patient_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Phone = models.CharField(max_length=20)
    Age = models.IntegerField()

    class Meta:
        db_table = 'Patients'

class Doctor(models.Model):
    Doctor_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Specialty = models.CharField(max_length=50)
    Phone = models.CharField(max_length=20)
    Fee = models.IntegerField()

    class Meta:
        db_table = 'Doctors'

class Department(models.Model):
    Department_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Head = models.CharField(max_length=100)
    Floor = models.IntegerField()

    class Meta:
        db_table = 'Departments'

class Appointment(models.Model):
    Appointment_ID = models.AutoField(primary_key=True)
    Patient_ID = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='Patient_ID')
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE, db_column='Doctor_ID')
    Date = models.DateField()
    Time = models.TimeField()

    class Meta:
        db_table = 'Appointments'

class Prescription(models.Model):
    Prescription_ID = models.AutoField(primary_key=True)
    Appointment_ID = models.ForeignKey(Appointment, on_delete=models.CASCADE, db_column='Appointment_ID')
    Medicines = models.TextField()
    Notes = models.TextField(null=True)

    class Meta:
        db_table = 'Prescriptions'
