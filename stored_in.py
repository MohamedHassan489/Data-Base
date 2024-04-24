import pyodbc
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x500")
app.title('Stored in')

entry_warehouseid = ctk.CTkEntry(app, placeholder_text = "Warehouse id")
entry_warehouseid.place(relx=0.2 , rely=0.2)

entry_storedmedicineid = ctk.CTkEntry(app, placeholder_text = "Medicine id")
entry_storedmedicineid.place(relx=0.2 , rely=0.3)

entry_storedquantity = ctk.CTkEntry(app, placeholder_text = "Quantity")
entry_storedquantity.place(relx=0.2 , rely=0.4)


def insert():
    try:
        connection =pyodbc.connect('DRIVER={SQL Server};'+
                                   'SERVER=YOUSSEFALBERT;'+
                                   'DATABASE=MedicineFactoryDB;'+
                                   'Trusted_connection= True;'
        )
        connection.autocommit= True
        connection.execute(f"insert into Stored_in values"+
                           f"( {entry_warehouseid.get()} , {entry_storedmedicineid.get()} , {entry_storedquantity.get()})")
        info_label.configure(text="INSERT COMPLETED!")

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text = "INSERT FAILED!")

insert_button = ctk.CTkButton(app, border_spacing=2,text="INSERT", command =insert, fg_color="green")
insert_button.place(relx=0.2 , rely=0.8)

table_label = ctk.CTkLabel(app , text ="Add a stored in")
table_label.place(relx=0.2 , rely=0.1)

info_label = ctk.CTkLabel(app , text ="")
info_label.place(relx=0.2 , rely=0.9)

app.mainloop()