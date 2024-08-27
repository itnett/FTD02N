-- Eksempel på grunnleggende SQL-kommandor
CREATE TABLE ansatte (
    ansatt_id INT PRIMARY KEY,
    navn VARCHAR(50),
    stilling VARCHAR(50),
    lønn DECIMAL(10, 2)
);

INSERT INTO ansatte (ansatt_id, navn, stilling, lønn) VALUES (1, 'Ola Nordmann', 'Utvikler', 60000.00);

SELECT * FROM ansatte;