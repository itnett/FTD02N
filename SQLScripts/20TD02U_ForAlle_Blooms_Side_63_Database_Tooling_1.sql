sql
-- Opprett to tabeller som følger relasjonsmodellen og er normalisert
CREATE TABLE ordre (
    ordre_id INT PRIMARY KEY,
    kunde_id INT,
    dato DATE,
    FOREIGN KEY (kunde_id) REFERENCES kunder(kunde_id)
);

CREATE TABLE ordrelinjer (
    ordrelinje_id INT PRIMARY KEY,
    ordre_id INT,
    produkt VARCHAR(100),
    antall INT,
    FOREIGN KEY (ordre_id) REFERENCES ordre(ordre_id)
);