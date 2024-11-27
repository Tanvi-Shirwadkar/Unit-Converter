# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:45:58 2024

@author: tanvi
"""

import tkinter
from tkinter import *
from tkinter import messagebox

app = tkinter.Tk()
app.title("Unit Converter")
app.minsize(500,550)
app.maxsize(700,550)
app.config(bg="#9EC8B9")

font1 = ("Calibri", 30, "bold")
font2 = ("Calibri", 25, "bold")
font3 = ("Calibri", 18, "bold")

unit_options = ["Length", "Mass", "Time", "Temperature"]
length_options = ["mm", "cm", "m", "km", "inches", "feet", "yards", "miles"]
mass_options = ["mg", "g", "kg", "pounds"]
time_options = ["ms", "sec", "min", "hours", "days", "weeks"]
temp_options = ["°F", "°C", "K"]

variable1 = StringVar() #unit
variable2 = StringVar() #from
variable3 = StringVar() #to

def convert():
    length_factors = {"mm":0.001, "cm":0.01, "m":1, "km":1000, "inches":0.0254, "feet":0.3048, 
                      "yards":0.9144, "miles":1609.344}
    mass_factors = {"mg":0.001, "g":1, "kg":1000, "pounds":453.59237}
    time_factors = {"ms":0.001, "sec":1, "min":60, "hours":3600, "days":86400, "weeks":604800}
    
    try:
        if variable1.get() == "Length":
            metres = float(value_entry.get()) * length_factors[variable2.get()]
            converted_value = metres / length_factors[variable3.get()]
        elif variable1.get() == "Mass":
            grams = float(value_entry.get()) * mass_factors[variable2.get()]
            converted_value = grams / mass_factors[variable3.get()]
        elif variable1.get() == "Time":
            seconds = float(value_entry.get()) * time_factors[variable2.get()]
            converted_value = seconds / time_factors[variable3.get()]
        elif variable1.get() == "Temperature":
            if variable2.get() == '°C' and variable3.get() == 'K':
                converted_value = float(value_entry.get()) + 273.15
            elif variable2.get() == '°C' and variable3.get() == '°F':
                converted_value = (float(value_entry.get()) * 9/5) + 32
            elif variable2.get() == 'K' and variable3.get() == '°C':
                converted_value = float(value_entry.get()) - 273.15
            elif variable2.get() == 'K' and variable3.get() == '°F':
                converted_value = (float(value_entry.get()) - 273.15) * 9/5 + 32
            elif variable2.get() == '°F' and variable3.get() == '°C':
                converted_value = (float(value_entry.get()) - 32) * 5/9
            elif variable2.get() == '°F' and variable3.get() == 'K':
                converted_value = (float(value_entry.get()) - 32) * 5/9 + 273.15
            
        final_label.configure(text=f'{value_entry.get()} {variable2.get()} = {converted_value:} {variable3.get()}')

    except:
        messagebox.showerror("Error", "Enter valid numeric values!")

title_label = tkinter.Label(app, text="UNIT CONVERTER", font=font1, foreground='#135D66', background="#9EC8B9")
title_label.place(x=85,y=20)

unit_label = tkinter.Label(app, text="Unit:", font=font2, foreground="#1B1A55", background="#9EC8B9")
unit_label.place(x=115,y=100)

unit_option = OptionMenu(app, variable1, *unit_options)
unit_option.place(x=275,y=110)

from_label = tkinter.Label(app, text="From:", font=font2, foreground="#1B1A55", background="#9EC8B9")
from_label.place(x=20,y=200)

from_option = OptionMenu(app, variable2, *length_options)
from_option.place(x=40,y=250)

to_label = tkinter.Label(app, text="To:", font=font2, foreground="#1B1A55", background="#9EC8B9")
to_label.place(x=200,y=200)

to_option = OptionMenu(app, variable3, *length_options)
to_option.place(x=200,y=250)

value_label = tkinter.Label(app, text="Value:", font=font2, foreground="#1B1A55", background="#9EC8B9")
value_label.place(x=340,y=200)

value_entry = tkinter.Entry(app, font=font3, foreground="black", background="white", width=10)
value_entry.place(x=340,y=250)

convert_button = tkinter.Button(app, text="Convert", command=convert, font=font2, foreground="white", background="#135D66", width=10)
convert_button.place(x=135,y=320)

result_label = tkinter.Label(app, text="Result:", font=font2, foreground="#1B1A55", background="#9EC8B9")
result_label.place(x=20,y=410)

final_label = tkinter.Label(app, text="", font=font2, foreground="black", background="#9EC8B9")
final_label.place(x=20,y=460)

def update_options(*args):
    if variable1.get() == "Length":
        from_option['menu'].delete(0, 'end')
        to_option['menu'].delete(0, 'end')
        for length_unit in length_options:
            from_option['menu'].add_command(label=length_unit, command=lambda unit=length_unit: variable2.set(unit))
            to_option['menu'].add_command(label=length_unit, command=lambda unit=length_unit: variable3.set(unit))
        variable2.set(length_options[0])
        variable3.set(length_options[1])
    
    elif variable1.get() == "Mass":
        from_option['menu'].delete(0, 'end')
        to_option['menu'].delete(0, 'end')
        for mass_unit in mass_options:
            from_option['menu'].add_command(label=mass_unit, command=lambda unit=mass_unit: variable2.set(unit))
            to_option['menu'].add_command(label=mass_unit, command=lambda unit=mass_unit: variable3.set(unit))
        variable2.set(mass_options[0])
        variable3.set(mass_options[1])
        
    elif variable1.get() == "Time":   
        from_option['menu'].delete(0, 'end')
        to_option['menu'].delete(0, 'end')
        for time_unit in time_options:
            from_option['menu'].add_command(label=time_unit, command=lambda unit=time_unit: variable2.set(unit))
            to_option['menu'].add_command(label=time_unit, command=lambda unit=time_unit: variable3.set(unit))
        variable2.set(time_options[0])
        variable3.set(time_options[1])
    
    elif variable1.get() == "Temperature":
        from_option['menu'].delete(0, 'end')
        to_option['menu'].delete(0, 'end')
        for temp_unit in temp_options:
            from_option['menu'].add_command(label=temp_unit, command=lambda unit=temp_unit: variable2.set(unit))
            to_option['menu'].add_command(label=temp_unit, command=lambda unit=temp_unit: variable3.set(unit))
        variable2.set(temp_options[0])
        variable3.set(temp_options[1])
        
variable1.trace("w", update_options)
app.mainloop()
