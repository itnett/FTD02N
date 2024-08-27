python
import math

avstand_km = 1000  # Avstand mellom to noder i kilometer
lys_hastighet_km_s = 299792.458  # Lyshastigheten i kilometer per sekund

forsinkelse_sekunder = 2 * avstand_km / lys_hastighet_km_s
forsinkelse_ms = forsinkelse_sekunder * 1000  # Konverter til millisekunder

print(f"Estimert rundtur-forsinkelse: {forsinkelse_ms:.2f} ms")