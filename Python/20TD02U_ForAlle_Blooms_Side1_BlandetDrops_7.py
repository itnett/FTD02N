python
import tkinter as tk

def hilsen():
    navn = navn_input.get()
    hilsen_label.config(text="Hei, " + navn + "!")

vindu = tk.Tk()
vindu.title("Enkel hilsen")

navn_label = tk.Label(vindu, text="Navn:")
navn_label.pack()

navn_input = tk.Entry(vindu)
navn_input.pack()

hilsen_knapp = tk.Button(vindu, text="Hils", command=hilsen)
hilsen_knapp.pack()

hilsen_label = tk.Label(vindu, text="")
hilsen_label.pack()

vindu.mainloop()