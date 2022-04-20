import tkinter as tk

window = tk.Tk()

text_box = tk.Text()
text_box.pack()

# similar methods as entry:
# .get(["<line, start=1>.<character, start=0>"], [end position])
# all text via .get('1.0', tk.END)
# .delete() and .insert() work with similar positional arguments
# .insert() needs '\n' to add newlines
# escape characters also count to positional indices

window.mainloop()
