sql
-- Create a new database
CREATE DATABASE School;

-- Use the created database
USE School;

-- Create a table for students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BirthDate DATE
);

-- Insert data into the Students table
INSERT INTO Students (StudentID, FirstName, LastName, BirthDate)
VALUES (1, 'John', 'Doe', '2000-01-01'),
       (2, 'Jane', 'Smith', '1999-05-12');

-- Select data from the Students table
SELECT * FROM Students;