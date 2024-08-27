python
try:
    with open('eksempel.txt', 'r') as fil:
        innhold = fil.read()
        print(innhold)
except FileNotFoundError:
    print('Filen ble ikke funnet!')
except IOError:
    print('En IO-feil oppstod!')