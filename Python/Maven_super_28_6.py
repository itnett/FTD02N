python
import tkinter as tk

def trykk(tall):
    nåværende = inndata.get()
    inndata.delete(0, tk.END)
    inndata.insert(tk.END, nåværende + str(tall))

def beregn():
    try:
        resultat = eval(inndata.get())
        inndata.delete(0, tk.END)
        inndata.insert(tk.END, str(resultat))
    except:
        inndata.delete(0, tk.END)
        inndata.insert(tk.END, "Feil")

def slett():
    inndata.delete(0, tk.END)

vindu = tk.Tk()
vindu.title("Enkel Kalkulator")

inndata = tk.Entry(vindu, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
inndata.grid(row=0, column=0, columnspan=4)

# Knappene på kalkulatoren
tall_knapper = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0'
]

rad = 1
kolonne = 0
for tall in tall_knapper:
    tk.Button(vindu, text=tall, width=5, height=2, command=lambda t=tall: trykk(t)).grid(row=rad, column=kolonne)
    kolonne += 1
    if kolonne > 2:
        kolonne = 0
        rad += 1

# Operasjonsknapper
tk.Button(vindu, text="+", width=5, height=2, command=lambda: trykk('+')).grid(row=1, column=3)
tk.Button(vindu, text="-", width=5, height=2, command=lambda: trykk('-')).grid(row=2, column=3)
tk.Button(vindu, text="*", width=5, height=2, command=lambda: trykk('*')).grid(row=3, column=3)
tk.Button(vindu, text="/", width=5, height=2, command=lambda: trykk('/')).grid(row=4, column=3)

# Beregnings- og slettknapper
tk.Button(vindu, text="=", width=11, height=2, command=beregn).grid(row=5, column=0, columnspan=2)
tk.Button(vindu, text="C", width=11, height=2, command=slett).grid(row=5, column=2, columnspan=2)

vindu.mainloop()