python
def legg_til(a, b):
    return a + b

def trekk_fra(a, b):
    return a - b

def multipliser(a, b):
    return a * b

def del_tall(a, b):
    if b != 0:
        return a / b
    else:
        return "Kan ikke dele med null"

# Testing av funksjonene
print(legg_til(10, 5))
print(trekk_fra(10, 5))
print(multipliser(10, 5))
print(del_tall(10, 5))