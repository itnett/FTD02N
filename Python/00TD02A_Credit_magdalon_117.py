python
import logging

logging.basicConfig(filename="sikkerhet.log", level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")
logging.warning("Mistenkelig aktivitet oppdaget!")