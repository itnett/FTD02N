python
    import requests

    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("Lyktes å hente data fra API")
    else:
        print("Feil ved henting av data")