python
# Initialiserer tekst-til-tale-motoren
moon = pyttsx3.init('sapi5')  # Initialiserer pyttsx3 med SAPI5 som er en tale-API tilgjengelig i Windows
voices = moon.getProperty('voices')
moon.setProperty('voice', voices[0].id)  # Setter stemmen til den første (mannlig) i listen over tilgjengelige stemmer