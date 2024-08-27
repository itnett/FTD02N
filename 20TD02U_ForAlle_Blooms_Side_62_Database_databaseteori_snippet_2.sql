-- Opprett en tabell for kurs
CREATE TABLE kurs (
    kurs_id INT PRIMARY KEY,
    kurs_navn VARCHAR(50)
);

-- Legg til en fremmednøkkel i student-tabellen for å koble til kurs-tabellen
ALTER TABLE studenter
ADD kurs_id INT,
ADD CONSTRAINT fk_kurs FOREIGN KEY (kurs_id) REFERENCES kurs(kurs_id);