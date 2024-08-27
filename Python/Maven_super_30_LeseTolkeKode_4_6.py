python
Auds = [".mp3", ".m4a", ".wav", ".flv"]
Audios = [file for file in files if os.path.split(file)[1].lower() in Auds]