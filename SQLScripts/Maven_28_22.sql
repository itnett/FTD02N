sql
     CREATE DATABASE oekonomistyring;

     USE oekonomistyring;

     CREATE TABLE Konto (
         konto_id INT PRIMARY KEY AUTO_INCREMENT,
         navn VARCHAR(255) NOT NULL,
         type ENUM('Eiendel', 'Gjeld', 'Inntekt', 'Kostnad') NOT NULL
     );

     CREATE TABLE Transaksjon (
         transaksjon_id INT PRIMARY KEY AUTO_INCREMENT,
         dato DATE NOT NULL,
         konto_id INT,
         belop DECIMAL(15, 2) NOT NULL,
         type ENUM('Debet', 'Kredit') NOT NULL,
         FOREIGN KEY (konto_id) REFERENCES Konto(konto_id)
     );