import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text='Hello, Tkinter',
    foreground='white',
    background='#34A2FE',
    width=10,  # width and height are in text units relative to '0'
    height=10
)
label.pack()

window.mainloop()
