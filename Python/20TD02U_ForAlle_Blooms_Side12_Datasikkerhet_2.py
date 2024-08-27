python
roller = {
    "admin": ["lese", "skrive", "slette"],
    "bruker": ["lese"],
}

bruker_roller = {
    "alice": "admin",
    "bob": "bruker",
}

def har_tillatelse(bruker, tillatelse):
    rolle = bruker_roller.get(bruker)
    if rolle:
        return tillatelse in roller[rolle]
    return False

print(har_tillatelse("alice", "slette"))  # True
print(har_tillatelse("bob", "slette"))    # False