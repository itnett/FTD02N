python
while True:
    svar = input("Vil du fortsette? (ja/nei): ")
    if svar.lower() == 'nei':
        print("Avslutter programmet...")
        break
    else:
        print("Programmet fortsetter...")