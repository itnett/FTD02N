-- Opprett tabeller for fag og påmeldinger
CREATE TABLE fag (
    fag_id INT PRIMARY KEY,
    fag_navn VARCHAR(100)
);

CREATE TABLE påmeldinger (
    elev_id INT,
    fag_id INT,
    PRIMARY KEY (elev_id, fag_id),
    FOREIGN KEY (elev_id) REFERENCES elever(elev_id),
    FOREIGN KEY (fag_id) REFERENCES fag(fag_id)
);

-- Sett inn data i tabellene
INSERT INTO fag (fag_id, fag_navn) VALUES (1, 'Matematikk');
INSERT INTO påmeldinger (elev_id, fag_id) VALUES (1, 1);