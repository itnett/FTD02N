python
def beregn_npv(kontantstrømmer, diskonteringsrente):
    npv = -kontantstrømmer[0]  # Start med den initiale investeringen som en negativ kontantstrøm
    for år, kontantstrøm in enumerate(kontantstrømmer[1:], start=1):
        npv += kontantstrøm / (1 + diskonteringsrente) ** år
    return npv

kontantstrømmer = [-50000, 15000, 20000, 25000, 30000]
diskonteringsrente = 0.1
npv = beregn_npv(kontantstrømmer, diskonteringsrente)
print(f"Nåverdi (NPV): {npv:.2f}")