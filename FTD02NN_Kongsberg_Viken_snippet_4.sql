-- Opprette tabell
CREATE TABLE Produkter (
    ProduktID INT PRIMARY KEY,
    Navn VARCHAR(100),
    Pris DECIMAL(10, 2)
);

-- Legge inn data
INSERT INTO Produkter (ProduktID, Navn, Pris)
VALUES (1, 'Laptop', 9999.99);

-- Hente data
SELECT * FROM Produkter;