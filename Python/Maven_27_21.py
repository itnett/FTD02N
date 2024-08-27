python
    import tkinter as tk

    def show_message():
        message_label.config(text="Hello, Tkinter!")

    window = tk.Tk()
    window.title("Simple GUI")

    message_label = tk.Label(window, text="")
    message_label.pack()

    show_button = tk.Button(window, text="Click Me", command=show_message)
    show_button.pack()

    window.mainloop()