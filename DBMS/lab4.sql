-- Create and use the database
DROP DATABASE IF EXISTS library_lab;
CREATE DATABASE library_lab;
USE library_lab;

-- Drop previous tables & procedure (optional)
DROP TABLE IF EXISTS Fine;
DROP TABLE IF EXISTS Borrower;
DROP PROCEDURE IF EXISTS ProcessReturn;

-- Create Borrower Table
CREATE TABLE IF NOT EXISTS Borrower (
    Roll_no INT,
    Name VARCHAR(100),
    Date_of_Issue DATE,
    Name_of_Book VARCHAR(100),
    Status CHAR(1), -- '1' = issued, 'R' = returned
    PRIMARY KEY (Roll_no, Name_of_Book)
);

-- Create Fine Table
CREATE TABLE IF NOT EXISTS Fine (
    Roll_no INT,
    Date DATE,
    Amt DECIMAL(10,2)
);

-- Insert Sample Data (Updated Names)
INSERT INTO Borrower (Roll_no, Name, Date_of_Issue, Name_of_Book, Status) VALUES
(101, 'Dipanshu', '2025-07-01', 'Database Systems', '1'),
(102, 'Chinu', '2025-08-05', 'Operating Systems', '1'),
(103, 'Pranjal', '2025-08-20', 'Computer Networks', '1'),
(104, 'Ketan', '2025-08-10', 'AI Foundations', '1'),
(105, 'Priya', '2025-09-01', 'DBMS Lab Manual', '1'),
(106, 'Kashish', '2025-09-15', 'Software Engineering', '1'),
(107, 'Raj', '2025-09-18', 'Data Science Basics', '1');

-- Stored Procedure
DELIMITER $$

CREATE PROCEDURE ProcessReturn(
    IN input_Roll_no INT,
    IN input_Name_of_Book VARCHAR(100)
)
BEGIN
    DECLARE v_Date_of_Issue DATE;
    DECLARE v_Days INT;
    DECLARE v_Fine_Amt DECIMAL(10,2) DEFAULT 0;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'An error occurred. Please check input.' AS Error;
    END;

    START TRANSACTION;

    SELECT Date_of_Issue INTO v_Date_of_Issue
    FROM Borrower
    WHERE Roll_no = input_Roll_no
        AND Name_of_Book = input_Name_of_Book
        AND Status = '1'
    FOR UPDATE;

    IF v_Date_of_Issue IS NULL THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No active issue found for this Roll_no / Book!';
    END IF;

    SET v_Days = DATEDIFF(CURDATE(), v_Date_of_Issue);

    IF v_Days > 30 THEN
        SET v_Fine_Amt = v_Days * 50;
    ELSEIF v_Days > 15 THEN
        SET v_Fine_Amt = v_Days * 5;
    ELSE
        SET v_Fine_Amt = 0;
    END IF;

    IF v_Fine_Amt > 0 THEN
        INSERT INTO Fine (Roll_no, Date, Amt)
        VALUES (input_Roll_no, CURDATE(), v_Fine_Amt);
    END IF;

    UPDATE Borrower
    SET Status = 'R'
    WHERE Roll_no = input_Roll_no AND Name_of_Book = input_Name_of_Book;

    COMMIT;

    SELECT CONCAT('Book returned successfully. Fine: ₹', FORMAT(v_Fine_Amt, 2)) AS Message;
END$$

DELIMITER ;

-- ▶ Example Calls (you can change book names / roll no)
CALL ProcessReturn(101, 'Database Systems');
CALL ProcessReturn(105, 'DBMS Lab Manual');

-- ▶ View Updated Tables
SELECT * FROM Borrower;
SELECT * FROM Fine;
