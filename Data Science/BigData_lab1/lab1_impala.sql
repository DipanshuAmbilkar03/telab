CREATE DATABASE IF NOT EXISTS college_db;
USE college_db;

CREATE TABLE IF NOT EXISTS students (
    student_id INT,
    student_name STRING,
    department STRING,
    cgpa DOUBLE
)
STORED AS PARQUET;

INSERT INTO students VALUES
(1, 'Aarav', 'CSE', 8.6),
(2, 'Isha', 'IT', 9.1),
(3, 'Rohan', 'ECE', 7.8),
(4, 'Meera', 'CSE', 8.9),
(5, 'Kabir', 'IT', 7.5);

SELECT * FROM students;
SELECT department, COUNT(*) AS total_students FROM students GROUP BY department;
SELECT student_name, cgpa FROM students WHERE cgpa >= 8.5 ORDER BY cgpa DESC;
