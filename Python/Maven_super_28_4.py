python
import tkinter as tk

vindu = tk.Tk()
vindu.title("Grid Layout Eksempel")

# Bruke grid layout
tk.Label(vindu, text="Navn:").grid(row=0, column=0)
tk.Entry(vindu).grid(row=0, column=1)

tk.Label(vindu, text="Alder:").grid(row=1, column=0)
tk.Entry(vindu).grid(row=1, column=1)

tk.Button(vindu, text="Send inn").grid(row=2, columnspan=2)

vindu.mainloop()