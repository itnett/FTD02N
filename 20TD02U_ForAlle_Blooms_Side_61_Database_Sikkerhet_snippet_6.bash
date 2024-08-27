# Skript for å sjekke om alle sensitive data er kryptert i MySQL
mysql -u root -p -e "
SELECT TABLE_NAME, COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'skole' AND DATA_TYPE = 'varbinary';
"

# Verifiser at resultatet samsvarer med forventet krypteringsstrategi