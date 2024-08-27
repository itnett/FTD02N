-- Bruk MySQL-sikkerhetsrevisjonsskript for å sjekke konfigurasjonen
SHOW VARIABLES LIKE 'have_ssl';

-- Evaluer styrken på passordpolitikken
SHOW VARIABLES LIKE 'validate_password%';