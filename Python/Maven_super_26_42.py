python
with open('data.txt', 'r') as fil:
    for linje in fil:
        print(linje.strip())