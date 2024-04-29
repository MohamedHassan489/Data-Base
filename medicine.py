import pyodbc
import customtkinter as ctk
from tkinter import *
from tkinter import ttk
import tkinter as tk


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("700x500")
app.title('Medicine')

entry_productid = ctk.CTkEntry(app, placeholder_text="Product id")
entry_productid.place(relx=0.05, rely=0.1)

entry_medicinename = ctk.CTkEntry(app, placeholder_text="Name")
entry_medicinename.place(relx=0.05, rely=0.2)

entry_active = ctk.CTkEntry(app, placeholder_text="Active substance")
entry_active.place(relx=0.05, rely=0.3)

entry_price = ctk.CTkEntry(app, placeholder_text="Price")
entry_price.place(relx=0.05, rely=0.4)

entry_medicinefactoryid = ctk.CTkEntry(app, placeholder_text="Factory id")
entry_medicinefactoryid.place(relx=0.05, rely=0.5)

def insert():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};'
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;'
                                    'DATABASE=MedicineFactoryDB;'
                                    'Trusted_connection=True;')
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Medicine VALUES (?, ?, ?, ?, ?)",
                       (entry_productid.get(), entry_medicinename.get(),
                        entry_active.get(), entry_price.get(),
                        entry_medicinefactoryid.get()))
        info_label.configure(text="INSERT COMPLETED!")
        get_data_and_display()
        clear()
    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="INSERT FAILED!")

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
    entry_productid.delete(0, ctk.END)
    entry_medicinename.delete(0, ctk.END)
    entry_active.delete(0, ctk.END)
    entry_price.delete(0, ctk.END)
    entry_medicinefactoryid.delete(0, ctk.END)

def display_data(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        entry_productid.insert(0, row[0])
        entry_medicinename.insert(0, row[1])
        entry_active.insert(0, row[2])
        entry_price.insert(0, row[3])
        entry_medicinefactoryid.insert(0, row[4])

def delete():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};'
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;'
                                    'DATABASE=MedicineFactoryDB;'
                                    'Trusted_connection=True;')
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Medicine WHERE Product_id = ?", (entry_productid.get(),))
        info_label.configure(text="DELETE COMPLETED!")
        get_data_and_display()
        clear()
    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="DELETE FAILED!")

def update():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};'
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;'
                                    'DATABASE=MedicineFactoryDB;'
                                    'Trusted_connection=True;')
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute("UPDATE Medicine SET Name=?, Active_substance=?, Price=?, Factory_id=? WHERE Product_id=?",
                       (entry_medicinename.get(), entry_active.get(), entry_price.get(),
                        entry_medicinefactoryid.get(), entry_productid.get()))
        
        info_label.configure(text="UPDATE COMPLETED!")
        get_data_and_display()
        clear()
    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="UPDATE FAILED!")

def get_data_and_display():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};'
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;'
                                    'DATABASE=MedicineFactoryDB;'
                                    'Trusted_connection=True;')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Medicine")
        medicines_data = cursor.fetchall()

        for record in tree.get_children():
            tree.delete(record)

        for medicine_data in medicines_data:
            clean_data = [str(item).strip() for item in medicine_data]
            tree.insert('', 'end', values=clean_data)

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="FETCH DATA FAILED!")

insert_button = ctk.CTkButton(app, border_spacing=2, text="INSERT", command=insert, fg_color="green")
insert_button.place(relx=0.05, rely=0.6)

delete_button = ctk.CTkButton(app, border_spacing=2, text="DELETE", command=delete, fg_color="red")
delete_button.place(relx=0.2, rely=0.6)

update_button = ctk.CTkButton(app, border_spacing=2, text="UPDATE", command=update, fg_color="orange")
update_button.place(relx=0.35, rely=0.6)

table_label = ctk.CTkLabel(app, text="Add a medicine")
table_label.place(relx=0.05, rely=0.05)

info_label = ctk.CTkLabel(app, text="")
info_label.place(relx=0.05, rely=0.65)

style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview', font=('Arial', 10, 'bold'), foreground='#fff', background='#000', fieldbackground='#313837')
style.map('Treeview', background=[('selected', '#1A8F2D')])
tree = ttk.Treeview(app, height=8)
tree['columns'] = ('Product_id', 'Name', 'Active', 'Price', 'Factory_id')
tree.column('#0', width=0, stretch=ctk.NO)
tree.column('Product_id', anchor=tk.CENTER, width=100)
tree.column('Name', anchor=tk.CENTER, width=100)
tree.column('Active', anchor=tk.CENTER, width=100)
tree.column('Price', anchor=tk.CENTER, width=100)
tree.column('Factory_id', anchor=tk.CENTER, width=100)
tree.heading('Product_id', text='Product ID')
tree.heading('Name', text='Name')
tree.heading('Active', text='Active Substance')
tree.heading('Price', text='Price')
tree.heading('Factory_id', text='Factory ID')
tree.place(relx=0.5, rely=0.05)

get_data_and_display()
tree.bind('<ButtonRelease>', display_data)
app.mainloop()