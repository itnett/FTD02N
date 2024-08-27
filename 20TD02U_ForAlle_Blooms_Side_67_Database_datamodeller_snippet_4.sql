-- Eksempel på å dele opp en tabell i mindre tabeller for normalisering
-- Start med en denormalisert tabell
CREATE TABLE prosjekter (
    prosjekt_id INT PRIMARY KEY,
    prosjekt_navn VARCHAR(100),
    ansatt_navn VARCHAR(100),
    ansatt_stilling VARCHAR(50)
);

-- Normaliser til 3NF
CREATE TABLE ansatte (
    ansatt_id INT PRIMARY KEY AUTO_INCREMENT,
    navn VARCHAR(100),
    stilling VARCHAR(50)
);

CREATE TABLE prosjekter (
    prosjekt_id INT PRIMARY KEY,
    prosjekt_navn VARCHAR(100),
    ansatt_id INT,
    FOREIGN KEY (ansatt_id) REFERENCES ansatte(ansatt_id)
);