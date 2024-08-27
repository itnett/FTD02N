python
def createIfNot(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)