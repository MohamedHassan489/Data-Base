import pyodbc
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x500")
app.title('Machines')

entry_serialnumber = ctk.CTkEntry(app, placeholder_text = "Serial Number")
entry_serialnumber.place(relx=0.2 , rely=0.2)

entry_brand = ctk.CTkEntry(app, placeholder_text = "Brand")
entry_brand.place(relx=0.2 , rely=0.3)

entry_func = ctk.CTkEntry(app, placeholder_text = "Functionality")
entry_func.place(relx=0.2 , rely=0.4)

entry_machinesfactoryid = ctk.CTkEntry(app, placeholder_text = "Factory id")
entry_machinesfactoryid.place(relx=0.2 , rely=0.5)

def insert():
    try:
        connection =pyodbc.connect('DRIVER={SQL Server};'+
                                   'SERVER=YOUSSEFALBERT;'+
                                   'DATABASE=MedicineFactoryDB;'+
                                   'Trusted_connection= True;'
        )
        connection.autocommit= True
        connection.execute(f"insert into Machines values"+
                           f"( {entry_serialnumber.get()} , '{entry_brand.get()}' , '{entry_func.get()}' , {entry_machinesfactoryid.get()})")
        info_label.configure(text="INSERT COMPLETED!")

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text = "INSERT FAILED!")

insert_button = ctk.CTkButton(app, border_spacing=2,text="INSERT", command =insert, fg_color="green")
insert_button.place(relx=0.2 , rely=0.8)

table_label = ctk.CTkLabel(app , text ="Add a machine")
table_label.place(relx=0.2 , rely=0.1)

info_label = ctk.CTkLabel(app , text ="")
info_label.place(relx=0.2 , rely=0.9)

app.mainloop()