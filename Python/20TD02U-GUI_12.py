python
   import tkinter as tk

   root = tk.Tk()
   root.title("Canvas Widget")

   canvas = tk.Canvas(root, width=400, height=300, bg="white")
   canvas.pack()

   # Tegne en linje
   canvas.create_line(0, 0, 200, 100, fill="blue")

   # Tegne en rektangel
   canvas.create_rectangle(50, 50, 150, 100, fill="red")

   # Tegne en sirkel (oval)
   canvas.create_oval(200, 150, 300, 250, fill="green")

   root.mainloop()