import tkinter as tk

window = tk.Tk()

label = tk.Label(text='Name')
entry = tk.Entry(
    fg='yellow',
    bg='blue',
    width=50
)
label.pack()
entry.pack()

# entry.get() -> obtains text in entry box
# entry.insert([position], [text]) -> inserts text into entry box
# entry.delete([start position], [end position]) -> deletes text in entry box

window.mainloop()
