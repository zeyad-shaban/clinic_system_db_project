from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # Patients URLs
    path("patients/", views.patients_page, name="patients_page"),
    path("api/patients/", views.get_patients, name="get_patients"),
    path("api/patients/add/", views.add_new_patient, name="add_new_patient"),
    path('api/patients/delete/<int:patient_id>/',
         views.delete_patient_view, name='delete_patient'),
    path('api/patients/update/<int:patient_id>/',
         views.update_patient_view, name='update_patient'),

    # Doctors URLs
    path("doctors/", views.doctors_page, name="doctors_page"),
    path("api/doctors/", views.get_doctors, name="get_doctors"),
    path("api/doctors/add/", views.add_new_doctor, name="add_new_doctor"),
    path("api/doctors/delete/<int:doctor_id>/",
         views.delete_doctor_view, name="delete_doctor"),
    path("api/doctors/update/<int:doctor_id>/",
         views.update_doctor_view, name="update_doctor"),
    path("api/stats/doctors/", views.get_doctor_stats, name="doctor_stats"),

    # Departments URLs
    path("departments/", views.departments_page, name="departments_page"),
    path("api/departments/", views.get_departments, name="get_departments"),
    path("api/departments/add/", views.add_new_department,
         name="add_new_department"),
    path("api/departments/delete/<int:department_id>/",
         views.delete_department_view, name="delete_department"),
    path("api/departments/update/<int:department_id>/",
         views.update_department_view, name="update_department"),

    # Appointments URLs
    path("appointments/", views.appointments_page, name="appointments_page"),
    path("api/appointments/", views.get_appointments, name="get_appointments"),
    path("api/appointments/add/", views.add_new_appointment,
         name="add_new_appointment"),
    path("api/appointments/delete/<int:appointment_id>/",
         views.delete_appointment_view, name="delete_appointment"),
    path("api/appointments/update/<int:appointment_id>/",
         views.update_appointment_view, name="update_appointment"),
    path("api/detailed/appointments/", views.get_detailed_appointments,
         name="detailed_appointments"),

    # Prescriptions URL
    path("prescriptions/", views.prescriptions_page, name="prescriptions_page"),
    path("api/prescriptions/", views.get_prescriptions, name="get_prescriptions"),
    path("api/prescriptions/add/", views.add_new_prescription,
         name="add_new_prescription"),
    path("api/prescriptions/delete/<int:prescription_id>/",
         views.delete_prescription_view, name="delete_prescription"),
    path("api/prescriptions/update/<int:prescription_id>/",
         views.update_prescription_view, name="update_prescription"),
    path("api/detailed/prescriptions/", views.get_detailed_prescriptions,
         name="detailed_prescriptions"),
]
