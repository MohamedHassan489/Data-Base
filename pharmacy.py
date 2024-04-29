import pyodbc
import customtkinter as ctk
from tkinter import *
from tkinter import ttk
import tkinter as tk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x500")
app.title('Pharmacy')

entry_pharmacyid = ctk.CTkEntry(app, placeholder_text="Pharmacy id")
entry_pharmacyid.place(relx=0.2, rely=0.2)

entry_pharmacyname = ctk.CTkEntry(app, placeholder_text="Name")
entry_pharmacyname.place(relx=0.2, rely=0.3)

entry_pharmacyaddress = ctk.CTkEntry(app, placeholder_text="Address")
entry_pharmacyaddress.place(relx=0.2, rely=0.4)

info_label = ctk.CTkLabel(app, text="")
info_label.place(relx=0.2, rely=0.9)

def insert():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};'
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;'
                                    'DATABASE=MedicineFactoryDB;'
                                    'Trusted_connection=True;')
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO Pharmacy VALUES ({entry_pharmacyid.get()}, '{entry_pharmacyname.get()}', '{entry_pharmacyaddress.get()}')")
        info_label.configure(text="INSERT COMPLETED!")
        get_data_and_display()
    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="INSERT FAILED!")

def delete():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};'
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;'
                                    'DATABASE=MedicineFactoryDB;'
                                    'Trusted_connection=True;')
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Pharmacy WHERE Pharmacy_id = ?", (entry_pharmacyid.get(),))
        info_label.configure(text="DELETE COMPLETED!")
        get_data_and_display()
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
        cursor.execute("UPDATE Pharmacy SET Name=?, Address=? WHERE Pharmacy_id=?",
                       (entry_pharmacyname.get(), entry_pharmacyaddress.get(), entry_pharmacyid.get()))
        info_label.configure(text="UPDATE COMPLETED!")
        get_data_and_display()
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
        cursor.execute("SELECT * FROM Pharmacy")
        pharmacy_data = cursor.fetchall()

        for record in tree.get_children():
            tree.delete(record)

        for pharmacy in pharmacy_data:
            clean_data = [str(item).strip() for item in pharmacy]
            tree.insert('', 'end', values=clean_data)

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="FETCH DATA FAILED!")

def populate_entry_fields(event):
    try:
        # Get the selected row
        selected_item = tree.selection()[0]
        # Get the values from the selected row
        values = tree.item(selected_item, 'values')
        # Populate the entry fields with the values
        entry_pharmacyid.delete(0, END)
        entry_pharmacyid.insert(0, values[0])
        entry_pharmacyname.delete(0, END)
        entry_pharmacyname.insert(0, values[1])
        entry_pharmacyaddress.delete(0, END)
        entry_pharmacyaddress.insert(0, values[2])
    except IndexError:
        # If no row is selected, clear the entry fields
        entry_pharmacyid.delete(0, END)
        entry_pharmacyname.delete(0, END)
        entry_pharmacyaddress.delete(0, END)


insert_button = ctk.CTkButton(app, border_spacing=2, text="INSERT", command=insert, fg_color="green")
insert_button.place(relx=0.2, rely=0.8)

delete_button = ctk.CTkButton(app, border_spacing=2, text="DELETE", command=delete, fg_color="red")
delete_button.place(relx=0.35, rely=0.8)

update_button = ctk.CTkButton(app, border_spacing=2, text="UPDATE", command=update, fg_color="orange")
update_button.place(relx=0.5, rely=0.8)

table_label = ctk.CTkLabel(app, text="Pharmacy Data")
table_label.place(relx=0.2, rely=0.1)

style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview', font=('Arial', 12, 'bold'), foreground='#fff', background='#000', fieldbackground='#313837')
style.map('Treeview', background=[('selected', '#1A8F2D')])
tree = ttk.Treeview(app, height=15)
tree.bind("<ButtonRelease-1>", populate_entry_fields)
tree['columns'] = ('PharmacyID', 'Name', 'Address')
tree.column('#0', width=0, stretch=tk.NO)
tree.column('PharmacyID', anchor=tk.CENTER, width=120)
tree.column('Name', anchor=tk.CENTER, width=200)
tree.column('Address', anchor=tk.CENTER, width=200)
tree.heading('PharmacyID', text='Pharmacy ID')
tree.heading('Name', text='Name')
tree.heading('Address', text='Address')
tree.place(relx=0.5, rely=0.1)

get_data_and_display()

app.mainloop()