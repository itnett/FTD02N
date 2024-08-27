sql
     CREATE TABLE Products (
         ProductID INT PRIMARY KEY,
         ProductName NVARCHAR(100),
         SupplierID INT
     );

     CREATE TABLE OrderDetails (
         OrderDetailID INT PRIMARY KEY,
         OrderID INT,
         ProductID INT,
         Quantity INT,
         FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
         FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
     );