sql
-- Aktivere logging av påloggingsforsøk i MySQL
SET GLOBAL log_warnings = 2;
SHOW VARIABLES LIKE 'log_warnings';

-- Eksempel på logging i applikasjonen
-- Python
import logging

# Sett opp logging
logging.basicConfig(filename='security.log', level=logging.INFO)

# Logge et påloggingsforsøk
def logg_inn_bruker(brukernavn, passord):
    # Eksempel autentisering
    if autentiser_bruker(brukernavn, passord):
        logging.info(f'Påloggingsforsøk vellykket for bruker: {brukernavn}')
    else:
        logging.warning(f'Feilet påloggingsforsøk for bruker: {brukernavn}')