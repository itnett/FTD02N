sql
-- Oppretting av databasen
CREATE DATABASE skole;
USE skole;

-- Oppretting av tabellen Student
CREATE TABLE Student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    navn VARCHAR(100) NOT NULL,
    fødselsdato DATE NOT NULL
);

-- Oppretting av tabellen Kurs
CREATE TABLE Kurs (
    kurs_id INT AUTO_INCREMENT PRIMARY KEY,
    kursnavn VARCHAR(100) NOT NULL
);

-- Oppretting av tabellen Påmelding
CREATE TABLE Påmelding (
    påmelding_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    kurs_id INT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (kurs_id) REFERENCES Kurs(kurs_id)
);