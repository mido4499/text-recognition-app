from tkinter import Tk, StringVar
from tkinter import ttk
from data_entry import create_excel
from tkinter import filedialog

root = Tk()
frm = ttk.Frame(root, padding=20)


def select_file():
    file_paths = filedialog.askopenfilenames(
        title='Select an Image',
        filetypes=[('Image Files', '*.png *.jpg *.jpeg *.bmp'), ('All Files', '*.*')]
    )
    if file_paths:
        create_excel(file_paths)




style = ttk.Style()
style.configure('Selection.TButton', font=('Arial', 16))
style.configure('Quit.TButton', font=('Arial', 12))
style.configure('Title.TLabel', font=('Arial', 24))
frm.grid()
ttk.Label(frm, style='Title.TLabel', text='Automatic Data Handler').grid(column=0, row=0, columnspan=2)

ttk.Button(frm, style='Selection.TButton', text='Select Images', command=select_file).grid(column=0, row=1, padx=100, pady=50)


ttk.Button(frm, text="quit", style='Quit.TButton', command=root.destroy).grid(column=0, row=5)
root.mainloop()