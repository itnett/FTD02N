python
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data['message']
    response = handle_message(user_message)
    return jsonify({"reply": response})

def handle_message(message):
    # Logikk for å håndtere melding og søke i NDLA
    if "matematikk" in message.lower():
        return search_ndla("matematikk")
    elif "norsk" in message.lower():
        return search_ndla("norsk")
    else:
        return "Beklager, jeg forstod ikke spørsmålet ditt. Kan du prøve igjen?"

def search_ndla(query):
    ndla_api_url = f"https://api.ndla.no/search?q={query}"
    response = requests.get(ndla_api_url)
    if response.status_code == 200:
        results = response.json()
        # Eksempel på å returnere de første resultatene
        return results[0]['title'] + ": " + results[0]['url']
    else:
        return "Beklager, jeg klarte ikke å finne informasjon om dette på NDLA."

if __name__ == '__main__':
    app.run(port=5000)