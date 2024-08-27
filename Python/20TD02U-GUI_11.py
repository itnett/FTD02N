python
   import tkinter as tk

   root = tk.Tk()
   root.title("Listbox med Scrollbar")

   listbox = tk.Listbox(root)
   listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

   scrollbar = tk.Scrollbar(root, orient="vertical", command=listbox.yview)
   scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

   listbox.config(yscrollcommand=scrollbar.set)

   for i in range(50):
       listbox.insert(tk.END, f"Element {i+1}")

   root.mainloop()