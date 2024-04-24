import pyodbc
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x500")
app.title('Imports')

entry_importid = ctk.CTkEntry(app, placeholder_text = "Import id")
entry_importid.place(relx=0.2 , rely=0.2)

entry_importfactoryid = ctk.CTkEntry(app, placeholder_text = "Factory id")
entry_importfactoryid.place(relx=0.2 , rely=0.3)

entry_importmaterialid = ctk.CTkEntry(app, placeholder_text = "Material id")
entry_importmaterialid.place(relx=0.2 , rely=0.4)

entry_importsupplierid = ctk.CTkEntry(app, placeholder_text = "Supplier id")
entry_importsupplierid.place(relx=0.2 , rely=0.5)

def insert():
    try:
        connection =pyodbc.connect('DRIVER={SQL Server};'+
                                   'SERVER=YOUSSEFALBERT;'+
                                   'DATABASE=MedicineFactoryDB;'+
                                   'Trusted_connection= True;'
        )
        connection.autocommit= True
        connection.execute(f"insert into Imports values"+
                           f"( {entry_importid.get()} , {entry_importfactoryid.get()} , {entry_importmaterialid.get()} , {entry_importsupplierid.get()} )")
        info_label.configure(text="INSERT COMPLETED!")

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text = "INSERT FAILED!")

insert_button = ctk.CTkButton(app, border_spacing=2,text="INSERT", command =insert, fg_color="green")
insert_button.place(relx=0.2 , rely=0.8)

table_label = ctk.CTkLabel(app , text ="Add an import")
table_label.place(relx=0.2 , rely=0.1)

info_label = ctk.CTkLabel(app , text ="")
info_label.place(relx=0.2 , rely=0.9)

app.mainloop()