CREATE DATABASE frienddb;

USE frienddb;

CREATE TABLE friends (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    nickname VARCHAR(50),
    phone VARCHAR(15),
    city VARCHAR(50)
);
