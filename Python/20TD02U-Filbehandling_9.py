python
   from flask import Flask, request, render_template

   app = Flask(__name__)

   @app.route('/upload', methods=['POST'])
   def upload_file():
       if 'file' not in request.files:
           return 'No file part'
       file = request.files['file']
       if file.filename == '':
           return 'No selected file'
       file.save(f'./uploads/{file.filename}')
       return 'File uploaded successfully'

   if __name__ == '__main__':
       app.run(debug=True)