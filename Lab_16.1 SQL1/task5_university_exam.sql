CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE Subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT NOT NULL
);

CREATE TABLE Exams (
    exam_id INTEGER PRIMARY KEY,
    exam_name TEXT NOT NULL,
    exam_date TEXT NOT NULL
);

CREATE TABLE Results (
    result_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    exam_id INTEGER NOT NULL,
    marks INTEGER NOT NULL CHECK (marks BETWEEN 0 AND 100),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id),
    FOREIGN KEY (exam_id) REFERENCES Exams(exam_id)
);

INSERT INTO Students VALUES (1, 'Adagiri Ansika'), (2, 'Neha Sharma');
INSERT INTO Subjects VALUES (10, 'AI Assisted Coding'), (20, 'Computer Networks');
INSERT INTO Exams VALUES (1, 'Midterm 2026', '2026-10-15');
INSERT INTO Results VALUES (1, 1, 10, 1, 94), (2, 1, 20, 1, 88), (3, 2, 10, 1, 86), (4, 2, 20, 1, 80);

-- 1. Subject-wise marks for student_id = 1
SELECT s.name AS student, sub.subject_name, r.marks
FROM Results r
JOIN Students s ON r.student_id = s.student_id
JOIN Subjects sub ON r.subject_id = sub.subject_id
WHERE r.student_id = 1;

-- 2. Average marks for each subject
SELECT sub.subject_name, ROUND(AVG(r.marks), 2) AS avg_marks
FROM Subjects sub
JOIN Results r ON sub.subject_id = r.subject_id
GROUP BY sub.subject_id, sub.subject_name;
