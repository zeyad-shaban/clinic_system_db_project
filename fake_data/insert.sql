-- Reset Tables
DELETE FROM Prescription;
DELETE FROM Appointment;
DELETE FROM Insurance;
DELETE FROM Doctor;
DELETE FROM Patient;

DELETE FROM sqlite_sequence;

-- Insert Patients
INSERT INTO Patient (Name, Email, Phone, Age) 
VALUES 
('John Doe', 'john1@email.com', '123-456-7890', 35),
('Jane Smith', 'jane2@email.com', '234-567-8901', 28),
('Mike Brown', 'mike3@email.com', '345-678-9012', 40),
('Sara White', 'sara4@email.com', '456-789-0123', 22),
('Emma Green', 'emma5@email.com', '567-890-1234', 30),
('Chris Blue', 'chris6@email.com', '678-901-2345', 50),
('Anna Black', 'anna7@email.com', '789-012-3456', 45),
('Tom Grey', 'tom8@email.com', '890-123-4567', 29),
('Lisa Yellow', 'lisa9@email.com', '901-234-5678', 33),
('Jake Red', 'jake10@email.com', '012-345-6789', 38);

-- Insert Doctors
INSERT INTO Doctor (Name, Specialty, Phone, Fee) 
VALUES 
('Dr. Smith', 'Cardiology', '098-765-4321', 150),
('Dr. Johnson', 'Dermatology', '111-222-3333', 120),
('Dr. Lee', 'Neurology', '222-333-4444', 200),
('Dr. Kim', 'Orthopedics', '333-444-5555', 180),
('Dr. Brown', 'Pediatrics', '444-555-6666', 130),
('Dr. Wilson', 'Radiology', '555-666-7777', 170),
('Dr. Taylor', 'Urology', '666-777-8888', 140),
('Dr. Davis', 'Oncology', '777-888-9999', 250),
('Dr. Martinez', 'Gynecology', '888-999-0000', 160),
('Dr. Garcia', 'Psychiatry', '999-000-1111', 190);

-- Insert Appointments
INSERT INTO Appointment (Patient_ID, Doctor_ID, Date, Time) 
VALUES 
(1, 1, '2024-03-20', '14:30'),
(2, 2, '2024-03-21', '10:00'),
(3, 3, '2024-03-22', '11:30'),
(4, 4, '2024-03-23', '09:45'),
(5, 5, '2024-03-24', '13:15'),
(6, 6, '2024-03-25', '15:00'),
(7, 7, '2024-03-26', '08:30'),
(8, 8, '2024-03-27', '12:00'),
(9, 9, '2024-03-28', '16:45'),
(10, 10, '2024-03-29', '14:00');

-- Insert Insurance
INSERT INTO Insurance (Name, Provider, Coverage) 
VALUES 
('Basic Health', 'Provider A', 80),
('Comprehensive Health', 'Provider B', 90),
('Emergency Coverage', 'Provider C', 70),
('Family Plan', 'Provider D', 85),
('Individual Premium', 'Provider E', 95);

-- Insert Prescriptions
INSERT INTO Prescription (Appointment_ID, Insurance_ID, Medicines, Notes) 
VALUES 
(1, 1, 'Aspirin 100mg', 'Take twice daily'),
(2, 2, 'Ibuprofen 200mg', 'Take after meals'),
(3, 3, 'Paracetamol 500mg', 'Take three times daily'),
(4, NULL, 'Amoxicillin 250mg', 'Take with water'), -- No insurance
(5, 4, 'Vitamin C 1000mg', 'Take once daily'),
(6, NULL, 'Loratadine 10mg', 'Take as needed'), -- No insurance
(7, 5, 'Metformin 500mg', 'Take before meals'),
(8, 1, 'Losartan 50mg', 'Take in the morning'),
(9, 2, 'Atorvastatin 20mg', 'Take at bedtime'),
(10, 3, 'Omeprazole 20mg', 'Take before breakfast');
