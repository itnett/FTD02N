python
# Eksempel på datastruktur-manipulasjon
def main():
    liste = [1, 2, 3, 4, 5]
    sett = {1, 2, 3, 4, 5}
    ordbok = {"en": 1, "to": 2, "tre": 3}

    for nummer in liste:
        if nummer % 2 == 0:
            print(f"{nummer} er partall")

if __name__ == "__main__":
    main()