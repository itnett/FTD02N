-- Opprett en enkel tabell i MySQL
CREATE TABLE ansatte (
    ansatt_id INT PRIMARY KEY,
    navn VARCHAR(50),
    stilling VARCHAR(50),
    lønn DECIMAL(10, 2)
);

-- Sett inn noen eksempeldata
INSERT INTO ansatte (ansatt_id, navn, stilling, lønn) VALUES (1, 'Ola Nordmann', 'Utvikler', 60000.00);