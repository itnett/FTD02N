python
# Skrive til en fil
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# Lese

 fra en fil
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)