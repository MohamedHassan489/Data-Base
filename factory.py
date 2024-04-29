import pyodbc
import customtkinter as ctk
from tkinter import *
from tkinter import ttk
import tkinter as tk


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x500")
app.title('Factory')

entry_factoryid = ctk.CTkEntry(app, placeholder_text="Factory id")
entry_factoryid.place(relx=0.2, rely=0.2)

entry_factoryname = ctk.CTkEntry(app, placeholder_text="Name")
entry_factoryname.place(relx=0.2, rely=0.3)

entry_factoryaddress = ctk.CTkEntry(app, placeholder_text="Address")
entry_factoryaddress.place(relx=0.2, rely=0.4)

info_label = ctk.CTkLabel(app, text="")
info_label.place(relx=0.2, rely=0.9)

def insert_factory():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;' +
                                    'DATABASE=MedicineFactoryDB;' +
                                    'Trusted_connection= True;'
                                    )
        connection.autocommit = True
        connection.execute(f"INSERT INTO Factory VALUES " +
                           f"({entry_factoryid.get()}, '{entry_factoryname.get()}', '{entry_factoryaddress.get()}')")
        info_label.configure(text="INSERT COMPLETED!")
        get_factory_data_and_display()
    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="INSERT FAILED!")

def delete_factory():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;' +
                                    'DATABASE=MedicineFactoryDB;' +
                                    'Trusted_connection= True;'
                                    )
        connection.autocommit = True
        connection.execute(f"DELETE FROM Factory WHERE Factory_id = {entry_factoryid.get()}")
        info_label.configure(text="DELETE COMPLETED!")
        get_factory_data_and_display()
    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="DELETE FAILED!")

def update_factory():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;' +
                                    'DATABASE=MedicineFactoryDB;' +
                                    'Trusted_connection= True;'
                                    )
        connection.autocommit = True
        connection.execute(f"UPDATE Factory SET Name='{entry_factoryname.get()}', Address='{entry_factoryaddress.get()}' WHERE Factory_id={entry_factoryid.get()}")
        info_label.configure(text="UPDATE COMPLETED!")
        get_factory_data_and_display()
    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="UPDATE FAILED!")

def get_factory_data_and_display():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;' +
                                    'DATABASE=MedicineFactoryDB;' +
                                    'Trusted_connection= True;'
                                    )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Factory")
        factories_data = cursor.fetchall()

        # Clearing existing items in the Treeview
        for record in tree.get_children():
            tree.delete(record)
        
        # Adding data from the database to the Treeview
        for factory_data in factories_data:
            # Removing parentheses and single quotes from the data
            clean_data = [str(item).replace("(", "").replace(")", "").replace("'", "").strip() for item in factory_data]
            tree.insert('', 'end', values=clean_data)

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="FETCH DATA FAILED!")        

def clear_factory_entries():
    entry_factoryid.delete(0, END)
    entry_factoryname.delete(0, END)
    entry_factoryaddress.delete(0, END)

def display_factory_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear_factory_entries()
        entry_factoryid.insert(0, row[0])
        entry_factoryname.insert(0, row[1])
        entry_factoryaddress.insert(0, row[2])


insert_button = ctk.CTkButton(app, border_spacing=2, text="INSERT", command=insert_factory, fg_color="green")
insert_button.place(relx=0.2, rely=0.6)

delete_button = ctk.CTkButton(app, border_spacing=2, text="DELETE", command=delete_factory, fg_color="red")
delete_button.place(relx=0.5, rely=0.6)

update_button = ctk.CTkButton(app, border_spacing=2, text="UPDATE", command=update_factory, fg_color="orange")
update_button.place(relx=0.8, rely=0.6)

table_label = ctk.CTkLabel(app, text="Manage Factories")
table_label.place(relx=0.2, rely=0.1)

style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview', font=('Arial', 10, 'bold'), foreground='#fff', background='#000', fieldbackground='#313837')
style.map('Treeview', background=[('selected', '#1A8F2D')])
tree = ttk.Treeview(app, height=8)
tree['columns'] = ('Factory_id', 'Name', 'Address')
tree.column('#0', width=0, stretch=ctk.NO)
tree.column('Factory_id', anchor=tk.CENTER, width=100)
tree.column('Name', anchor=tk.CENTER, width=100)
tree.column('Address', anchor=tk.CENTER, width=100)
tree.heading('Factory_id', text='Factory ID')
tree.heading('Name', text='Name')
tree.heading('Address', text='Address')
tree.place(relx=0.7, rely=0.05, anchor="ne")  # Adjusted placement to top right corner

get_factory_data_and_display()
tree.bind('<ButtonRelease>', display_factory_data)        

app.mainloop()