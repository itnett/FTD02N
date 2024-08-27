python
import requests

CANVAS_API_URL = 'https://canvas.instructure.com/api/v1/'
CANVAS_API_KEY = 'din_canvas_api_nokkel'

def hent_oppgaver(kurs_id):
    headers = {
        'Authorization': f'Bearer {CANVAS_API_KEY}'
    }
    response = requests.get(f'{CANVAS_API_URL}/courses/{kurs_id}/assignments', headers=headers)
    return response.json()

@app.route('/api/oppgaver', methods=['GET'])
def oppgaver():
    kurs_id = request.args.get('kurs_id')
    oppgaver = hent_oppgaver(kurs_id)
    return jsonify(oppgaver)