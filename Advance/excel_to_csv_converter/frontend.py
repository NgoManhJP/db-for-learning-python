from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pandas as pd

def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def open_input_file():
    """
    This is comment for open_input_file() method

    """
    # root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("excel files","*.xls"),("all files","*.*")))
    root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("all files","*.*"),))
    input_file = root.filename
    # Display file name at Entry Box 1
    entry1.insert(END, input_file)
    # Load sheet name from input file
    all_sheetnames = pd.ExcelFile(input_file).sheet_names
    for sheetname in all_sheetnames:
        lbx.insert(END, sheetname)


    # workbook = xlrd.open_workbook(input_file)
    # all_wksheets = workbook.sheet_names()
    # for wksheet_name in all_wksheets:
    #     lbx.insert(END, wksheet_name)

def open_output_dir():
    """
    This is comment for open_output_dir() method

    """
    output_dir = filedialog.askdirectory()
    entry2.insert(END, output_dir)

def convert():
    """
    This is comment for convert() method

    """
    if check_input_file() == 0:
        if check_output_dir() == 0:
            get_user_cus()
            try:
                index = lbx.curselection()[0]
                sheetname = lbx.get(index)
                try:
                    xls_file = pd.read_excel(excel_file, sheet_name=sheetname)
                    try:
                        xls_file.to_csv('%s/%s.%s' % (save_dir, sheetname, filetype), sep=sep, index=False)  # , quotechar=quotechar )
                        messagebox.showinfo(title="Show Info", message="Convert Successed!")
                    except:
                        messagebox.showerror(title="Show Error", message="Failed to save file!")
                        pass
                except:
                    messagebox.showerror(title="Show Error", message="Failed to open file!")
                    pass
            except:
                messagebox.showinfo(title="Show Info", message="Select one sheet to convert!")
                pass

def convert_all()    :
    """
    This is comment for convert_all() method

    """
    if check_input_file() == 0:
        if check_output_dir() == 0:
            get_user_cus()
            try:
                all_sheetnames = pd.ExcelFile(excel_file).sheet_names
                for sheetname in all_sheetnames:
                    try:
                        xls_file = pd.read_excel(excel_file, sheet_name=sheetname)
                        xls_file.to_csv('%s/%s.%s' %(save_dir, sheetname, filetype), sep=sep, index=False, quotechar='"', doublequote=True)
                    except:
                        print('Failed to save file!')
                        pass
                messagebox.showinfo(title="Show Info", message="Convert Successed!")
            except:
                print('Failed to open file!')
                pass

def get_user_cus():
    global excel_file
    global save_dir
    global sep
    global quotechar
    global filetype
    excel_file = input_file.get()
    save_dir =  output_dir.get() + "/"

    if separator.get()== 'Comma':
        sep = ','
    else:
        sep = '\t'

    if quote.get()=='None':
        quotechar = ''
    else:
        quotechar = '"'

    if file_type.get()=='.txt':
        filetype='.txt'
    else:
        filetype='.csv'

def check_input_file()        :
    if input_file.get() == "":
        messagebox.showwarning(title = "Input File Path Null", message = "Please select input file!")
        return -1
    else:
        return 0

def check_output_dir()        :
    if output_dir.get() == "":
        messagebox.showwarning(title = "Output Directory Null", message = "Please select output directory!")
        return -1
    else:
        return 0

if __name__ == '__main__':
    root = Tk()
    root.title('Exel Converter')

    # Label 1
    lbl1 = Label(root, text="Input File：")
    lbl1.grid(row=0, column=0)

    # Label 2
    lbl2=Label(root,text="Output Dir：")
    lbl2.grid(row=1,column=0)

    # Entry box 1
    input_file=StringVar()
    entry1=Entry(root,textvariable=input_file)
    entry1.grid(row=0,column=1, columnspan=5, sticky=W+E)

    # Entry box 2
    output_dir=StringVar()
    entry2=Entry(root,textvariable=output_dir)
    entry2.grid(row=1,column=1, columnspan=5, sticky=W+E)

    # Button 1
    btn1=Button(root, text="Select", width=12, command=open_input_file)
    btn1.grid(row=0,column=6)

    # Button 2
    btn1=Button(root, text="Select", width=12, command=open_output_dir)
    btn1.grid(row=1,column=6)

    # Label 3
    lbl3 = Label(root, text = "Separator")
    lbl3.grid(row=2, column=0)

    # Label 4
    lbl3 = Label(root, text = "Quote Char")
    lbl3.grid(row=2, column=2)

    # Label 5
    lbl4 = Label(root, text = "File Type")
    lbl4.grid(row=2, column=4)

    # Combobox 1
    separator = StringVar()
    cbb1 = ttk.Combobox(root, textvariable=separator, width = 10)
    cbb1['values']=('Comma', 'Tab')
    cbb1.set("Tab")
    cbb1.grid(row=2, column = 1, sticky=W)

    # Combobox 2
    quote = StringVar()
    cbb2 = ttk.Combobox(root, textvariable=quote, width=10)
    cbb2['values']=('None','"')
    cbb2.set('None')
    cbb2.grid(row=2, column=3)

    # Combobox 3
    file_type = StringVar()
    cbb3 = ttk.Combobox(root, textvariable=file_type, width = 10)
    cbb3['values']=('.txt', '.csv')
    cbb3.set(".csv")
    cbb3.grid(row=2, column = 5, sticky=E)

    # Listbox
    lbx=Listbox(root, height=6, width=76)
    lbx.grid(row=3, column=0,rowspan=6,columnspan=6, sticky=E)

    # Scrollbar
    srb=Scrollbar(root)
    srb.grid(row=3, column=5,rowspan=6, sticky=E)

    lbx.configure(yscrollcommand=srb.set)
    srb.configure(command=lbx.yview)

    # Button 3
    btn3=Button(root, text="Convert", height=2, width=12, command=convert)
    btn3.grid(row=3, column=6)

    # Button 4
    btn4=Button(root, text="Convert All", height=2, width=12, command=convert_all)
    btn4.grid(row=4, column=6)

    # Button 5
    btn4 = Button(root, text="Close", height=2, width=12, command=root.destroy)
    btn4.grid(row=5, column=6)

    center(root)
    root.mainloop()
