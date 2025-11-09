-- Create and use the database
DROP DATABASE IF EXISTS rollcall_lab;
CREATE DATABASE rollcall_lab;
USE rollcall_lab;

-- Drop if exists (optional for re-run)
DROP TABLE IF EXISTS O_Roll_Call;
DROP TABLE IF EXISTS N_Roll_Call;
DROP PROCEDURE IF EXISTS MergeRollCalls;

-- Create Old Table
CREATE TABLE O_Roll_Call (
    Roll_No INT PRIMARY KEY,
    Name VARCHAR(100)
);

-- Create New Table
CREATE TABLE N_Roll_Call (
    Roll_No INT,
    Name VARCHAR(100)
);

-- Insert sample data in OLD table (1 record)
INSERT INTO O_Roll_Call VALUES (101, 'Dipanshu');

-- Insert sample data in NEW table (duplicates + new)
INSERT INTO N_Roll_Call VALUES (101, 'Dipanshu'); -- duplicate
INSERT INTO N_Roll_Call VALUES (102, 'Aarohi Deshmukh');
INSERT INTO N_Roll_Call VALUES (103, 'Kashish Sharma');
INSERT INTO N_Roll_Call VALUES (104, 'Isha Mehta');
INSERT INTO N_Roll_Call VALUES (105, 'Priya Iyer');
INSERT INTO N_Roll_Call VALUES (106, 'Ananya Nair');
INSERT INTO N_Roll_Call VALUES (107, 'Mitali Joshi');

-- Stored Procedure
DELIMITER $$

CREATE PROCEDURE MergeRollCalls()
BEGIN
    DECLARE v_roll INT;
    DECLARE v_name VARCHAR(100);
    DECLARE v_exists INT;
    DECLARE done INT DEFAULT 0;

    DECLARE cur CURSOR FOR SELECT Roll_No, Name FROM N_Roll_Call;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO v_roll, v_name;

        IF done THEN
            LEAVE read_loop;
        END IF;

        SELECT COUNT(*) INTO v_exists 
        FROM O_Roll_Call WHERE Roll_No = v_roll;

        IF v_exists = 0 THEN
            INSERT INTO O_Roll_Call (Roll_No, Name) VALUES (v_roll, v_name);
            SELECT CONCAT('Inserted: ', v_roll, ' - ', v_name) AS Message;
        ELSE
            SELECT CONCAT('Skipped (Duplicate): ', v_roll) AS Message;
        END IF;
    END LOOP;

    CLOSE cur;
END$$

DELIMITER ;

-- Run the procedure
CALL MergeRollCalls();

-- Check Result
SELECT * FROM O_Roll_Call;
