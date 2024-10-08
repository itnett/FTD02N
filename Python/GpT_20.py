python
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Sett opp OpenAI API-nøkkel
openai.api_key = 'din_api_nokkel'

# Funksjon for å generere svar
def generer_svar(sporsmal):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Du er en ekspert i økonomistyring, organisasjon, ledelse og markedsføringsledelse. Svar på følgende spørsmål: {sporsmal}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

# API-endepunkt for å motta spørsmål
@app.route('/api/svar', methods=['POST'])
def svar():
    data = request.json
    sporsmal = data.get('sporsmal')
    svar = generer_svar(sporsmal)
    return jsonify({"svar": svar})

if __name__ == '__main__':
    app.run(debug=True)