python
   import tkinter as tk
   from tkinter import ttk
   import pandas as pd

   root = tk.Tk()
   root.title("Visning av DataFrame")

   data = {'Navn': ['Ola', 'Kari', 'Per'],
           'Alder': [23, 25, 21]}

   df = pd.DataFrame(data)

   tree = ttk.Treeview(root, columns=("Navn", "Alder"), show='headings')
   tree.heading("Navn", text="Navn")
   tree.heading("Alder", text="Alder")
   tree.pack(expand=True, fill="both")

   for index, row in df.iterrows():
       tree.insert("", tk.END, values=(row["Navn"], row["Alder"]))

   root.mainloop()