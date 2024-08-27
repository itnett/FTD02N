python
answers = """1) Løsningen innebærer bruk av Black-Scholes-modellen for å beregne egenkapital som en kjøpsopsjon og gjeld som en salgsopsjon. Konflikter oppstår på grunn av ulike risikopreferanser og kan dempes ved bruk av gjeldskontrakter med restriktive avtaler. Aksjeselskap gir begrenset ansvar og skattefordeler, men partnerskap gir fleksibilitet. Børsnoterte selskaper har tilgang til mer kapital, men kan være mer utsatt for markedsvolatilitet. Selskapsformene i Norge inkluderer aksjeselskap (AS) og ansvarlig selskap (ANS).
2) a
3) b
4) a
5) b
6) b
7) b
8) b
9) c
10) c"""
file_path = '/mnt/data/answers_1.txt'
with open(file_path, 'w') as file:
    file.write(answers)
file_path