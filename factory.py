import pyodbc
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x500")
app.title('Factory')

entry_factoryid = ctk.CTkEntry(app, placeholder_text = "Facctory id")
entry_factoryid.place(relx=0.2 , rely=0.2)

entry_factoryname = ctk.CTkEntry(app, placeholder_text = "Name")
entry_factoryname.place(relx=0.2 , rely=0.3)

entry_factoryaddress = ctk.CTkEntry(app, placeholder_text = "Address")
entry_factoryaddress.place(relx=0.2 , rely=0.4)


def insert():
    try:
        connection =pyodbc.connect('DRIVER={SQL Server};'+
                                   'SERVER=YOUSSEFALBERT;'+
                                   'DATABASE=MedicineFactoryDB;'+
                                   'Trusted_connection= True;'
        )
        connection.autocommit= True
        connection.execute(f"insert into Factory values"+
                           f"( {entry_factoryid.get()} , '{entry_factoryname.get()}' , '{entry_factoryaddress.get()}' )")
        info_label.configure(text="INSERT COMPLETED!")

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text = "INSERT FAILED!")

insert_button = ctk.CTkButton(app, border_spacing=2,text="INSERT", command =insert, fg_color="green")
insert_button.place(relx=0.2 , rely=0.8)

table_label = ctk.CTkLabel(app , text ="Add a new factory")
table_label.place(relx=0.2 , rely=0.1)

info_label = ctk.CTkLabel(app , text ="")
info_label.place(relx=0.2 , rely=0.9)

app.mainloop()