python
import tkinter as tk

def update_label(*args):
    text = entry.get()
    label.config(text=text)

root = tk.Tk()
root.title("Dynamisk Oppdatering")

entry = tk.Entry(root)
entry.pack(pady=10)
entry.bind("<KeyRelease>", update_label)

label = tk.Label(root, text="Teksten vises her")
label.pack(pady=10)

root.mainloop()