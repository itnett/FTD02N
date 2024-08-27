python
Imgs = [".png", ".jpg", ".jpeg"]
Images = [file for file in files if os.path.split(file)[1].lower() in Imgs]