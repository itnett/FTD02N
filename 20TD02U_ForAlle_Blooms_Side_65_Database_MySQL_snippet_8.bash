#!/bin/bash

# MySQL-tilkoblingsdetaljer
MYSQL_USER="root"
MYSQL_PASSWORD="your_password"

# Funksjon for å utføre sikkerhetssjekk
function check_security {
  echo "Sikkerhetssjekk nr. $1: $2"
  mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -e "$3"
}

# Funksjon for å rette sikkerhetssårbarhet
function fix_security {
  read -p "Ønsker du å rette dette problemet? (y/n): " choice
  if [ "$choice" == "y" ]; then
    mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -e "$1"
    echo "Rettet."
  else
    echo "Valgte å ikke rette."
  fi
}

echo "Kjører sikkerhetssjekk på MySQL-serveren..."

# 1. Sjekk for anonyme brukere
check_security 1 "Sjekk for anonyme brukere" "SELECT user, host FROM mysql.user WHERE user='';"
fix_security "DELETE FROM mysql.user WHERE user='';"

# 2. Sjekk for brukere uten passord
check_security 2 "Sjekk for brukere uten passord" "SELECT user, host FROM mysql.user WHERE authentication_string='';"
fix_security "UPDATE mysql.user SET authentication_string=PASSWORD('NewStrongPassword') WHERE authentication_string='';"

# 3. Sjekk om root har tilgang fra alle verter
check_security 3 "Sjekk om root har tilgang fra alle verter" "SELECT user, host FROM mysql.user WHERE user='root' AND host='%';"
fix_security "UPDATE mysql.user SET host='localhost' WHERE user='root' AND host='%';"

# 4. Sjekk om SSL er aktivert
check_security 4 "Sjekk om SSL er aktivert" "SHOW VARIABLES LIKE 'have_ssl';"
fix_security "SET GLOBAL require_secure_transport = ON;"

# 5. Sjekk om serveren har generell logging aktivert
check_security 5 "Sjekk om generell logging er aktivert" "SHOW VARIABLES LIKE 'general_log';"
fix_security "SET GLOBAL general_log = 'ON';"

# 6. Sjekk om serveren har slow query logging aktivert
check_security 6 "Sjekk om slow query logging er aktivert" "SHOW VARIABLES LIKE 'slow_query_log';"
fix_security "SET GLOBAL slow_query_log = 'ON';"

# 7. Sjekk for gamle eller sårbare MySQL-versjoner
check_security 7 "Sjekk for gamle eller sårbare MySQL-versjoner" "SELECT VERSION();"
echo "Oppgrader MySQL hvis det er en gammel versjon."

# 8. Sjekk om innebygde kontoer som 'test' finnes
check_security 8 "Sjekk om 'test'-databasen eller kontoer finnes" "SHOW DATABASES LIKE 'test';"
fix_security "DROP DATABASE IF EXISTS test;"

# 9. Sjekk for tillatelse til å utføre innlasting av filer
check_security 9 "Sjekk for FILE-tillatelse" "SELECT user, host FROM mysql.user WHERE File_priv='Y';"
fix_security "REVOKE FILE ON *.* FROM 'user'@'host';"

# 10. Sjekk for usikre autentiseringsprotokoller
check_security 10 "Sjekk for gammeldags autentiseringsprotokoller" "SHOW VARIABLES LIKE 'old_passwords';"
fix_security "SET GLOBAL old_passwords=0;"

# 11. Sjekk for brukere med SUPER-tillatelse
check_security 11 "Sjekk for brukere med SUPER-tillatelse" "SELECT user, host FROM mysql.user WHERE Super_priv='Y';"
fix_security "REVOKE SUPER ON *.* FROM 'user'@'host';"

# 12. Sjekk for brukere med GRANT OPTION
check_security 12 "Sjekk for brukere med GRANT OPTION" "SELECT user, host FROM mysql.user WHERE Grant_priv='Y';"
fix_security "REVOKE GRANT OPTION ON *.* FROM 'user'@'host';"

# 13. Sjekk om event scheduler er aktivert
check_security 13 "Sjekk om event scheduler er aktivert" "SHOW VARIABLES LIKE 'event_scheduler';"
fix_security "SET GLOBAL event_scheduler=OFF;"

# 14. Sjekk for brukere med USAGE-tillatelse
check_security 14 "Sjekk for brukere med kun USAGE-tillatelse" "SELECT user, host FROM mysql.user WHERE Insert_priv='N' AND Select_priv='N' AND Update_priv='N' AND Delete_priv='N';"
fix_security "DELETE FROM mysql.user WHERE Insert_priv='N' AND Select_priv='N' AND Update_priv='N' AND Delete_priv='N';"

# 15. Sjekk om MySQL kjører med root-rettigheter (system)
check_security 15 "Sjekk om MySQL kjører som root" "SELECT @@hostname, @@user;"
echo "Kjør MySQL som en begrenset bruker hvis den kjører som root."

# 16. Sjekk for databaseversjonslekkasjer
check_security 16 "Sjekk om versjonsinformasjon blir eksponert" "SHOW VARIABLES LIKE 'version_comment';"
fix_security "SET GLOBAL version_comment='';"

# 17. Sjekk for farlige globale variabler
check_security 17 "Sjekk for farlige globale variabler" "SHOW VARIABLES WHERE Value LIKE '%';"
echo "Gjennomgå og endre eventuelle usikre variabler."

# 18. Sjekk for inaktive brukere
check_security 18 "Sjekk for inaktive brukere" "SELECT user, host, last_login FROM mysql.user WHERE last_login IS NULL OR last_login < NOW() - INTERVAL 1 YEAR;"
fix_security "DELETE FROM mysql.user WHERE user = 'inaktiv_bruker';"

# 19. Sjekk om binære loggfiler er beskyttet
check_security 19 "Sjekk om binære loggfiler er beskyttet" "SHOW VARIABLES LIKE 'log_bin_trust_function_creators';"
fix_security "SET GLOBAL log_bin_trust_function_creators=0;"

# 20. Sjekk for gamle eller ubrukte indekser
check_security 20 "Sjekk for gamle eller ubrukte indekser" "SELECT DISTINCT TABLE_NAME, INDEX_NAME FROM information_schema.STATISTICS WHERE CARDINALITY=0;"
echo "Gjennomgå og slett eventuelle ubrukte indekser."

echo "Sikkerhetssjekk fullført."