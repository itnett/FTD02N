python
   import tkinter as tk

   root = tk.Tk()
   root.title("Place Layout")

   tk.Label(root, text="Label 1").place(x=50, y=50)
   tk.Label(root, text="Label 2").place(x=100, y=100)

   root.mainloop()