import tkinter as tk


def temp_convert():
    if cbx_temp['text'] == '\N{DEGREE FAHRENHEIT}':
        fahrenheit = ent_temperature.get()
        celsius = (5 / 9) * (float(fahrenheit) - 32)
        kelvin = celsius + 273.15
        lbl_result['text'] = (f'{celsius:.2f} \N{DEGREE CELSIUS}'
                              f'\n{kelvin:.2f} K')
    elif cbx_temp['text'] == '\N{DEGREE CELSIUS}':
        celsius = ent_temperature.get()
        fahrenheit = (float(celsius) * (9 / 5)) + 32
        kelvin = float(celsius) + 273.15
        lbl_result['text'] = (f'{fahrenheit:.2f} \N{DEGREE FAHRENHEIT}'
                              f'\n{kelvin:.2f} K')
    else:
        kelvin = ent_temperature.get()
        celsius = float(kelvin) - 273.15
        fahrenheit = (float(celsius) * (9 / 5)) + 32
        lbl_result['text'] = (f'{celsius:.2f} \N{DEGREE CELSIUS}'
                              f'\n{fahrenheit:.2f} \N{DEGREE FAHRENHEIT}')


window = tk.Tk()
window.title('Temperature Converter')

default_option = tk.StringVar(window)
default_option.set('\N{DEGREE FAHRENHEIT}')
options = {'\N{DEGREE FAHRENHEIT}', '\N{DEGREE CELSIUS}', 'K'}

frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
cbx_temp = tk.OptionMenu(frm_entry, default_option, *options)

ent_temperature.grid(row=0, column=0, sticky='e')
cbx_temp.grid(row=0, column=1, sticky='w')

btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=temp_convert
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}\nK")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()
