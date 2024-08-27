sql
-- Opprett tabeller for kunder, produkter, ordrer og ordrelinjer
CREATE TABLE kunder (
    kunde_id INT PRIMARY KEY AUTO_INCREMENT,
    navn VARCHAR(100),
    epost VARCHAR(100)
);

CREATE TABLE produkter (
    produkt_id INT PRIMARY KEY AUTO_INCREMENT,
    produkt_navn VARCHAR(100),
    pris DECIMAL(10, 2)
);

CREATE TABLE ordrer (
    ordre_id INT PRIMARY KEY AUTO_INCREMENT,
    kunde_id INT,
    ordre_dato DATE,
    FOREIGN KEY (kunde_id) REFERENCES kunder(kunde_id)
);

CREATE TABLE ordrelinjer (
    ordrelinje_id INT PRIMARY KEY AUTO_INCREMENT,
    ordre_id INT,
    produkt_id INT,
    antall INT,
    FOREIGN KEY (ordre_id) REFERENCES ordrer(ordre_id) ON DELETE CASCADE,
    FOREIGN KEY (produkt_id) REFERENCES produkter(produkt_id)
);

-- Sett inn data i tabellene
INSERT INTO kunder (navn, epost) VALUES ('Ola Nordmann', 'ola@example.com');
INSERT INTO produkter (produkt_navn, pris) VALUES ('Laptop', 9999.99);
INSERT INTO ordrer (kunde_id, ordre_dato) VALUES (1, '2024-08-01');
INSERT INTO ordrelinjer (ordre_id, produkt_id, antall) VALUES (1, 1, 1);