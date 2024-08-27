python
Dcs = [".pdf", ".doc", ".docx", ".txt"]
Docs = [file for file in files if os.path.split(file)[1].lower() in Dcs]