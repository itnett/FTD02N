python
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Sett din OpenAI API-nøkkel her
openai.api_key = 'din-api-nøkkel'

# Ledetekst basert på målgruppen
lead_in_text = "Skriv som om du er en lærerhjelper for lærere på videregående skole. Vær didaktisk, hjelpsom og kreativ."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data.get('message', '')
    response = get_openai_response(user_message)
    return jsonify({"reply": response})

def get_openai_response(message):
    # Send forespørsel til OpenAI API
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=lead_in_text + "\n\n" + message,
        max_tokens=150,
        temperature=0.5
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(port=5000)