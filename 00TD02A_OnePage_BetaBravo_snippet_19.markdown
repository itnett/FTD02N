# Integrasjon av Polynomfunksjoner

### Hva er integrasjon?
- Integrasjon er en metode innenfor matematisk analyse som brukes til å beregne arealer under kurver, finne volum av roterte objekter, og mye mer. Det motsatte av derivasjon, kalles også "antiderivasjon".

### Hvorfor er integrasjon viktig?
- **Areal under kurver**: Integrasjon kan brukes til å beregne arealet under en funksjons graf. Dette er nyttig i mange praktiske anvendelser, som å finne avstand basert på hastighet over tid, eller å beregne akkumulert mengde av en variabel over tid.
- **Bestemme funksjoner fra deres derivater**: Hvis du kjenner den deriverte av en funksjon, kan du bruke integrasjon til å finne tilbake til den opprinnelige funksjonen.
- **Anvendelser**: Integrasjon er et kraftig verktøy som brukes i mange fagfelt, inkludert fysikk, økonomi og ingeniørfag. For eksempel kan det brukes til å modellere bevegelse, optimalisere produksjon og kostnader, og designe effektive konstruksjoner.

### Integrasjonsregler:
- Det finnes flere regler for å integrere ulike typer funksjoner. Her er noen grunnleggende regler for polynomfunksjoner:
  - **Konstantregel**: Integrasjonen av en konstant (et tall uten variabel) er konstanten multiplisert med variabelen.
    - Eksempel: \( \int 5 \, dx = 5x + C \)
  - **Potensregel**: Integrasjonen av \( x^n \) er \( \frac{x^{n+1}}{n+1} \) (for \( n \neq -1 \)).
    - Eksempel: \( \int x^3 \, dx = \frac{x^4}{4} + C \)
  - **Sumregel og differansregel**: Integrasjonen av en sum eller differanse av funksjoner er lik summen eller differansen av integrasjonene.
    - Eksempel: \( \int (x^2 + 3x) \, dx = \frac{x^3}{3} + \frac{3x^2}{2} + C \)

### Anvendelser av integrasjon (polynomfunksjoner):
- **Finne areal**: For å finne arealet under en polynomfunksjons graf mellom to punkter, integrerer du funksjonen og evaluerer integralet ved de to punktene. Differansen mellom disse verdiene gir arealet.
- **Bestemme opprinnelig funksjon**: For å finne en funksjon gitt dens deriverte, integrerer du den deriverte funksjonen.

### Eksempel:
- Finn arealet under funksjonen \( f(x) = x^2 \) fra \( x = 1 \) til \( x = 3 \).
  1. Integrer funksjonen: \( \int x^2 \, dx = \frac{x^3}{3} + C \)
  2. Evaluer integralet ved de to punktene:
     \[ \left[ \frac{x^3}{3} \right]_1^3 = \frac{3^3}{3} - \frac{1^3}{3} = \frac{27}{3} - \frac{1}{3} = 9 - \frac{1}{3} = \frac{26}{3} \]

### Viktig å huske:
- **Konstanten C**: Når du integrerer, må du alltid legge til en vilkårlig konstant \( C \) (kalles også integrasjonskonstanten), siden derivasjonen av en konstant er null.
- **Bestemte og ubestemte integraler**: Et ubestemt integral inkluderer integrasjonskonstanten \( C \), mens et bestemt integral evalueres mellom to punkter og gir en bestemt verdi.
- **Numerisk integrasjon**: For mer komplekse funksjoner som ikke kan integreres analytisk, kan numeriske metoder brukes for å finne en tilnærmet verdi for integralet.