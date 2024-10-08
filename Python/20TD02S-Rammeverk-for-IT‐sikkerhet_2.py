python
import logging

# Konfigurer logging
logging.basicConfig(filename='sikkerhetshendelser.log', level=logging.INFO)

def logg_hendelse(hendelse, alvorlighet):
    logging.info(f"Hendelse: {hendelse}, Alvorlighet: {alvorlighet}")

# Eksempel på logging av en hendelse
logg_hendelse("Uautorisert tilgang oppdaget", "Høy")