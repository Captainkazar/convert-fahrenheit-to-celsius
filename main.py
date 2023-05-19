from tkinter import *


def fahrenheit_to_celsius():
    fahrenheit = float(fahrenheit_input.get())
    celsius = (fahrenheit - 32) * 5/9
    celsius_result_label.config(text=f"{celsius}")


window = Tk()
window.title("Fahrenheit to Celsius converter.")
window.config(padx=20, pady=20)

fahrenheit_input = Entry(width=7)
fahrenheit_input.grid(column=1, row=0)
fahrenheit_input.focus()

fahrenheit_label = Label(text="Fahrenheit")
fahrenheit_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

celsius_result_label = Label(text="0")
celsius_result_label.grid(column=1, row=1)

celsius_label = Label(text="°C")
celsius_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=fahrenheit_to_celsius)
calculate_button.grid(column=1, row=2)


window.mainloop()
