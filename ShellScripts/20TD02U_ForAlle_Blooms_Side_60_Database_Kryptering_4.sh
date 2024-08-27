bash
# Eksempel på nøkkelrotasjonsskript for å oppdatere krypteringsnøkkel i MySQL
ny_nøkkel="ny_hemmelig_nøkkel"
gammel_nøkkel="gammel_hemmelig_nøkkel"

# Dekryptere og kryptere data på nytt med ny nøkkel
mysql -u root -p -e "
UPDATE brukere SET personnummer = AES_ENCRYPT(AES_DECRYPT(personnummer, '$gammel_nøkkel'), '$ny_nøkkel');
"

# Oppdater systemet til å bruke den nye nøkkelen
echo "Nøkkelrotasjon fullført."