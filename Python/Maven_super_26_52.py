python
fil = Path('eksempel.txt')

if fil.exists():
    print(f"Filens størrelse: {fil.stat().st_size} bytes")
    if fil.is_file():
        print("Dette er en fil.")
    elif fil.is_dir():
        print("Dette er en katalog.")