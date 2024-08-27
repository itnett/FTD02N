python
   from flask import Flask, jsonify, request

   app = Flask(__name__)

   @app.route('/kontoer', methods=['GET'])
   def get_kontoer():
       return jsonify(kontoer)

   @app.route('/transaksjon', methods=['POST'])
   def legg_til_transaksjon():
       data = request.get_json()
       transaksjoner.append(data)
       return jsonify({"status": "Transaksjon lagt til!"})

   if __name__ == '__main__':
       app.run(debug=True)