python
def vis_hilsen():
    navn = navn_inn.get()
    hilsen_tekst.config(text=f"Hei, {navn}!")

# Tekstboks for navn
navn_inn = tk.Entry(vindu, width=50)
navn_inn.pack(pady=10)

# Vis hilsen-knapp
hilsen_knapp = tk.Button(vindu, text="Vis hilsen", command=vis_hilsen)
hilsen_knapp.pack(pady=10)

# Label for å vise hilsen
hilsen_tekst = tk.Label(vindu, text="")
hilsen_tekst.pack(pady=10)