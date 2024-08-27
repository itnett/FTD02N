-- Eksempel på en fullstendig datamodell for en e-handelsplattform
CREATE TABLE kategorier (
    kategori_id INT PRIMARY KEY AUTO_INCREMENT,
    kategori_navn VARCHAR(100)
);

CREATE TABLE produkter (
    produkt_id INT PRIMARY KEY AUTO_INCREMENT,
    produkt_navn VARCHAR(100),
    pris DECIMAL(10, 2),
    lager INT,
    kategori_id INT,
    FOREIGN KEY (kategori_id) REFERENCES kategorier(kategori_id)
);

CREATE TABLE kunder (
    kunde_id INT PRIMARY KEY AUTO_INCREMENT,
    navn VARCHAR(100),
    epost VARCHAR(100),
    adresse VARCHAR(255)
);

CREATE TABLE ordrer (
    ordre_id INT PRIMARY KEY AUTO_INCREMENT,
    kunde_id INT,
    ordre_dato DATE,
    totalbelop DECIMAL(10, 2),
    FOREIGN KEY (kunde_id) REFERENCES kunder(kunde_id)
);

CREATE TABLE ordrelinjer (
    ordrelinje_id INT PRIMARY KEY AUTO_INCREMENT,
    ordre_id INT,
    produkt_id INT,
    antall INT,
    pris_pr_enhet DECIMAL(10, 2),
    FOREIGN KEY (ordre_id) REFERENCES ordrer(ordre_id) ON DELETE CASCADE,
    FOREIGN KEY (produkt_id) REFERENCES produkter(produkt_id)
);

-- Indekser for ytelsesforbedring
CREATE INDEX idx_produkter_kategori ON produkter(kategori_id);
CREATE INDEX idx_ordrer_kunde ON ordrer(kunde_id);