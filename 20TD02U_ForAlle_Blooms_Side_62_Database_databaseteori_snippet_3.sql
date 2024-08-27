-- Eksempel på normalisering fra 1NF til 2NF
-- Start med en enkel tabell
CREATE TABLE ordre (
    ordre_id INT,
    kunde_navn VARCHAR(50),
    produkt_navn VARCHAR(50),
    antall INT,
    PRIMARY KEY (ordre_id)
);

-- Normaliser til 2NF ved å dele tabellen i to
CREATE TABLE kunde (
    kunde_id INT PRIMARY KEY,
    kunde_navn VARCHAR(50)
);

CREATE TABLE produkt (
    produkt_id INT PRIMARY KEY,
    produkt_navn VARCHAR(50)
);

CREATE TABLE ordre_ny (
    ordre_id INT PRIMARY KEY,
    kunde_id INT,
    produkt_id INT,
    antall INT,
    FOREIGN KEY (kunde_id) REFERENCES kunde(kunde_id),
    FOREIGN KEY (produkt_id) REFERENCES produkt(produkt_id)
);