sql
     INSERT INTO Konto (navn, type) VALUES ('Bankkonto', 'Eiendel');
     INSERT INTO Konto (navn, type) VALUES ('Salg', 'Inntekt');

     INSERT INTO Transaksjon (dato, konto_id, belop, type)
     VALUES ('2024-09-01', 1, 10000.00, 'Debet');

     INSERT INTO Transaksjon (dato, konto_id, belop, type)
     VALUES ('2024-09-01', 2, 10000.00, 'Kredit');