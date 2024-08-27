python
# Åpne en fil for lesing
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Åpne en fil for skriving
with open('example.txt', 'w') as file:
    file.write('Dette er en test.')