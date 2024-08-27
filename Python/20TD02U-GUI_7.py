python
   import tkinter as tk

   root = tk.Tk()
   root.title("Grid Layout")

   tk.Label(root, text="Rad 0, Kolonne 0").grid(row=0, column=0)
   tk.Label(root, text="Rad 0, Kolonne 1").grid(row=0, column=1)
   tk.Label(root, text="Rad 1, Kolonne 0").grid(row=1, column=0)
   tk.Label(root, text="Rad 1, Kolonne 1").grid(row=1, column=1)

   root.mainloop()