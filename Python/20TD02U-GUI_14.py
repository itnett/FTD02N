python
   import tkinter as tk
   from tkinter import ttk

   root = tk.Tk()
   root.title("Combobox Eksempel")

   tk.Label(root, text="Velg et alternativ:").pack(pady=10)

   options = ["Alternativ 1", "Alternativ 2", "Alternativ 3"]
   combobox = ttk.Combobox(root, values=options)
   combobox.pack(pady=10)

   def show_selection():
       tk.messagebox.showinfo("Valg", f"Du valgte: {combobox.get()}")

   tk.Button(root, text="Vis Valg", command=show_selection).pack(pady=10)

   root.mainloop()