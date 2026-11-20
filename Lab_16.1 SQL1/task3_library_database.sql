CREATE TABLE Books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL
);

CREATE TABLE Members (
    member_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE Loans (
    loan_id INTEGER PRIMARY KEY,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    loan_date TEXT NOT NULL,
    return_date TEXT,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE INDEX idx_loans_member ON Loans(member_id);
CREATE INDEX idx_loans_return_date ON Loans(return_date);

INSERT INTO Books VALUES (1, 'Clean Code', 'Robert Martin'), (2, 'Operating Systems', 'Silberschatz'), (3, 'DBMS', 'Korth');
INSERT INTO Members VALUES (1, 'Ansika'), (2, 'Siddharth');
INSERT INTO Loans VALUES
    (1, 1, 1, '2026-10-01', NULL),
    (2, 2, 1, '2026-11-10', NULL),
    (3, 3, 2, '2026-09-15', '2026-09-28');

-- 1. Currently issued books (not yet returned)
SELECT b.title, m.name AS borrower, l.loan_date
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL;

-- 2. Overdue books (loan_date older than 30 days from 2026-11-20)
SELECT b.title, m.name AS borrower, l.loan_date
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL AND julianday('2026-11-20') - julianday(l.loan_date) > 30;

-- 3. Count books loaned by each member
SELECT m.name, COUNT(l.loan_id) AS total_loans
FROM Members m
LEFT JOIN Loans l ON m.member_id = l.member_id
GROUP BY m.member_id, m.name;
