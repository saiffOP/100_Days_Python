from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=60)
window.config(padx=30, pady=30)

# Taking input from user using Entry widget
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

Km_result_label = Label(text=0)
Km_result_label.grid(column=1, row=1)

Kilometer_label = Label(text="Km")
Kilometer_label.grid(column=2, row=1)


# Converting Miles into Km
def convert():
    Miles = float(miles_input.get())
    Km = round(Miles * 1.609, 2)
    Km_result_label.config(text=Km)


calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()
