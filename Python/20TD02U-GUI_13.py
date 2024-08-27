python
   import tkinter as tk
   from tkinter import messagebox

   root = tk.Tk()
   root.title("Meny Eksempel")

   menubar = tk.Menu(root)

   def on_open():
       messagebox.showinfo("Åpne", "Åpne fil")

   def on_save():
       messagebox.showinfo("Lagre", "Lagre fil")

   def on_exit():
       root.quit()

   filemenu = tk.Menu(menubar, tearoff=0)
   filemenu.add_command(label="Åpne", command=on_open)
   filemenu.add_command(label="Lagre", command=on_save)
   filemenu.add_separator()
   filemenu.add_command(label="Avslutt", command=on_exit)

   menubar.add_cascade(label="Fil", menu=filemenu)

   root.config(menu=menubar)

   root.mainloop()