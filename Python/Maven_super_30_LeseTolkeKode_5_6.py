python
# Hoveddel av koden
if __name__=="__main__" :
    wishMe()  # Ønsker brukeren velkommen

    while True:
        query = Command()  # Lytter etter brukerens kommando

        if query is None:
            continue

        # Bruker Wikipedia for å hente informasjon
        if 'wikipedia' in query or 'what is' in query or 'who is' in query or 'define' in query or 'definition' in query or 'meaning' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)