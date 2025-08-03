CREATE DATABASE lab;
USE lab;

CREATE TABLE student (
    rollNo INT,
    name VARCHAR(30),
    admis_date DATE,
    PRIMARY KEY (rollNo)
);

CREATE TABLE studData (
    stud_id INT AUTO_INCREMENT,
    rollNo INT,
    dept VARCHAR(30),
    passOut DATE,
    FOREIGN KEY (rollNo) REFERENCES student(rollNo),
    PRIMARY KEY (stud_id)
);

ALTER TABLE student ADD COLUMN email VARCHAR(30);

RENAME TABLE studData TO studinfo;

ALTER TABLE student COMMENT = 'This table contains student data';

INSERT INTO studinfo () VALUE ();
TRUNCATE TABLE studinfo;


INSERT INTO student (rollNo, name, admis_date, email) VALUES
(1, 'Dipanshu', '2023-08-07', 'dipanshu@gmail.com'),
(2, 'Onyx',     '2024-08-27', 'onyx@gmail.com'),
(3, 'Keshav',   '2024-08-23', 'keshav@gmail.com'),
(4, 'Snehil',    '2023-08-02', 'snehil@gmail.com'),
(5, 'Tanvi',    '2023-08-02', 'tanvi@gmail.com'),
(6, 'Rohan',    '2024-07-07', 'rohan@gmail.com'),
(7, 'Aarav',    '2024-03-10', 'aarav@gmail.com');

INSERT INTO studinfo (stud_id, rollNo, dept, passOut, cgpa) VALUES
(NULL, 2, 'AI&DS', '2027-08-07', 8.66),
(NULL, 3, 'AI&DS', '2027-08-07', 8.59),
(NULL, 4, 'AI&DS', '2027-08-07', 7.25),
(NULL, 5, 'Mech',  '2027-08-07', 6.9),
(NULL, 6, 'CS',    '2027-08-07', 9.45),
(NULL, 7, 'CS',    '2027-08-07', 10.0),
(NULL, 1, 'AI&DS', '2027-08-07', NULL);

UPDATE studinfo SET cgpa = NULL WHERE rollNo = 1;


CREATE VIEW viewstud AS
SELECT s.rollNo, s.name, s.email, f.dept, f.cgpa
FROM student AS s
INNER JOIN studinfo AS f ON s.rollNo = f.rollNo;


ALTER TABLE student ADD INDEX id (rollNo);

CALL sys.create_synonym_db('lab', 'New_Lab');

SELECT * FROM student;
SELECT * FROM studinfo;
SELECT * FROM viewstud;
