python
# Bruk `sjekk_partall` funksjonen til å skrive ut alle partall fra 1 til 10
for i in range(1, 11):
    if sjekk_partall(i):
        print(f"{i} er et partall")