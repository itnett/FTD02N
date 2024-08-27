python
# Deklarasjon og initialisering av en liste (array)
my_list = [1, 2, 3, 4, 5]

# Tilgang til elementer
print(my_list[0])  # Output: 1

# Legge til elementer
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Fjerne elementer
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5, 6]

# Iterere gjennom listen
for item in my_list:
    print(item)