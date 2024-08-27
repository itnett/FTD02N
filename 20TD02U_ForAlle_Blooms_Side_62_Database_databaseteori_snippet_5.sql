-- Opprett tabeller for et bibliotekssystem
CREATE TABLE bøker (
    bok_id INT PRIMARY KEY,
    tittel VARCHAR(100),
    forfatter_id INT,
    FOREIGN KEY (forfatter_id) REFERENCES forfattere(forfatter_id)
);

CREATE TABLE forfattere (
    forfatter_id INT PRIMARY KEY,
    navn VARCHAR(50)
);

CREATE TABLE lån (
    lån_id INT PRIMARY KEY,
    bok_id INT,
    låntaker_id INT,
    lån_dato DATE,
    retur_dato DATE,
    FOREIGN KEY (bok_id) REFERENCES bøker(bok_id),
    FOREIGN KEY (låntaker_id) REFERENCES låntakere(låntaker_id)
);

CREATE TABLE låntakere (
    låntaker_id INT PRIMARY KEY,
    navn VARCHAR(50),
    adresse VARCHAR(100)
);