import pyodbc
import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x900")
app.title('Raw Materials')

entry_materialid = ctk.CTkEntry(app, placeholder_text="Material id")
entry_materialid.place(relx=0.2, rely=0.2)

entry_materialname = ctk.CTkEntry(app, placeholder_text="Name")
entry_materialname.place(relx=0.2, rely=0.3)

info_label = ctk.CTkLabel(app, text="")
info_label.place(relx=0.2, rely=0.9)



def insert():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'SERVER=YOUSSEFALBERT;' +
                                    'DATABASE=MedicineFactoryDB;' +
                                    'Trusted_connection= True;'
                                    )
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"insert into Raw_Materials values" +
                       f"( {entry_materialid.get()} , '{entry_materialname.get()}')")
        info_label.configure(text="INSERT COMPLETED!")
        get_data_and_display()
        clear()

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="INSERT FAILED!")

def update():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'SERVER=YOUSSEFALBERT;' +
                                    'DATABASE=MedicineFactoryDB;' +
                                    'Trusted_connection= True;'
                                    )
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"UPDATE Raw_Materials SET Name = '{entry_materialname.get()}' WHERE Material_ID = {entry_materialid.get()}")
        get_data_and_display()
        info_label.configure(text="UPDATE COMPLETED!")
        clear()

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="UPDATE FAILED!")

def delete():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'SERVER=YOUSSEFALBERT;' +
                                    'DATABASE=MedicineFactoryDB;' +
                                    'Trusted_connection= True;'
                                    )
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM Raw_Materials WHERE Material_ID = {entry_materialid.get()}")
        get_data_and_display()
        info_label.configure(text="DELETE COMPLETED!")
        clear()

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="DELETE FAILED!")

def clear():
    entry_materialid.delete(0, ctk.END)
    entry_materialname.delete(0, ctk.END)

def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        entry_materialid.insert(0, row[0])
        entry_materialname.insert(0, row[1])
    else:
        pass


def get_data_and_display():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'SERVER=YOUSSEFALBERT;' +
                                    'DATABASE=MedicineFactoryDB;' +
                                    'Trusted_connection= True;'
                                    )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Raw_Materials")
        materials_data = cursor.fetchall()

        # Clearing existing items in the Treeview
        for record in tree.get_children():
            tree.delete(record)

        # Adding data from the database to the Treeview
        for material_data in materials_data:
            tree.insert('', 'end', values=material_data)

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="FETCH DATA FAILED!")

insert_button = ctk.CTkButton(app, border_spacing=2, text="INSERT", command=insert, fg_color="green")
insert_button.place(relx=0.2, rely=0.8)

delete_button = ctk.CTkButton(app, border_spacing=2, text="DELETE", command=delete, fg_color="red")
delete_button.place(relx=0.4, rely=0.8)

update_button = ctk.CTkButton(app, border_spacing=2, text="UPDATE", command=update, fg_color="orange")
update_button.place(relx=0.6, rely=0.8)

table_label = ctk.CTkLabel(app, text="Add a raw material")
table_label.place(relx=0.2, rely=0.1)

info_label = ctk.CTkLabel(app, text="")
info_label.place(relx=0.2, rely=0.9)
tree_columns = ('Material ID', 'Name')
tree = ttk.Treeview(app, columns=tree_columns, show='headings')

tree.heading('Material ID', text='Material ID')
tree.heading('Name', text='Name')
tree.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.4)

get_data_and_display()

tree.bind('<ButtonRelease>',display_data)

app.mainloop()
