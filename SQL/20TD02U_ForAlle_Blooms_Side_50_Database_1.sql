sql
-- Oppretting av en bruker med begrensede rettigheter
CREATE USER 'student'@'localhost' IDENTIFIED BY 'passord123';
GRANT SELECT, INSERT ON skole.* TO 'student'@'localhost';

-- Oppretting av indekser for å forbedre søkeytelsen
CREATE INDEX idx_navn ON elever (navn);
CREATE INDEX idx_klasse_id ON elever (klasse_id);