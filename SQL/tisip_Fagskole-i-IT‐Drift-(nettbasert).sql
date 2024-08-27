sql
-- Hente alle studenter
SELECT * FROM Student;

-- Hente alle kurs
SELECT * FROM Kurs;

-- Hente alle påmeldinger
SELECT * FROM Påmelding;

-- Hente alle studenter som er påmeldt et kurs
SELECT Student.navn, Kurs.kursnavn
FROM Påmelding
JOIN Student ON Påmelding.student_id = Student.student_id
JOIN Kurs ON Påmelding.kurs_id = Kurs.kurs_id;