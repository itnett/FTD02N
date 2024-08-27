python
   def secure_open(file_path):
       if os.path.isabs(file_path) and 'safe_directory' in os.path.abspath(file_path):
           with open(file_path, 'r') as file:
               return file.read()
       else:
           raise Exception("Insecure file path")