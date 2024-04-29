import pyodbc
import customtkinter as ctk
from tkinter import *
from tkinter import ttk

# Set appearance mode and default color theme
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Function to insert machine data into the database
def insert():
    try:
        # Establish connection to the database
        connection = pyodbc.connect('DRIVER={SQL Server};'+
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;'+
                                    'DATABASE=MedicineFactoryDB;'+
                                    'Trusted_connection= True;')
        connection.autocommit = True
        
        # Execute SQL query to insert machine data
        connection.execute(f"INSERT INTO Machines VALUES "+
                           f"({entry_serialnumber.get()}, '{entry_brand.get()}', "+
                           f"'{entry_func.get()}', {entry_machinesfactoryid.get()})")
        info_label.configure(text="INSERT COMPLETED!")
        display_data()
    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="INSERT FAILED!")

# Function to delete machine data from the database
def delete():
    try:
        # Establish connection to the database
        connection = pyodbc.connect('DRIVER={SQL Server};'+
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;'+
                                    'DATABASE=MedicineFactoryDB;'+
                                    'Trusted_connection= True;')
        connection.autocommit = True
        
        # Execute SQL query to delete machine data
        connection.execute(f"DELETE FROM Machines WHERE SerialNumber = {entry_serialnumber.get()}")
        info_label.configure(text="DELETE COMPLETED!")
        display_data()
    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="DELETE FAILED!")

# Function to update machine data in the database
def update():
    try:
        # Establish connection to the database
        connection = pyodbc.connect('DRIVER={SQL Server};'+
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;'+
                                    'DATABASE=MedicineFactoryDB;'+
                                    'Trusted_connection= True;')
        connection.autocommit = True
        
        # Execute SQL query to update machine data
        connection.execute(f"UPDATE Machines SET Brand='{entry_brand.get()}', "+
                           f"Functionality='{entry_func.get()}', "+
                           f"FactoryID={entry_machinesfactoryid.get()} "+
                           f"WHERE SerialNumber={entry_serialnumber.get()}")
        info_label.configure(text="UPDATE COMPLETED!")
        display_data()
    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="UPDATE FAILED!")

# Function to fetch machine data from the database and display it in the Treeview
def display_data():
    try:
        # Establish connection to the database
        connection = pyodbc.connect('DRIVER={SQL Server};'+
                                    'SERVER=DESKTOP-I6LBKCA\\MSSQLSERVER1;'+
                                    'DATABASE=MedicineFactoryDB;'+
                                    'Trusted_connection= True;')
        cursor = connection.cursor()
        
        # Execute SQL query to select all machine data
        cursor.execute("SELECT * FROM Machines")
        machines_data = cursor.fetchall()

        # Clear existing data in the Treeview
        for record in tree.get_children():
            tree.delete(record)
        
        # Insert fetched data into the Treeview after cleaning it
        for machine_data in machines_data:
            # Clean data to remove extra characters
            clean_data = [str(item).strip() for item in machine_data]
            tree.insert('', 'end', values=clean_data)

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="FETCH DATA FAILED!")
# Create the main application window
app = ctk.CTk()
app.geometry("800x500")
app.title('Machines')

# Entry widgets for machine data
entry_serialnumber = ctk.CTkEntry(app, placeholder_text="Serial Number")
entry_serialnumber.place(relx=0.2, rely=0.2)

entry_brand = ctk.CTkEntry(app, placeholder_text="Brand")
entry_brand.place(relx=0.2, rely=0.3)

entry_func = ctk.CTkEntry(app, placeholder_text="Functionality")
entry_func.place(relx=0.2, rely=0.4)

entry_machinesfactoryid = ctk.CTkEntry(app, placeholder_text="Factory id")
entry_machinesfactoryid.place(relx=0.2, rely=0.5)

# Buttons to trigger actions
insert_button = ctk.CTkButton(app, border_spacing=2, text="INSERT", command=insert, fg_color="green")
insert_button.place(relx=0.2, rely=0.6)

delete_button = ctk.CTkButton(app, border_spacing=2, text="DELETE", command=delete, fg_color="red")
delete_button.place(relx=0.35, rely=0.6)

update_button = ctk.CTkButton(app, border_spacing=2, text="UPDATE", command=update, fg_color="orange")
update_button.place(relx=0.5, rely=0.6)

# Label for the machine management section
table_label = ctk.CTkLabel(app, text="Manage Machines")
table_label.place(relx=0.2, rely=0.1)

# Label to display insertion status
info_label = ctk.CTkLabel(app, text="")
info_label.place(relx=0.2, rely=0.9)

# Treeview to display machine data
tree = ttk.Treeview(app, columns=('Serial Number', 'Brand', 'Functionality', 'Factory'), show='headings')
tree.heading('Serial Number', text='Serial Number')
tree.heading('Brand', text='Brand')
tree.heading('Functionality', text='Functionality')
tree.heading('Factory', text='Factory')
tree.place(relx=0.4, rely=0.1, relwidth=0.6, relheight=0.4)

# Display machine data when the application starts
display_data()

# Start the application main loop
app.mainloop()