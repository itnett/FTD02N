python
     from tkinter import Tk, Button

     def on_click():
         print("Button clicked!")

     root = Tk()
     button = Button(root, text="Click me", command=on_click)
     button.pack()
     root.mainloop()