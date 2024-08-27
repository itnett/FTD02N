python
def beregn_fremtidig_verdi(nåverdi, inflasjon, antall_år):
    fremtidig_verdi = nåverdi * (1 + inflasjon) ** antall_år
    return fremtidig_verdi

nåverdi = 100000
inflasjon = 0.025  # 2.5%
antall_år = 5
fremtidig_verdi = beregn_fremtidig_verdi(nåverdi, inflasjon, antall_år)
print(f"Fremtidig verdi om {antall_år} år: {fremtidig_verdi:.2f}")