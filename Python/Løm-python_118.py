python
# Beregning av netto nåverdi (NPV)
anskaffelseskost = 3000000
installasjon_opplæring = 200000
levetid = 4
restverdi = 300000
innbetalingsoverskudd_per_år = 1000000
avkastningskrav = 0.10

# Beregne NPV
investeringer = anskaffelseskost + installasjon_opplæring
kontantstrømmer = [innbetalingsoverskudd_per_år] * levetid
kontantstrømmer[-1] += restverdi  # Legge til restverdi i siste år

npv = -investeringer
for t, kontantstrøm in enumerate(kontantstrømmer):
    npv += kontantstrøm / ((1 + avkastningskrav) ** (t + 1))

print(f"Netto nåverdi (NPV): {npv:.2f} kr")