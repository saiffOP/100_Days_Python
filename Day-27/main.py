from tkinter import *

window = Tk()
window.title("Widgets Example")
window.minsize(width=500, height=300)

# Create a Label
my_label = Label(text="Label")
my_label.grid(column=0, row=0)
# Edit text of label
my_label.config(text="New Text")


# Buttons

def action():
    entry_text = entry.get()
    my_label.config(text=entry_text)


button = Button(text="Click Me", command=action)
button.grid(column=2, row=0)

# Entry

entry = Entry(width=30)
entry.insert(END, string="Start...")
entry.grid(column=1, row=0)

# Text
text = Text(height=5, width=35)
text.focus()
text.insert(END, "Example of multi line text entry")
text.grid(column=0, row=1)


# Spin Box
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=1, row=1)


# Scale
scale = Scale(from_=0, to=10)
scale.grid(column=0, row=2)


# Check Button
def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
check_button = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
check_button.grid(column=1, row=2)


# Radio Button
def radiobutton_used():
    print(radio_state.get())

radio_state = IntVar()
radio_button1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radiobutton_used)
radio_button2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radiobutton_used)
radio_button1.grid(column=0, row=3)
radio_button2.grid(column=0, row=4)


# ListBox

def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=0, row=5)

window.mainloop()
