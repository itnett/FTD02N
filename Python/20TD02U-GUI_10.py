python
   import tkinter as tk

   root = tk.Tk()
   root.title("Entry Widget")

   tk.Label(root, text="Skriv noe:").pack()
   entry = tk.Entry(root)
   entry.pack()

   def show_entry():
       print("Innholdet er:", entry.get())

   tk.Button(root, text="Vis Innhold", command=show_entry).pack()

   root.mainloop()