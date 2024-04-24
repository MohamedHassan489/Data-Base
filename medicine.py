import pyodbc
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x500")
app.title('Medicine')

entry_productid = ctk.CTkEntry(app, placeholder_text = "Product id")
entry_productid.place(relx=0.2 , rely=0.2)

entry_medicinename = ctk.CTkEntry(app, placeholder_text = "Name")
entry_medicinename.place(relx=0.2 , rely=0.3)

entry_active = ctk.CTkEntry(app, placeholder_text = "Active substance")
entry_active.place(relx=0.2 , rely=0.4)

entry_price = ctk.CTkEntry(app, placeholder_text = "Price")
entry_price.place(relx=0.2 , rely=0.5)

entry_medicinefactoryid = ctk.CTkEntry(app, placeholder_text = "Factory id")
entry_medicinefactoryid.place(relx=0.2 , rely=0.6)

def insert():
    try:
        connection =pyodbc.connect('DRIVER={SQL Server};'+
                                   'SERVER=YOUSSEFALBERT;'+
                                   'DATABASE=MedicineFactoryDB;'+
                                   'Trusted_connection= True;'
        )
        connection.autocommit= True
        connection.execute(f"insert into Medicine values"+
                           f"( {entry_productid.get()} , '{entry_medicinename.get()}' , '{entry_active.get()}' , {entry_price.get()} ,{entry_medicinefactoryid.get()} )")
        info_label.configure(text="INSERT COMPLETED!")

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text = "INSERT FAILED!")

insert_button = ctk.CTkButton(app, border_spacing=2,text="INSERT", command =insert, fg_color="green")
insert_button.place(relx=0.2 , rely=0.8)

table_label = ctk.CTkLabel(app , text ="Add a medicine")
table_label.place(relx=0.2 , rely=0.1)

info_label = ctk.CTkLabel(app , text ="")
info_label.place(relx=0.2 , rely=0.9)

app.mainloop()