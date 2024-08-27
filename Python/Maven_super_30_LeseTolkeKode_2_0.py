python
# Importerer nødvendige biblioteker for å bygge programmet
import tkinter as tk  # GUI-biblioteket Tkinter
import requests  # For API-kall
import json  # For håndtering av JSON-data
import os  # For filbehandling
import hashlib  # For datasikkerhet, her brukt til hashing
from tkinter import messagebox  # For meldingsbokser i GUI

# Definerer en klasse for vårt NotatVerktøy, som inkluderer GUI, API-henting, filbehandling og datasikkerhet
class NotatVerktøy:
    def __init__(self, root):
        """Konstruktørmetoden for å initialisere GUI-komponenter og variabler"""
        # Binder rotvinduet (hovedvinduet) til instansvariabelen
        self.root = root  # Hovedvinduet for applikasjonen
        self.root.title("Notatverktøy")  # Setter tittelen på hovedvinduet

        # Variabeldeklarasjoner
        self.filnavn = "notater.txt"  # Filnavnet hvor notater lagres
        self.nåværende_notat = ""  # Holder innholdet av det nåværende notatet

        # GUI-komponenter
        self.text_area = tk.Text(self.root, wrap='word')  # Tekstområde for å skrive notater
        self.text_area.pack(expand=True, fill='both')  # Plasserer tekstområdet i hovedvinduet

        # Menylinje - en del av GUI som inneholder kommandoer som "Lagre", "Åpne", osv.
        self.menylinje = tk.Menu(self.root)  # Lager en menylinje
        self.root.config(menu=self.menylinje)  # Konfigurerer menylinjen i hovedvinduet

        # Filer-menyen
        fil_meny = tk.Menu(self.menylinje, tearoff=0)  # Lager en undermeny for filer
        self.menylinje.add_cascade(label="Filer", menu=fil_meny)  # Legger til "Filer" i menylinjen
        fil_meny.add_command(label="Lagre", command=self.lagre_notat)  # Legger til "Lagre"-kommando i menyen
        fil_meny.add_command(label="Åpne", command=self.åpne_notat)  # Legger til "Åpne"-kommando i menyen

        # Hjelp-menyen
        hjelp_meny = tk.Menu(self.menylinje, tearoff=0)  # Lager en undermeny for hjelp
        self.menylinje.add_cascade(label="Hjelp", menu=hjelp_meny)  # Legger til "Hjelp" i menylinjen
        hjelp_meny.add_command(label="Om", command=self.om)  # Legger til "Om"-kommando i menyen

        # Laster inn tidligere notater om filen eksisterer
        self.åpne_notat()

    def lagre_notat(self):
        """Lagrer det nåværende notatet til en fil"""
        try:
            # Åpner filen for skriving ('w' for skrive modus)
            with open(self.filnavn, 'w') as fil:
                filinnhold = self.text_area.get(1.0, tk.END)  # Henter innholdet fra tekstområdet i GUI
                fil.write(filinnhold)  # Skriver innholdet til filen
            # Viser en informasjonboks som bekrefter lagring
            messagebox.showinfo("Lagre", "Notat lagret!")
        except IOError as e:  # Fanger opp fil I/O-feil
            messagebox.showerror("Feil", f"Kunne ikke lagre notatet: {e}")

    def åpne_notat(self):
        """Åpner et notat fra fil hvis det eksisterer"""
        if os.path.exists(self.filnavn):  # Sjekker om filen eksisterer
            try:
                # Åpner filen for lesing ('r' for lesemodus)
                with open(self.filnavn, 'r') as fil:
                    innhold = fil.read()  # Leser innholdet av filen
                    self.text_area.delete(1.0, tk.END)  # Tømmer tekstområdet i GUI
                    self.text_area.insert(tk.END, innhold)  # Setter inn filinnholdet i tekstområdet
            except IOError as e:  # Fanger opp fil I/O-feil
                messagebox.showerror("Feil", f"Kunne ikke åpne notatet: {e}")

    def om(self):
        """Viser en informasjonstekst om applikasjonen"""
        messagebox.showinfo("Om", "Notatverktøy v1.0 - Et enkelt notatverktøy")

    def krypter_innhold(self, innhold):
        """Krypterer innholdet ved hjelp av en hashfunksjon"""
        hasher = hashlib.sha256()  # Initialiserer SHA-256 hashing-algoritmen
        hasher.update(innhold.encode('utf-8'))  # Oppdaterer hashen med innholdet, konvertert til bytes
        return hasher.hexdigest()  # Returnerer den heksadesimale representasjonen av hashen

    def hent_data_fra_api(self):
        """Eksempel på å hente data fra et API (f.eks. OpenWeatherMap)"""
        api_url = "https://api.openweathermap.org/data/2.5/weather?q=Oslo&appid=ditt_api_nøkkel"
        try:
            respons = requests.get(api_url)  # Sender en GET-forespørsel til API-en
            data = respons.json()  # Konverterer svaret til JSON
            temperatur = data['main']['temp']  # Henter temperaturen fra dataen
            # Konverterer temperaturen fra Kelvin til Celsius
            return f"Temperaturen i Oslo er {temperatur - 273.15:.2f}°C"
        except requests.RequestException as e:  # Fanger opp nettverksfeil
            messagebox.showerror("Feil", f"Kunne ikke hente data fra API: {e}")
            return "Ingen data tilgjengelig"

# Starten på programmet, som lager rotvinduet og starter applikasjonen
if __name__ == "__main__":
    root = tk.Tk()  # Oppretter hovedvinduet
    app = NotatVerktøy(root)  # Instansierer klassen NotatVerktøy
    root.mainloop()  # Starter hovedløkken for GUI-en