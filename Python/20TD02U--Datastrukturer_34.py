python
import tkinter as tk

# Opprett et hovedvindu
root = tk.Tk()
root.title("Enkel GUI")

# Legg til en etikett
label = tk.Label(root, text="Hei, verden!")
label.pack()

# Kjør GUI
root.mainloop()