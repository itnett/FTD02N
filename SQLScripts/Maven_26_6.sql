sql
CREATE DATABASE Okonomistyring;

USE Okonomistyring;

CREATE TABLE Accounts (
    AccountID INT PRIMARY KEY,
    AccountName VARCHAR(100),
    AccountType VARCHAR(50)
);

CREATE TABLE Budget (
    BudgetID INT PRIMARY KEY,
    Year INT,
    AccountID INT,
    BudgetAmount DECIMAL(15, 2),
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);

CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY,
    AccountID INT,
    TransactionDate DATE,
    Amount DECIMAL(15, 2),
    Description VARCHAR(255),
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);

CREATE TABLE Investments (
    InvestmentID INT PRIMARY KEY,
    InvestmentName VARCHAR(100),
    InvestmentDate DATE,
    InitialAmount DECIMAL(15, 2),
    ExpectedReturn DECIMAL(5, 2)
);