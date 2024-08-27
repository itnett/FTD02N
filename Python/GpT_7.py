python
@app.route('/api/itsikkerhet', methods=['POST'])
def itsikkerhet():
    data = request.json
    problem = data.get('problem')
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Du er en ekspert i IT-sikkerhet. Gi råd om følgende problem: {problem}",
        max_tokens=150
    )
    return jsonify({"råd": response.choices[0].text.strip()})