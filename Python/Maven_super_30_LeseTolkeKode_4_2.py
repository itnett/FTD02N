python
def move(folderName, files):
    for file in files:
        os.replace(file,folderName)