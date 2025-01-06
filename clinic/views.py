from django.shortcuts import render
from django.http import JsonResponse
from .sql_queries import (
    add_patient, get_all_patients, update_patient, delete_patient,
    add_doctor, get_all_doctors, update_doctor, delete_doctor,
    add_appointment, get_all_appointments, update_appointment, delete_appointment,
    add_prescription, get_all_prescriptions, update_prescription, delete_prescription,
    get_doctors_count_by_specialty, get_average_doctor_fee,
    get_appointments_with_details, get_prescriptions_with_appointment_details,
    add_insurance, get_all_insurance, update_insurance, delete_insurance
)


def home(request):
    return render(request, "clinic/home.html")

# Patients CRUD APIs


def patients_page(request):
    return render(request, "clinic/patients.html")


def get_patients(request):
    patients = get_all_patients()
    data = [
        {"id": p[0], "name": p[1], "email": p[2], "phone": p[3], "age": p[4]}
        for p in patients
    ]
    return JsonResponse({"patients": data})


def add_new_patient(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        age = request.POST["age"]
        add_patient(name, email, phone, age)
        return JsonResponse({"message": "Patient added successfully!"})


def delete_patient_view(request, patient_id):
    if request.method == "POST":
        delete_patient(patient_id)
        return JsonResponse({"message": "Patient deleted successfully"})


def update_patient_view(request, patient_id):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        age = request.POST["age"]
        update_patient(patient_id, name, email, phone, age)
        return JsonResponse({"message": "Patient updated successfully"})

# Doctors CRUD APIs


def doctors_page(request):
    return render(request, "clinic/doctors.html")


def get_doctors(request):
    doctors = get_all_doctors()
    data = [
        {"id": d[0], "name": d[1], "specialty": d[2],
            "phone": d[3], "fee": d[4]}
        for d in doctors
    ]
    return JsonResponse({"doctors": data})


def add_new_doctor(request):
    if request.method == "POST":
        name = request.POST["name"]
        specialty = request.POST["specialty"]
        phone = request.POST["phone"]
        fee = request.POST["fee"]
        add_doctor(name, specialty, phone, fee)
        return JsonResponse({"message": "Doctor added successfully!"})


def delete_doctor_view(request, doctor_id):
    if request.method == "POST":
        delete_doctor(doctor_id)
        return JsonResponse({"message": "Doctor deleted successfully"})


def update_doctor_view(request, doctor_id):
    if request.method == "POST":
        name = request.POST["name"]
        specialty = request.POST["specialty"]
        phone = request.POST["phone"]
        fee = request.POST["fee"]
        update_doctor(doctor_id, name, specialty, phone, fee)
        return JsonResponse({"message": "Doctor updated successfully"})


def get_doctor_stats(request):
    specialty_counts = get_doctors_count_by_specialty()
    avg_fee = get_average_doctor_fee()
    return JsonResponse({
        "specialty_counts": [{"specialty": s[0], "count": s[1]} for s in specialty_counts],
        "average_fee": round(avg_fee[0], 2) if avg_fee[0] else 0
    })


# Appointments CRUD APIs


def appointments_page(request):
    return render(request, "clinic/appointments.html")


def get_appointments(request):
    appointments = get_all_appointments()
    data = [
        {"id": a[0], "patient_id": a[1],
            "doctor_id": a[2], "date": a[3], "time": a[4]}
        for a in appointments
    ]
    return JsonResponse({"appointments": data})


def add_new_appointment(request):
    if request.method == "POST":
        patient_id = request.POST["patient_id"]
        doctor_id = request.POST["doctor_id"]
        date = request.POST["date"]
        time = request.POST["time"]
        add_appointment(patient_id, doctor_id, date, time)
        return JsonResponse({"message": "Appointment added successfully!"})


def delete_appointment_view(request, appointment_id):
    if request.method == "POST":
        delete_appointment(appointment_id)
        return JsonResponse({"message": "Appointment deleted successfully"})


def update_appointment_view(request, appointment_id):
    if request.method == "POST":
        patient_id = request.POST["patient_id"]
        doctor_id = request.POST["doctor_id"]
        date = request.POST["date"]
        time = request.POST["time"]
        update_appointment(appointment_id, patient_id, doctor_id, date, time)
        return JsonResponse({"message": "Appointment updated successfully"})


def get_detailed_appointments(request):
    appointments = get_appointments_with_details()
    data = [
        {
            "id": a[0],
            "patient_id": a[1],
            "patient": a[2],
            "doctor_id": a[3],
            "doctor": a[4],
            "date": a[5],
            "time": a[6]
        } for a in appointments
    ]
    return JsonResponse({"appointments": data})

# Prescriptions CRUD APIs


def prescriptions_page(request):
    return render(request, "clinic/prescriptions.html")


def get_prescriptions(request):
    prescriptions = get_all_prescriptions()
    data = [
        {"id": p[0], "appointment_id": p[1], "medicines": p[2], "notes": p[3]}
        for p in prescriptions
    ]
    return JsonResponse({"prescriptions": data})


def add_new_prescription(request):
    if request.method == "POST":
        appointment_id = request.POST["appointment_id"]
        insurance_id = request.POST["insurance_id"] or None
        medicines = request.POST["medicines"]
        notes = request.POST["notes"]
        add_prescription(appointment_id, insurance_id, medicines, notes)
        return JsonResponse({"message": "Prescription added successfully!"})


def delete_prescription_view(request, prescription_id):
    if request.method == "POST":
        delete_prescription(prescription_id)
        return JsonResponse({"message": "Prescription deleted successfully"})


def update_prescription_view(request, prescription_id):
    if request.method == "POST":
        appointment_id = request.POST["appointment_id"]
        insurance_id = request.POST["insurance_id"] or None
        medicines = request.POST["medicines"]
        notes = request.POST["notes"]
        update_prescription(prescription_id, appointment_id,
                            insurance_id, medicines, notes)
        return JsonResponse({"message": "Prescription updated successfully"})


def get_detailed_prescriptions(request):
    prescriptions = get_prescriptions_with_appointment_details()
    data = [
        {
            "id": p[0],
            "appointment_id": p[1],
            "patient": p[2],
            "doctor": p[3],
            "date": p[4],
            "insurance_id": p[5],
            "insurance": p[6],
            "medicines": p[7],
            "notes": p[8]
        } for p in prescriptions
    ]
    return JsonResponse({"prescriptions": data})

# Insurance CRUD APIs


def insurance_page(request):
    return render(request, "clinic/insurance.html")


def get_insurance(request):
    insurance = get_all_insurance()
    data = [
        {"id": i[0], "name": i[1], "provider": i[2], "coverage": i[3]}
        for i in insurance
    ]
    return JsonResponse({"insurance": data})


def add_new_insurance(request):
    if request.method == "POST":
        name = request.POST["name"]
        provider = request.POST["provider"]
        coverage = request.POST["coverage"]
        add_insurance(name, provider, coverage)
        return JsonResponse({"message": "Insurance added successfully!"})


def delete_insurance_view(request, insurance_id):
    if request.method == "POST":
        delete_insurance(insurance_id)
        return JsonResponse({"message": "Insurance deleted successfully"})


def update_insurance_view(request, insurance_id):
    if request.method == "POST":
        name = request.POST["name"]
        provider = request.POST["provider"]
        coverage = request.POST["coverage"]
        update_insurance(insurance_id, name, provider, coverage)
        return JsonResponse({"message": "Insurance updated successfully"})