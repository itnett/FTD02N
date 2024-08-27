sql
CREATE DATABASE Markedsforingsstyring;

USE Markedsforingsstyring;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    ContactName VARCHAR(100),
    Country VARCHAR(50)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    ProductCategory VARCHAR(50),
    Price DECIMAL(10, 2)
);

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    CustomerID INT,
    SaleDate DATE,
    Quantity INT,
    TotalPrice DECIMAL(15, 2),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE MarketingCampaigns (
    CampaignID INT PRIMARY KEY,
    CampaignName VARCHAR(100),
    StartDate DATE,
    EndDate DATE,
    Budget DECIMAL(15, 2)
);