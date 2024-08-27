python
for i in range(10):
    if i == 5:
        break  # Stopp løkken når i er 5
    if i % 2 == 0:
        continue  # Hopp over utskrift for partall
    print(i)