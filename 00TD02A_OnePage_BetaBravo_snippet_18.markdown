# Derivasjon av Polynomfunksjoner

### Hva er derivasjon?
- Derivasjon er en metode innenfor matematisk analyse som brukes til å undersøke hvordan en funksjon endrer seg. Den gir oss informasjon om funksjonens stigningstall (hvor bratt grafen er) i hvert punkt.

### Hvorfor er derivasjon viktig?
- **Finne ekstremalpunkter**: Deriverte kan brukes til å finne toppunkter (maksima) og bunnpunkter (minima) på en funksjons graf. Dette er punkter der funksjonen endrer retning, og er viktige for å forstå funksjonens oppførsel.
- **Bestemme stigningstall**: Den deriverte gir oss stigningstallet til tangenten i et hvilket som helst punkt på grafen. Dette forteller oss hvor raskt funksjonen endrer seg i det punktet.
- **Anvendelser**: Derivasjon er et kraftig verktøy som brukes i mange fagfelt, inkludert fysikk, økonomi og ingeniørfag. For eksempel kan det brukes til å modellere hastighet og akselerasjon, optimalisere produksjon og kostnader, og designe effektive konstruksjoner.

### Derivasjonsregler:
- Det finnes flere regler for å derivere ulike typer funksjoner. Her er noen grunnleggende regler for polynomfunksjoner:
  - **Konstantregel**: Den deriverte av en konstant (et tall uten variabel) er alltid null.
    - Eksempel: \( f(x) = 5, f'(x) = 0 \)
  - **Potensregel**: Den deriverte av \( x^n \) er \( nx^{n-1} \).
    - Eksempel: \( f(x) = x^3, f'(x) = 3x^2 \)
  - **Sumregel og differansregel**: Den deriverte av en sum eller differanse av funksjoner er lik summen eller differansen av de deriverte.
    - Eksempel: \( f(x) = x^2 + 3x, f'(x) = 2x + 3 \)

### Anvendelser av derivasjon (polynomfunksjoner):
- **Finne ekstremalpunkter**: For å finne ekstremalpunktene til en polynomfunksjon, setter du den deriverte lik null og løser for \( x \). Deretter kan du finne de tilsvarende \( y \)-verdiene ved å sette inn \( x \)-verdiene i den opprinnelige funksjonen.
- **Bestemme stigningstall**: For å finne stigningstallet til en polynomfunksjon i et bestemt punkt, setter du inn \( x \)-verdien til punktet i den deriverte funksjonen. Resultatet er stigningstallet i det punktet.

### Eksempel:
- Finn ekstremalpunktene til funksjonen \( f(x) = x^3 - 3x^2 + 2 \).
  1. Finn den deriverte: \( f'(x) = 3x^2 - 6x \)
  2. Sett den deriverte lik null og løs for \( x \): \( 3x^2 - 6x = 0 \Rightarrow x(3x - 6) = 0 \Rightarrow x = 0 \) eller \( x = 2 \)
  3. Finn \( y \)-verdiene: \( f(0) = 2 \), \( f(2) = -2 \)
  4. Ekstremalpunktene er: \( (0, 2) \) (maksimum) og \( (2, -2) \) (minimum)

### Viktig å huske:
- **Fortegnsskjema**: Et fortegnsskjema hjelper deg å finne ut

 hvor funksjonen stiger og synker ved å analysere fortegnet til den deriverte.
- **Andre deriverte**: Den andre deriverte kan gi informasjon om konvekse og konkave områder på grafen.
- **Grenseverdier**: For å finne funksjonens oppførsel når \( x \) går mot uendelig eller et annet spesifikt punkt, kan du bruke grenseverdier.