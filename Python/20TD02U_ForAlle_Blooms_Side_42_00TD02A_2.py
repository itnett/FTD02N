python
import math

# Gitt en rettvinklet trekant med en vinkel på 30 grader og hypotenusens lengde på 10.
vinkel = math.radians(30)
hypotenus = 10

# Beregn lengden av motstående og hosliggende kateter
motstående = hypotenus * math.sin(vinkel)
hosliggende = hypotenus * math.cos(vinkel)
print(f"Motstående: {motstående}, Hosliggende: {hosliggende}")