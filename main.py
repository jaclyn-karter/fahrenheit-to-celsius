import tkinter as tk

# create a window
window = tk.Tk()


# create a function that takes user input from the entry widget and puts it through the Fahrenheit to Celsius conversion
# formula. the outcome will then be displayed on a label as a rounded float integer.
def enter_button():
    while True:
        try:
            global user_entry
            user_input = user_entry.get()
            degree = float(user_input) - 32 * 5/9
            degree = round(degree, 2)
            label_degree.configure(text=degree)
        # catch value error
        except ValueError:
            label_degree.config(text='')
        break


# create entry widget for user input
user_entry = tk.Entry(master=window,  bg='white', fg='black', font='times 33', width=6)
user_entry.grid(row=3, column=0,  sticky='NE')


# create title label
label = tk.Label(master=window, text='Fahrenheit to Celsius Conversion', font='times 25', fg='black')
label.grid(row=0, columnspan=4, padx=10, pady=10)

# create label to display outcome of user input in degree Celsius
label_degree = tk.Label(master=window,  bg='white', fg='black', font='times 33', width=6, relief='groove')
label_degree.grid(row=3, column=2,  sticky='W')


# create 'Degree Fahrenheit' label
label_f = tk.Label(master=window, text='Degree Fahrenheit', font='times 12', fg='black')
label_f.grid(row=4, column=0, sticky='WE')

# create 'Degree Celsius' label
label_c = tk.Label(master=window, text='Degree Celsius', font='times 12', fg='black')
label_c.grid(row=4, column=2, sticky='WE')

# create '=' label
label_equal = tk.Label(master=window, text='=', font='times 20', fg='black')
label_equal.grid(row=3, column=1, sticky='EW')

# create a 'Enter' button which will call the enter_button function when pressed.
button = tk.Button(master=window, command=enter_button, text='Enter', activebackground='black',
                   activeforeground='white', anchor='center',
                   cursor='hand2', width=10, padx=5, pady=5)
button.grid(row=20, column=1, padx=20, pady=20)

# keep the window open
window.mainloop()
