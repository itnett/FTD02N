python
fil = None
try:
    fil = open('eksempel.txt', 'r')
    innhold = fil.read()
except Exception as e:
    print(f"En feil oppstod: {e}")
finally:
    if fil:
        fil.close()