python
import tkinter as tk

def si_hei():
    label.config(text="Hei, verden!")

root = tk.Tk()
root.title("Mitt første GUI-program")

label = tk.Label(root, text="Klikk på knappen")
label.pack()

knapp = tk.Button(root, text="Klikk meg", command=si_hei)
knapp.pack()

root.mainloop()