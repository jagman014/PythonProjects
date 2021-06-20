import tkinter as tk

window = tk.Tk()


def handle_keypress(event):
    print(event.char)


def handle_click(event):
    print("The button was clicked!")


button = tk.Button(text="Click me!")
button.pack()

button.bind("<Button-1>", handle_click)

window.bind('<Key>', handle_keypress)

window.mainloop()

# events will occur within the mainloop()
# .bind() binds the event to a handler
# takes event in the form '<event_name>'
