python
import tkinter as tk

vindu = tk.Tk()
vindu.title("Etikett Eksempel")

# Legge til en etikett
etikett = tk.Label(vindu, text="Hei, verden!", font=("Arial", 16))
etikett.pack()  # Plasserer etiketten i vinduet

vindu.mainloop()