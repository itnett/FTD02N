sql
     CREATE DATABASE ITDrift;
     USE ITDrift;

     CREATE TABLE Employees (
         EmployeeID INT PRIMARY KEY,
         FirstName VARCHAR(50),
         LastName VARCHAR(50),
         Department VARCHAR(50)
     );

     CREATE TABLE Projects (
         ProjectID INT PRIMARY KEY,
         ProjectName VARCHAR(100),
         StartDate DATE,
         EndDate DATE
     );