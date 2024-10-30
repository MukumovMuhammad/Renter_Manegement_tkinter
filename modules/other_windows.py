from tkinter import *
from tkinter import ttk
from modules import db


def on_user_close(windows, refresh_callback):
    refresh_callback(1)
    windows.destroy()


def open_about_window(root):
    # Create the main window
    about_window = Toplevel(root)
    about_window.geometry("800x500")
    about_window.title("Renter Equipment Management")

    # Set background color for modern design
    about_window.config(bg="#e9ecef")

    # Function to close the About section


    # Header for the "About" section
    header_label = Label(about_window, text="Renter Equipment Management", font=("Arial", 24, "bold"), bg="#e9ecef", fg="#212529")
    header_label.pack(pady=(30, 10))

    # Subheader
    subheader_label = Label(about_window, text="About This System", font=("Arial", 16), bg="#e9ecef", fg="#6c757d")
    subheader_label.pack(pady=(0, 20))

    # Information Text
    info_text = (
        "Renter Equipment Management is designed to streamline the management of rental equipment.\n"
        "Whether you're handling computers, tablets, or other devices, this tool offers an efficient way\n"
        "to track, update, and manage your inventory. Key features include real-time status tracking,\n"
        "category management, and easy integration with databases for seamless operations.\n\n"
        "Features:\n"
        "- Fast and intuitive equipment entry\n"
        "- Real-time equipment status tracking\n"
        "- Category-based inventory management\n"
        "- Easy data update, delete, and search functionality"
    )
    info_label = Label(about_window, text=info_text, font=("Arial", 12), bg="#e9ecef", fg="#495057", justify=LEFT)
    info_label.pack(padx=40, pady=10)

    # Add a horizontal separator (optional, for aesthetics)
    separator = Frame(about_window, height=2, bd=1, relief=SUNKEN, bg="#adb5bd")
    separator.pack(fill=X, padx=40, pady=20)

    # Footer message or version info
    version_label = Label(about_window, text="Version: 0.1.0 | © 2024 Renter Solutions", font=("Arial", 10), bg="#e9ecef", fg="#868e96")
    version_label.pack(pady=5)

    # Close Button with modern styling
    close_button = Button(about_window, text="Close", command=about_window.destroy, bg="#dc3545", fg="white", font=("Arial", 12), width=12)
    close_button.pack(pady=20)

    # Disable resizing for cleaner look
    root.resizable(False, False)


def open_add_equip(root, refresh_callback):
    # Create the main window
    addEq_window = Toplevel(root)
    addEq_window.geometry("450x650")
    addEq_window.title("Adding to DB")
    addEq_window.config(bg="#f2f2f2")  # Light background

    data = db.get_computers()
    # Use protocol to handle the close button click on the Toplevel window
    addEq_window.protocol("WM_DELETE_WINDOW", lambda: (on_user_close(addEq_window,refresh_callback)))
    def on_submit():
        model = Computer_model_inp.get()
        sn = Computer_SN_inp.get()
        code = Computer_code_inp.get()
        Computer_model_inp.delete(0, END)
        Computer_SN_inp.delete(0, END)
        Computer_code_inp.delete(0, END)

        if Category.get() == "Computers":
            db.add_computers(code, model, sn)
            data = db.get_computers()
        else:
            db.add_tablet(code, model, sn)
            data = db.get_tablets()

        comps['values'] = data
        if data:
            comps.set(data[0])

    def delete_comp():
        id = comps.get()[0]
        if Category.get() == "Computers":
            db.delete_computer(id)
            data = db.get_computers()
        else:
            db.delete_tablet(id)
            data = db.get_tablets()

        comps['values'] = data
        if data:
            comps.set(data[0])

    def category_show(event):
        if Category.get() == "Computers":
            data = db.get_computers()
        else:
            data = db.get_tablets()
        comps['values'] = data
        if data:
            comps.set(data[0])

    # Main frame for a cleaner, more structured layout
    main_frame = Frame(addEq_window, bg="#f2f2f2", padx=20, pady=20)
    main_frame.pack(fill=BOTH, expand=True)

    # Title for a modern feel
    header_label = ttk.Label(main_frame, text="Add Equipment to Database", font=("Calibri", 16, "bold"),
                             background="#f2f2f2")
    header_label.grid(row=0, column=0, columnspan=3, pady=10)

    # Category section
    category_frame = LabelFrame(main_frame, text="Category", bg="#f2f2f2", padx=10, pady=10,
                                font=("Calibri", 12, "bold"))
    category_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=10)

    Category_lbl = ttk.Label(category_frame, text="Category:")
    Category_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=E)

    Category = ttk.Combobox(category_frame, values=["Computers", "Tablets"], width=30)
    Category.grid(row=0, column=1, padx=10, pady=5)
    Category.set("Computers")
    Category.bind("<<ComboboxSelected>>", category_show)

    # Information section
    info_frame = LabelFrame(main_frame, text="Information", bg="#f2f2f2", padx=10, pady=10,
                            font=("Calibri", 12, "bold"))
    info_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=10)

    # Code
    Computer_code_lbl = ttk.Label(info_frame, text="Code:")
    Computer_code_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=E)

    Computer_code_inp = ttk.Entry(info_frame, width=40)
    Computer_code_inp.grid(row=0, column=1, padx=10, pady=5)

    # Model
    Computer_model_lbl = ttk.Label(info_frame, text="Model:")
    Computer_model_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=E)

    Computer_model_inp = ttk.Entry(info_frame, width=40)
    Computer_model_inp.grid(row=1, column=1, padx=10, pady=5)

    # S/N
    Computer_SN_lbl = ttk.Label(info_frame, text="S/N:")
    Computer_SN_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=E)

    Computer_SN_inp = ttk.Entry(info_frame, width=40)
    Computer_SN_inp.grid(row=2, column=1, padx=10, pady=5)


    # Submit button
    submit_btn = ttk.Button(main_frame, text="Submit", command=on_submit)
    submit_btn.grid(row=3, column=1,columnspan=2, pady=20, sticky="e")

    # Computers section for viewing and deleting entries
    comp_frame = LabelFrame(main_frame, text="Select & Delete Item", bg="#f2f2f2", padx=10, pady=10,
                            font=("Calibri", 12, "bold"))
    comp_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=10)

    comps_lbl = ttk.Label(comp_frame, text="Item:")
    comps_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=E)

    comps = ttk.Combobox(comp_frame, values=data, width=30)
    comps.set(data[0])
    comps.grid(row=0, column=1, padx=10, pady=5)

    # Delete button
    delete_btn = Button(main_frame, text="Delete", command=delete_comp,  bg="#dc3545", fg="white", font=("Arial", 10), width=10)
    delete_btn.grid(row=5, column=1, columnspan=2, pady=10, sticky="e")

    addEq_window.resizable(False, False)


def open_add_user(root, refresh_callback):
    # Create the main window
    add_user_window = Toplevel(root)
    add_user_window.geometry("400x400")
    add_user_window.title("Adding to DB")
    add_user_window.config(bg="#f2f2f2")  # Light background

    user_datas = db.get_users_by_typeOf()

    def delete_user():
        user_data = users.get()
        db.delete_user(user_data[0])
        user_datas = db.get_users_by_typeOf()
        users["values"] = user_datas
        users.set(user_datas[0])

    def on_submit():
        name = userName_inp.get()
        surname = userSurname_inp.get()
        status = status_inp.get()
        db.add_user(name, surname, status)
        userName_inp.delete(0,END)
        userSurname_inp.delete(0, END)

    # Use protocol to handle the close button click on the Toplevel window
    add_user_window.protocol("WM_DELETE_WINDOW", lambda: (on_user_close(add_user_window, refresh_callback)))
    # Main frame for a cleaner, more structured layout
    main_frame = Frame(add_user_window, bg="#f2f2f2", padx=5, pady=5)
    main_frame.pack(fill=BOTH, expand=True)

    # Information section
    info_frame = LabelFrame(main_frame, text="Information", bg="#f2f2f2", padx=10, pady=10,
                            font=("Calibri", 12, "bold"))
    info_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=10)

    # Name
    userName_lbl = ttk.Label(info_frame, text="Name:")
    userName_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=E)

    userName_inp = ttk.Entry(info_frame, width=40)
    userName_inp.grid(row=0, column=1, padx=10, pady=5)

    # surname
    userSurname_lbl = ttk.Label(info_frame, text="Surname:")
    userSurname_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=E)

    userSurname_inp = ttk.Entry(info_frame, width=40)
    userSurname_inp.grid(row=1, column=1, padx=10, pady=5)

    # status
    status_lbl = ttk.Label(info_frame, text="status:")
    status_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=E)

    status_inp = ttk.Entry(info_frame, width=40)
    status_inp.grid(row=2, column=1, padx=10, pady=5)


    # Submit button
    submit_btn = ttk.Button(main_frame, text="Submit", command=on_submit)
    submit_btn.grid(row=3, column=0, columnspan=2, pady=10, sticky="e")



    # Computers section for viewing and deleting entries
    users_delete_frame = LabelFrame(main_frame, text="Select & Delete Item", bg="#f2f2f2", padx=10, pady=10,
                            font=("Calibri", 12, "bold"))
    users_delete_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=10)

    users_lbl = ttk.Label(users_delete_frame, text="Item:")
    users_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=E)

    users = ttk.Combobox(users_delete_frame, values=user_datas, width=20)
    users.set(user_datas[0])
    users.grid(row=0, column=1, padx=10, pady=5)

    # Delete button
    delete_btn = Button(main_frame, text="Delete", command=delete_user, bg="#dc3545", fg="white", font=("Arial", 10),
                        width=10)
    delete_btn.grid(row=5, column=0, columnspan=2, pady=10, sticky="e")

    add_user_window.resizable(False, False)