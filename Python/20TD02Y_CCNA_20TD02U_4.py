python
def del_tall(a, b):
    try:
        if b == 0:
            raise ValueError("Kan ikke dele med null")
        return a / b
    except ValueError as e:
        return str(e)

# Test sikkerhetsmekanismer
print(del_tall(10, 0))