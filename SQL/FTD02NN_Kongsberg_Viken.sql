sql
  CREATE DATABASE CustomerDB;

  USE CustomerDB;

  CREATE TABLE Customers (
      CustomerID INT PRIMARY KEY,
      Name VARCHAR(100),
      Email VARCHAR(100),
      Phone VARCHAR(15)
  );

  INSERT INTO Customers (CustomerID, Name, Email, Phone) VALUES (1, 'John Doe', 'john@example.com', '555-1234');
  INSERT INTO Customers (CustomerID, Name, Email, Phone) VALUES (2, 'Jane Smith', 'jane@example.com', '555-5678');

  SELECT * FROM Customers;

  UPDATE Customers SET Email = 'johndoe@example.com' WHERE CustomerID = 1;

  DELETE FROM Customers WHERE CustomerID = 2;