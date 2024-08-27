sql
-- Legge til studenter
INSERT INTO Student (navn, fødselsdato) VALUES ('Ola Nordmann', '2000-01-01');
INSERT INTO Student (navn, fødselsdato) VALUES ('Kari Nordmann', '1999-05-23');

-- Legge til kurs
INSERT INTO Kurs (kursnavn) VALUES ('Matematikk');
INSERT INTO Kurs (kursnavn) VALUES ('Norsk');

-- Legge til påmeldinger
INSERT INTO Påmelding (student_id, kurs_id) VALUES (1, 1); -- Ola Nordmann melder seg på Matematikk
INSERT INTO Påmelding (student_id, kurs_id) VALUES (1, 2); -- Ola Nordmann melder seg på Norsk
INSERT INTO Påmelding (student_id, kurs_id) VALUES (2, 1); -- Kari Nordmann melder seg på Matematikk