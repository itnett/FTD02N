python
import logging

logging.basicConfig(filename="applikasjon.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Applikasjonen startet.")
logging.warning("Ugyldig brukernavn eller passord.")
logging.error("Databasefeil.")