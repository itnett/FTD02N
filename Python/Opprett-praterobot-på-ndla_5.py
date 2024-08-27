python
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'din-api-nokkel'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data.get('message', '')
    response = get_openai_response(user_message)
    return jsonify({"reply": response})

def get_openai_response(message):
    system_prompt = ("Du er en ekspert i IT-drift og sikkerhet. Gi råd om IT-infrastruktur, "
                     "nettverk, cybersikkerhet, og serverdrift. Tilby løsninger for feilsøking og gi kursmateriell "
                     "og veiledning for IT-sertifiseringer som CCNA og ITIL.")
    prompt = f"{system_prompt}\n\nBrukermelding: {message}"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150,
        temperature=0.5
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(port=5000)