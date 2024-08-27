python
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Feil: Filen ble ikke funnet."
    except IOError:
        return "Feil: Kan ikke lese filen."

# Test lesing av en eksisterende og en ikke-eksisterende fil
print(read_file("existing_file.txt"))
print(read_file("non_existing_file.txt"))