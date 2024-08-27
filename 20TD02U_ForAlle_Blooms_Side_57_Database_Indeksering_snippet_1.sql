-- Opprette en enkel tabell
CREATE TABLE elever (
    id INT PRIMARY KEY,
    navn VARCHAR(50),
    alder INT
);

-- Opprette en indeks på 'navn' kolonnen for raskere søk
CREATE INDEX idx_navn ON elever (navn);