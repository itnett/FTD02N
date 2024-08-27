python
    import logging

    logging.basicConfig(filename='app.log', level=logging.INFO)

    logging.info('Application startet')
    logging.warning('Dette er en advarsel')
    logging.error('Dette er en feilmelding')