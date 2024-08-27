CREATE TABLE Customers (
         CustomerID INT PRIMARY KEY,
         CustomerName NVARCHAR(100),
         ContactName NVARCHAR(100),
         Country NVARCHAR(50)
     );

     CREATE TABLE Orders (
         OrderID INT PRIMARY KEY,
         OrderDate DATE,
         CustomerID INT,
         FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
     );