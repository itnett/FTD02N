python
API_KEY = "minhemmeligeapi-nøkkel"

@app.before_request
def sjekk_api_nøkkel():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        return jsonify({"error": "Ugyldig API-nøkkel"}), 401