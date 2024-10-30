from tkinter import *
from tkinter import ttk
from modules import db, other_windows
from modules import Writing_in_file as Edit
from datetime import datetime

# Function to open add window
def open_add():
    other_windows.open_add_equip(root, on_select_Category)


def open_about():
    other_windows.open_about_window(root)


def open_user():
    other_windows.open_add_user(root, on_select_Category)




# Create the main window
root = Tk()
root.geometry("450x700")
root.title("Renter v0.03")
root.config(bg="#F5F5F5")  # Light background

# Styling and themes
style = ttk.Style(root)
style.theme_use("clam")  # You can try 'default', 'clam', 'alt', 'vista', etc.
style.configure("TLabel", font=("Calibri", 11), background="#F5F5F5", foreground="#333333")
style.configure("TButton", font=("Calibri", 11), background="#4CAF50", foreground="white", padding=6)
style.configure("TEntry", font=("Calibri", 11), padding=4)
style.configure("TCombobox", padding=4)

# Menu setup
menu = Menu(root)
filemenu = Menu(menu, tearoff=0)
root.config(menu=menu)

menu.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='Open origin file', command=Edit.open_file)
filemenu.add_command(label='Open folder', command=Edit.open_folder)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

EditMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Edit', menu=EditMenu)
EditMenu.add_command(label='edit equip', command=open_add)
EditMenu.add_command(label='edit user', command=open_user)


helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About' , command=open_about)



#Vars



# Functions for events
def on_select_Category(event):
    selected_item = Categ_equip.get()
    if selected_item == "Computer":
        current_datas = db.get_computers("code")
    else:
        current_datas = db.get_tablets("code")
    Combo_Code['values'] = current_datas
    Combo_Code.set(current_datas[0][0])

    user_inp['values'] = db.get_users()
    on_select_model(1)

def on_select_model(event):
    Computer_model_inp.delete(0, END)
    Computer_SN_inp.delete(0, END)
    selected_item = Categ_equip.get()
    if selected_item == "Computer":
        item = db.GetComputerByCode(Combo_Code.get())
    else:
        item = db.GetTabletByCode(Combo_Code.get())
    Computer_model_inp.insert(0, item[2])
    Computer_SN_inp.insert(0, item[3])

def on_select_user(event):
    user_status_inp.delete(0, END)
    user_status_inp.insert(0, db.get_a_user_by("name", user_inp.get().split(" ")[1])[3])

def EditAndOpen():
    Edit.EditInFile(user_inp.get(), Dir_inp.get(), DataOfRent_inp.get(),
                    LastDate_inp.get(), Categ_equip.get(),
                    db.GetComputerByCode(Combo_Code.get()), actNum.get(), user_status_inp.get(), dir_status.get())

    db.save_act(actNum.get())


# Main container frames for better alignment
main_frame = Frame(root, bg="#F5F5F5", padx=10, pady=5)
main_frame.pack(fill=BOTH, expand=True)

# Adding a title or header for a modern feel
header_label = ttk.Label(main_frame, text="Renter Equipment Management", font=("Calibri", 16, "bold"))
header_label.grid(row=0, column=0, columnspan=3)

#-------------------- User Information Frame --------------------#
user_frame = LabelFrame(main_frame, text="User Information", bg="#F5F5F5", padx=20, pady=10, font=("Calibri", 12, "bold"))
user_frame.grid(row=1, column=0, sticky="ew", pady=5)

user_label = ttk.Label(user_frame, text="User:")
user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

user_inp = ttk.Combobox(user_frame, width=40, values=db.get_users())
user_inp.set(db.get_users()[0])
user_inp.grid(row=0, column=1, padx=10, pady=5)
user_inp.bind("<<ComboboxSelected>>", on_select_user)
# status
status_lbl = ttk.Label(user_frame, text="status:")
status_lbl.grid(row=1, column=0, padx=10, pady=5, sticky="w")

user_status_inp = ttk.Entry(user_frame, width=40)
user_status_inp.grid(row=1, column=1, padx=10, pady=5)
user_status_inp.insert(0, db.get_a_user_by("name", user_inp.get().split(" ")[1])[3])
#-------------------- Director Information Frame --------------------#
direct_frame = LabelFrame(main_frame, text="Admin Information", bg="#F5F5F5", padx=20, pady=10, font=("Calibri", 12, "bold"))
direct_frame.grid(row=2, column=0, sticky="ew", pady=5)

#---------Director----------#
Dir_lbl = ttk.Label(direct_frame, text="Director:")
Dir_lbl.grid(row=0, column=0, padx=10, pady=5, sticky="w")

Dir_inp = ttk.Entry(direct_frame, width=40)
Dir_inp.insert(0, "")
Dir_inp.grid(row=0, column=1, padx=10, pady=5)

Dir_status_lbl = ttk.Label(direct_frame, text="status:")
Dir_status_lbl.grid(row=1, column=0, padx=10, pady=5, sticky="w")

dir_status = ttk.Entry(direct_frame, width=40)
dir_status.insert(0, "Директор")
dir_status.grid(row=1, column=1, padx=10, pady=5)


# Rent Information Frame
rent_frame = LabelFrame(main_frame, text="Rent Information", bg="#F5F5F5", padx=20, pady=5, font=("Calibri", 12, "bold"))
rent_frame.grid(row=3, column=0, sticky="ew", pady=5)

actNum_lbl = ttk.Label(rent_frame, text="act Number:")
actNum_lbl.grid(row=0, column=0, padx=10, pady=5, sticky="w")

actNum = ttk.Entry(rent_frame, width=20)
actNum.insert(0, db.get_last_act())
actNum.grid(row=0, column=1, padx=10, pady=5)

DataOfRent_lbl = ttk.Label(rent_frame, text="Rent Date:")
DataOfRent_lbl.grid(row=1, column=0, padx=10, pady=5, sticky="w")

DataOfRent_inp = ttk.Entry(rent_frame, width=20)
DataOfRent_inp.insert(0, datetime.today().strftime('%d.%m.%Y'))
DataOfRent_inp.grid(row=1, column=1, padx=10, pady=5)

LastDate_lbl = ttk.Label(rent_frame, text="Last Date:")
LastDate_lbl.grid(row=2, column=0, padx=10, pady=5, sticky="w")

LastDate_inp = ttk.Entry(rent_frame, width=20)
LastDate_inp.insert(0, datetime.today().strftime('%d.%m.%Y'))
LastDate_inp.grid(row=2, column=1, padx=10, pady=5)

# Equipment Frame
equip_frame = LabelFrame(main_frame, text="Equipment Details", bg="#F5F5F5", padx=10, pady=5, font=("Calibri", 12, "bold"))
equip_frame.grid(row=4, column=0, sticky="ew", pady=5)

Categ_lbl = ttk.Label(equip_frame, text="Choose Category:")
Categ_lbl.grid(row=0, column=0, padx=10, pady=5, sticky="w")

Categ_equip = ttk.Combobox(equip_frame, values=["Computer", "Tablets"], width=30)
Categ_equip.set("Computer")
Categ_equip.grid(row=0, column=1, padx=10, pady=5)
Categ_equip.bind("<<ComboboxSelected>>", on_select_Category)

Combo_Code_lbl = ttk.Label(equip_frame, text="Choose Equipment:")
Combo_Code_lbl.grid(row=1, column=0, padx=10, pady=5, sticky="w")

Combo_Code = ttk.Combobox(equip_frame, values=db.get_computers("code"), width=30)
Combo_Code.set(db.get_computers("code")[0])
Combo_Code.grid(row=1, column=1, padx=10, pady=5)
Combo_Code.bind("<<ComboboxSelected>>", on_select_model)

#-------------- Model --------------#
Computer_model_lbl = ttk.Label(equip_frame, text="Model:")
Computer_model_lbl.grid(row=2, column=0, padx=10, pady=5, sticky="w")

Computer_model_inp = ttk.Entry(equip_frame, width=30)
Computer_model_inp.grid(row=2, column=1, padx=10, pady=5)

#-------------- SN --------------#
Computer_SN_lbl = ttk.Label(equip_frame, text="S/N:")
Computer_SN_lbl.grid(row=3, column=0, padx=10, pady=5, sticky="w")

Computer_SN_inp = ttk.Entry(equip_frame, width=30)
Computer_SN_inp.grid(row=3, column=1, padx=10, pady=5)

#Insering datas
item = db.GetComputerByCode(Combo_Code.get())
Computer_model_inp.insert(0, item[2])
Computer_SN_inp.insert(0, item[3])


# Edit & Open Button
button_frame = Frame(main_frame, bg="#F5F5F5")
button_frame.grid(row=5, column=0, pady=20, sticky="e")

open_file_btn = ttk.Button(button_frame, text="Edit & Open", command=EditAndOpen)
open_file_btn.grid(row=0, column=0, padx=10)

root.resizable(False, False)

root.mainloop()
