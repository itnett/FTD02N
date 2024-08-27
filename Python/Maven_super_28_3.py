python
import tkinter as tk

def vis_inndata():
    tekst = inndata.get()
    etikett.config(text=f"Inndata: {tekst}")

vindu = tk.Tk()
vindu.title("Inndata Eksempel")

etikett = tk.Label(vindu, text="Skriv noe og trykk Enter", font=("Arial", 16))
etikett.pack()

# Legge til inndatafelt
inndata = tk.Entry(vindu)
inndata.pack()

# Koble inndata til knappen
knapp = tk.Button(vindu, text="Vis inndata", command=vis_inndata)
knapp.pack()

vindu.mainloop()