-- Lage en database
        CREATE DATABASE min_database;

        -- Bruke databasen
        USE min_database;

        -- Lage en tabell
        CREATE TABLE kunder (
            id INT PRIMARY KEY AUTO_INCREMENT,
            navn VARCHAR(255),
            epost VARCHAR(255)
        );

        -- Legge til data
        INSERT INTO kunder (navn, epost) VALUES ('Ola Nordmann', 'ola@nordmann.no');

        -- Hente data
        SELECT * FROM kunder;