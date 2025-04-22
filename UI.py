from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from main import parser, country_list, country_remove_list, finally_command

def get_command_output():
    raw_block = parser('TEST.eu4')
    countries = country_list(raw_block)
    filtered = country_remove_list(countries)
    return finally_command(filtered)

root = Tk()
root.title("Clear AE Generator")
frm = ttk.Frame(root, padding=10)
frm.grid()

text_box = ScrolledText(frm, width=80, height=30, wrap=WORD)
text_box.grid(column=0, row=0, columnspan=2)

output = get_command_output()
text_box.insert(END, output)
text_box.configure(state='disabled')


ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1, sticky=E)

root.mainloop()
