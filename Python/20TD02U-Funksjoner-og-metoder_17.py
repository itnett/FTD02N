python
     from tkinter import Tk, Label, Button

     def on_button_click():
         label.config(text="Button clicked!")

     root = Tk()
     label = Label(root, text="Hello, World!")
     label.pack()
     button = Button(root, text="Click me", command=on_button_click)
     button.pack()
     root.mainloop()