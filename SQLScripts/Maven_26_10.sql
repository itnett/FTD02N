sql
CREATE DATABASE Organisasjonsstyring;

USE Organisasjonsstyring;

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100),
    ManagerID INT
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT,
    Position VARCHAR(50),
    Salary DECIMAL(10, 2),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Trainings (
    TrainingID INT PRIMARY KEY,
    TrainingName VARCHAR(100),
    EmployeeID INT,
    TrainingDate DATE,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

CREATE TABLE WorkEnvironment (
    ReviewID INT PRIMARY KEY,
    DepartmentID INT,
    ReviewDate DATE,
    Rating INT,  -- 1-5 rating
    Comments TEXT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);