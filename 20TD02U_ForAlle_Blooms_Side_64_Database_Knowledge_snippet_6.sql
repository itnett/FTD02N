-- Sikkerhetsgjennomgang: Bruk av views for å begrense dataeksponering
CREATE VIEW offentlig_ansatt_info AS
SELECT navn, stilling FROM ansatte;