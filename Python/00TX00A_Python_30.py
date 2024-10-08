python
def price_calculation(cost_price=100, markup_percentage=20):
   

 """
    Calculate the selling price based on cost price and markup percentage.

    Parametere:
    cost_price (int/float): Kostpris (standardverdi 100)
    markup_percentage (int/float): Påslagsprosent (standardverdi 20)

    Returnerer:
    float: Utsalgspris
    """
    selling_price = cost_price + (cost_price * (markup_percentage / 100))
    return selling_price

# Eksempel på bruk
price = price_calculation()
print(f'Utsalgspris: {price}')