python
def beregn_nåverdi(kontantstrømmer, diskonteringsrente):
    nåverdi = 0
    for år, kontantstrøm in enumerate(kontantstrømmer, start=1):
        nåverdi += kontantstrøm / (1 + diskonteringsrente) ** år
    return nåverdi

kontantstrømmer = [10000, 12000, 15000]
diskonteringsrente = 0.08  # 8%
nåverdi = beregn_nåverdi(kontantstrømmer, diskonteringsrente)
print(f"Nåverdi av kontantstrømmene: {nåverdi:.2f}")