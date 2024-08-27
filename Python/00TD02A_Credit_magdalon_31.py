python
import random

def simuler_responstid(gjennomsnitt, standardavvik):
    responstid = random.gauss(gjennomsnitt, standardavvik)
    return max(0, responstid)  # Sørg for at responstiden ikke er negativ

gjennomsnittlig_responstid = 50  # Millisekunder
standardavvik_responstid = 10

responstider = [simuler_responstid(gjennomsnittlig_responstid, standardavvik_responstid) for _ in range(1000)]