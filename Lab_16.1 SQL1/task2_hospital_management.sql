CREATE TABLE Doctors (
    doctor_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    specialization TEXT NOT NULL
);

CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT UNIQUE NOT NULL
);

CREATE TABLE Appointments (
    appt_id INTEGER PRIMARY KEY,
    doctor_id INTEGER NOT NULL,
    patient_id INTEGER NOT NULL,
    appt_date TEXT NOT NULL CHECK (appt_date LIKE '____-__-__'),
    diagnosis TEXT NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

INSERT INTO Doctors VALUES (1, 'Dr. Kavitha', 'Cardiology'), (2, 'Dr. Arjun', 'Orthopedics');
INSERT INTO Patients VALUES (10, 'Meera Nair', '9876500001'), (11, 'Kiran Rao', '9876500002');
INSERT INTO Appointments VALUES
    (1, 1, 10, '2026-11-10', 'Routine Checkup'),
    (2, 1, 11, '2026-11-12', 'BP Follow-up'),
    (3, 2, 10, '2026-11-15', 'Knee Pain');

-- 1. List appointments for Dr. Kavitha (doctor_id = 1)
SELECT a.appt_id, p.name AS patient, a.appt_date, a.diagnosis
FROM Appointments a
JOIN Patients p ON a.patient_id = p.patient_id
WHERE a.doctor_id = 1;

-- 2. Patient history for patient_id = 10
SELECT a.appt_date, d.name AS doctor, d.specialization, a.diagnosis
FROM Appointments a
JOIN Doctors d ON a.doctor_id = d.doctor_id
WHERE a.patient_id = 10;

-- 3. Count total distinct patients treated by each doctor
SELECT d.name AS doctor, COUNT(DISTINCT a.patient_id) AS total_patients
FROM Doctors d
LEFT JOIN Appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.name;
