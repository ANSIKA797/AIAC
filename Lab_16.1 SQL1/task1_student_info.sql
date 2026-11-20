CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    credits INTEGER NOT NULL
);

CREATE TABLE Enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

INSERT INTO Students VALUES (1, 'Adagiri Ansika', 'ansika@sru.edu'), (2, 'Rohan Verma', 'rohan@sru.edu');
INSERT INTO Courses VALUES (101, 'AI Assisted Coding', 4), (102, 'Database Systems', 3);
INSERT INTO Enrollments VALUES (1, 1, 101), (2, 1, 102), (3, 2, 101);

-- 1. Fetch all courses enrolled by student_id = 1
SELECT s.name AS student, c.course_name, c.credits
FROM Enrollments e
JOIN Students s ON e.student_id = s.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE s.student_id = 1;

-- 2. Count number of students in each course
SELECT c.course_name, COUNT(e.student_id) AS student_count
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;
