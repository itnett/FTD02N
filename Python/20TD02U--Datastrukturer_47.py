python
# Bruk av dictionary (hashmap) i Python
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Tilgang til verdier
print(my_dict['name'])  # Output: Alice

# Legge til/oppdatere verdier
my_dict['age'] = 26

# Fjerne verdier
del my_dict['city']

# Iterere gjennom nøkkel-verdi-par
for key, value in my_dict.items():
    print(f"{key}: {value}")