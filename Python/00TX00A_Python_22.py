python
import pandas as pd

def resultatbudsjett(inntekter=100000, varekostnad=40000, lønn=30000, andre_kostnader=10000):
    """
    Lager et enkelt resultatbudsjett.
    
    Parametere:
    inntekter (int/float): Forventede inntekter (standardverdi 100000)
    varekostnad (int/float): Kostnader for varer (standardverdi 40000)
    lønn (int/float): Lønnskostnader (standardverdi 30000)
    andre_kostnader (int/float): Andre kostnader (standardverdi 10000)
    
    Returnerer:
    DataFrame: Resultatbudsjettet
    """
    kostnader = varekostnad + lønn + andre_kostnader
    resultat = inntekter - kostnader
    data = {
        'Inntekter': [inntekter],
        'Varekostnad': [varekostnad],
        'Lønn': [lønn],
        'Andre kostnader': [andre_kostnader],
        'Totale kostnader': [kostnader],
        'Resultat': [resultat]
    }
    df = pd.DataFrame(data)
    return df

# Eksempel på bruk
budsjett = resultatbudsjett()
print(budsjett)