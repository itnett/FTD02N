sql
-- Eksempel på et komplekst databaseskjema for et e-handelssystem
CREATE TABLE produkter (
    produkt_id INT PRIMARY KEY,
    navn VARCHAR(100),
    pris DECIMAL(10, 2)
);

CREATE TABLE betalinger (
    betaling_id INT PRIMARY KEY,
    ordre_id INT,
    beløp DECIMAL(10, 2),
    dato DATE,
    FOREIGN KEY (ordre_id) REFERENCES ordre(ordre_id)
);