python
API_KEY = "hemmeligAPI-nøkkel"

def sjekk_api_nøkkel(request):
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        raise PermissionError("Ugyldig API-nøkkel")

# Bruk i API-kall
try:
    sjekk_api_nøkkel(request)
    # Fortsett med behandlingen av forespørselen
except PermissionError as e:
    print(e)
    # Returner en feilmelding til klienten