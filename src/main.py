import tkinter as tk
from tkinter import filedialog

import parse
import plot
import savefiles

# Variables
BG_COLOR = '#3A3A37'
TXT_COLOR = '#F0F0F0'
GREEN = '#1E4D2B'
GOLD = '#C8C372'

def choose_file():
    filename = filedialog.askopenfilename(
        title ='Choose a file',
        initialdir ='./',
        filetypes = (
            ('LabVIEW files', '*.lvm'),
            ('All files', '*.*')
        )
    )
    choose_entry.delete(0, 'end')
    choose_entry.insert(0, filename)


def main():
    for widget in widgets:
        widget.place_forget()
    
    title.configure(text='Parse and Save LabVIEW DATA')
    title.place(x=25, y=10)
    choose_entry.place(x=25, y=40)
    choose_button.place(x=25, y=60)
    to_plain_parse.place(x=25, y=120)
    to_plot.place(x=200, y=120)
    to_csv.place(x=25, y=200)
    to_xl.place(x=200, y=200)
    to_mat.place(x=375, y=200)


def plain_parse():
    for widget in widgets:
        widget.place_forget()
    
    title.configure(text='Plain Parse')
    title.place(x=25, y=10)
    back_button.place(x=525, y=250)

    try:
        filename = choose_entry.get()
        data = parse.parse_lvm(filename)
        info_label.configure(text=parse.data_to_infotxt(data))
    except FileNotFoundError:
        info_label.configure(text='File Not Found\n\nTry again')

    info_label.place(x=75, y=40)


def make_plots():
    for widget in widgets:
        widget.place_forget()

    title.configure(text='Plot Data Sets')
    title.place(x=25, y=10)
    back_button.place(x=525, y=250)
    
    try:
        filename = choose_entry.get()
        data = parse.parse_lvm(filename)
        info_label.configure(text=parse.data_to_infotxt(data))
        info_label.place(x=75, y=40)
        plot.plot_data_sets(data)
    except FileNotFoundError:
        info_label.configure(text='File Not Found\n\nTry again')
        info_label.place(x=75, y=40)


def make_csv():
    for widget in widgets:
        widget.place_forget()

    title.configure(text='Save Data to CSV')
    title.place(x=25, y=10)
    back_button.place(x=525, y=250)

    try:
        filename = choose_entry.get()
        data = parse.parse_lvm(filename)
        new_path = savefiles.save_to_csv(data, filename)
        label_text = f'Path = {new_path}\n\n' + parse.data_to_infotxt(data)
        info_label.configure(text=label_text)
        info_label.place(x=75, y=40)
    except FileNotFoundError:
        info_label.configure(text='File Not Found\n\nTry again')
        info_label.place(x=75, y=40)


def make_mat():
    for widget in widgets:
        widget.place_forget()

    title.configure(text='Save Data to .mat')
    title.place(x=25, y=10)
    back_button.place(x=525, y=250)

    try:
        filename = choose_entry.get()
        data = parse.parse_lvm(filename)
        new_path = savefiles.save_to_mat(data, filename)
        label_text = f'Path = {new_path}\n\n' + parse.data_to_infotxt(data)
        info_label.configure(text=label_text)
        info_label.place(x=75, y=40)
    except FileNotFoundError:
        info_label.configure(text='File Not Found\n\nTry again')
        info_label.place(x=75, y=40)


def make_xl():
    for widget in widgets:
        widget.place_forget()

    title.configure(text='Save Data to Excel')
    title.place(x=25, y=10)
    back_button.place(x=525, y=250)

    try:
        filename = choose_entry.get()
        data = parse.parse_lvm(filename)
        new_path = savefiles.save_to_xl(data, filename)
        label_text = f'Path = {new_path}\n\n' + parse.data_to_infotxt(data)
        info_label.configure(text=label_text)
        info_label.place(x=75, y=40)
    except FileNotFoundError:
        info_label.configure(text='File Not Found\n\nTry again')
        info_label.place(x=75, y=40)


# Window setup
root = tk.Tk()
root.title('LabVIEW Parser')
root.geometry('600x300')
root.resizable(False, False)
root.configure(bg=BG_COLOR)

widgets = [
    title := tk.Label(root, bg=BG_COLOR, fg=TXT_COLOR),
    back_button := tk.Button(root, text='Back', bg=GREEN, fg=TXT_COLOR, command=main),
    choose_entry := tk.Entry(root, width=90),
    choose_button := tk.Button(root, text='Choose a file', bg=GREEN, fg=TXT_COLOR, command=choose_file),
    to_csv := tk.Button(root, text='Save to CSV', height=2, width=15, bg=GOLD, command=make_csv),
    to_xl := tk.Button(root, text='Save to Excel', height=2, width=15, bg=GOLD, command=make_xl),
    to_mat := tk.Button(root, text='Save to .mat', height=2, width=15, bg=GOLD, command=make_mat),
    to_plot := tk.Button(root, text='Plot', height=2, width=15, bg=GOLD, command=make_plots),
    to_plain_parse := tk.Button(root, text='Plain Parse', height=2, width=15, bg=GOLD, command=plain_parse),
    info_label := tk.Label(root, bg=BG_COLOR, fg=TXT_COLOR, justify=tk.LEFT)
]


if __name__ == '__main__':
    main()
    root.mainloop()