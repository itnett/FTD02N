python
   import tkinter as tk

   def hilsen():
       navn = navn_input.get()
       hilsen_label.config(text=f"Hej, {navn}!")

   vindu = tk.Tk()
   vindu.title("Enkel hilsen")

   tk.Label(vindu, text="Navn:").pack()
   navn_input = tk.Entry(vindu)
   navn_input.pack()

   tk.Button(vindu, text="Hils", command=hilsen).pack()

   hilsen_label = tk.Label(vindu)
   hilsen_label.pack()

   vindu.mainloop()