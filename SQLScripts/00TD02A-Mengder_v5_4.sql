sql
INSERT INTO Person (PersonID, Navn, Alder, Kjønn, Vekt) VALUES
(1, 'Trine', 13, 'Kvinne', 50),
(2, 'Truls', 16, 'Mann', 70),
(3, 'Kari', 40, 'Kvinne', 60),
(4, 'Tormod', 46, 'Mann', 80);

INSERT INTO Koffert (KoffertID, Type, Vekt, PersonID) VALUES
(1, 'stor', 25, 1),
(2, 'stor', 25, 2),
(3, 'stor', 25, 3),
(4, 'stor', 25, 4),
(5, 'kabin', 10, 1),
(6, 'kabin', 10, 2),
(7, 'kabin', 10, 3),
(8, 'kabin', 10, 4);

INSERT INTO Alkohol (AlkoholID, Type, Mengde, PersonID) VALUES
(1, 'øl', 0, 1),
(2, 'vin', 0, 2),
(3, 'cider', 0, 3),
(4, 'øl', 1, 4);

INSERT INTO Faktor (FaktorID, Type, Verdi, PersonID) VALUES
(1, 'tid', '2 timer siden', 1),
(2, 'tid', '1 time siden', 2),
(3, 'mat', 'pizza', 3),
(4, 'metabolisme', 'normal', 4);