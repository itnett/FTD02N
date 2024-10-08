python
def install_package(package_name):
    """Installerer en pakke og håndterer ulike feil."""
    try:
        subprocess.run(['sudo', 'apt-get', 'install', '-y', package_name], check=True)
        logger.info(f"Pakken {package_name} ble installert.")
    except subprocess.CalledProcessError as e:
        if e.returncode == 100:  # Pakken finnes ikke
            logger.error(f"Pakken {package_name} ble ikke funnet.")
        else:
            logger.error(f"Feil ved installasjon av pakke: {e}")
    except PermissionError:
        logger.error("Du har ikke tillatelse til å installere pakker. Kjør skriptet med sudo.")