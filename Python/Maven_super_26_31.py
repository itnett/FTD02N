python
with open("eksempel.txt", "r") as fil:
    for linje i fil:
        print(linje.strip())  # .strip() fjerner eventuelle ekstra mellomrom og linjeskift