import tkinter as tk
import random
import string


#randomized password based on ticked boxes
def final(event):
    password = "" # tk.StringVar(value="")
    password_length = size.get()
    password_length = int(password_length) if password_length else 8
    characters = string.ascii_lowercase
    if uppercase_on.get():
        characters += string.ascii_uppercase
    if special_chars_on.get():
        characters += string.punctuation
    if numbers_on.get():
        characters += string.digits
    password = "".join(random.choice(characters) for i in range(password_length))
    no_result.set(password)
    # result["textvariable"] = password

        
        
# start of gui
window = tk.Tk()

# some variables.
no_result = tk.StringVar(value="")

# title
title_text = tk.Label(
text="Aero's Pawsword Generator",
fg="brown",
bg="grey",
height=5
)

# Action prompt text
action_descriptor = tk.Label(
text="Select the appropriate option and tap Generate!",
height=5
)

#size input field + text
size_text = tk.Label(text="Size")
size = tk.Entry(
width=3,
fg="grey"
)

# uppercase tick box + variable
uppercase_on = tk.BooleanVar(value=False)
upper = tk.Checkbutton(
text="Uppercase Included",
variable=uppercase_on,
onvalue=True,
offvalue=False,
height=3
)

# special characters tick box + variable
special_chars_on = tk.BooleanVar(value=False)
special_chars = tk.Checkbutton(
text = "Special Characters Included",
variable=special_chars_on,
onvalue=True,
offvalue=False,
height=3
)

# numbers tick box + variable
numbers_on = tk.BooleanVar(value=False)
numbers = tk.Checkbutton(
text="Numbers Included",
variable=numbers_on,
onvalue=True,
offvalue=False,
height=3
)

# generate button
generate = tk.Button(
text="Generate",
width=5,
height=2,
bg="grey",
fg="brown"
)

# results label, empty until something has been generated
result = tk.Label(
textvariable=no_result,
height=5
)

# pack all elements
title_text.pack(fill=tk.X)
action_descriptor.pack(fill=tk.X)
size_text.pack(fill=tk.X)
size.pack()
upper.pack()
special_chars.pack()
numbers.pack()
generate.pack()
result.pack(fill=tk.X)

generate.bind("<Button-1>", final)

window.mainloop()
