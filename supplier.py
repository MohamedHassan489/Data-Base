import pyodbc
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x500")
app.title('Supplier')

entry_supplierid = ctk.CTkEntry(app, placeholder_text = "Supplier id")
entry_supplierid.place(relx=0.2 , rely=0.2)

entry_suppliername = ctk.CTkEntry(app, placeholder_text = "Name")
entry_suppliername.place(relx=0.2 , rely=0.3)

entry_supplierphonenumber = ctk.CTkEntry(app, placeholder_text = "Phone number")
entry_supplierphonenumber.place(relx=0.2 , rely=0.4)


def insert():
    try:
        connection =pyodbc.connect('DRIVER={SQL Server};'+
                                   'SERVER=DESKTOP-PR45KHB\SQLSERVER;'+
                                   'DATABASE=master;'+
                                   'Trusted_connection= True;'
        )
        connection.autocommit= True
        connection.execute(f"insert into Supplier values"+
                           f"( {entry_supplierid.get()} , '{entry_suppliername.get()}' , {entry_supplierphonenumber.get()})")
        info_label.configure(text="INSERT COMPLETED!")

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text = "INSERT FAILED!")

insert_button = ctk.CTkButton(app, border_spacing=2,text="INSERT", command =insert, fg_color="green")
insert_button.place(relx=0.2 , rely=0.8)

table_label = ctk.CTkLabel(app , text ="Add a Supplier")
table_label.place(relx=0.2 , rely=0.1)

info_label = ctk.CTkLabel(app , text ="")
info_label.place(relx=0.2 , rely=0.9)

app.mainloop()