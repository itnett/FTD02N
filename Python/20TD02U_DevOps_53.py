python
  import tkinter as tk

  def on_click():
      label.config(text="Knappen ble klikket!")

  root = tk.Tk()
  root.title("Mitt første GUI")

  label = tk.Label(root, text="Hei, Tkinter!")
  label.pack()

  button = tk.Button(root, text="Klikk meg!", command=on_click)
  button.pack()

  root.mainloop()