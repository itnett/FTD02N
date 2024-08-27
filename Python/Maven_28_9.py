python
    import json

    data = {
        "department": "IT",
        "budget": 100000
    }

    # Lagre data til fil
    with open('budget.json', 'w') as f:
        json.dump(data, f)

    # Lese data fra fil
    with open('budget.json', 'r') as f:
        loaded_data = json.load(f)
        print(loaded_data)