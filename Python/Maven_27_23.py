python
    with open("example.txt", "w") as file:
        file.write("Dette er en testfil.")
    
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)