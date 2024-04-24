import pyodbc
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x500")
app.title('Exports')

entry_exportid = ctk.CTkEntry(app, placeholder_text = "Export id")
entry_exportid.place(relx=0.2 , rely=0.2)

entry_exportdate = ctk.CTkEntry(app, placeholder_text = "Date")
entry_exportdate.place(relx=0.2 , rely=0.3)

entry_exportquantity = ctk.CTkEntry(app, placeholder_text = "Quantity")
entry_exportquantity.place(relx=0.2 , rely=0.4)

entry_expharmacyid = ctk.CTkEntry(app, placeholder_text = "Pharmacy id")
entry_expharmacyid.place(relx=0.2 , rely=0.5)

entry_exmedicineid = ctk.CTkEntry(app, placeholder_text = "Medicine id")
entry_exmedicineid.place(relx=0.2 , rely=0.6)

entry_exfactoryid = ctk.CTkEntry(app, placeholder_text = "Factory id")
entry_exfactoryid.place(relx=0.2 , rely=0.7)


def insert():
    try:
        connection =pyodbc.connect('DRIVER={SQL Server};'+
                                   'SERVER=YOUSSEFALBERT;'+
                                   'DATABASE=MedicineFactoryDB;'+
                                   'Trusted_connection= True;'
        )
        connection.autocommit= True
        connection.execute(f"insert into Exports values"+
                           f"( {entry_exportid.get()} , '{entry_exportdate.get()}' , {entry_exportquantity.get()} , {entry_expharmacyid.get()} , {entry_exmedicineid.get()} , {entry_exfactoryid.get()})")
        info_label.configure(text="INSERT COMPLETED!")

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text = "INSERT FAILED!")

insert_button = ctk.CTkButton(app, border_spacing=2,text="INSERT", command =insert, fg_color="green")
insert_button.place(relx=0.2 , rely=0.9)

table_label = ctk.CTkLabel(app , text ="Add an export")
table_label.place(relx=0.2 , rely=0.1)

info_label = ctk.CTkLabel(app , text ="")
info_label.place(relx=0.2 , rely=0.95)

app.mainloop()