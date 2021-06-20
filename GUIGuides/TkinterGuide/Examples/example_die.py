import tkinter as tk
from random import randint


def roll_d6():
    lbl_result['text'] = f'{randint(1, 6)}'


window = tk.Tk()

window.rowconfigure([0, 1], minsize=50)
window.columnconfigure(0, minsize=150)

btn_roll = tk.Button(text="Roll", command=roll_d6)
lbl_result = tk.Label()

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)

window.mainloop()
