python
def newtons_2_lov(m=10, a=9.8):
    """
    Bruker Newtons 2. lov for å beregne kraften på et objekt.
    
    Parametere:
    m (int/float): Masse i kg (standardverdi 10)
    a (int/float): Akselerasjon i m/s^2 (standardverdi 9.8)
    
    Returnerer:
    float: Kraften i Newton
    """
    F = m * a
    return F

# Eksempel på bruk
kraft = newtons_2_lov()
print(f'Kraften er: {kraft} N')