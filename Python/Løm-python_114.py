python
timelønn = 220.00
arbeidsgiveravgift_timelønn = 31.02
feriepenger_timelønn = 26.40
arbeidsgiveravgift_feriepenger = 3.72
tjenestepensjon = 4.40
arbeidsgiveravgift_tjenestepensjon = 0.62

variabel_lønnskostnad = (
    timelønn + 
    arbeidsgiveravgift_timelønn + 
    feriepenger_timelønn + 
    arbeidsgiveravgift_feriepenger + 
    tjenestepensjon + 
    arbeidsgiveravgift_tjenestepensjon
)

print(f"Variabel lønnskostnad per arbeidstime: {variabel_lønnskostnad:.2f} kr")