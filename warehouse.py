import pyodbc
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x500")
app.title('Warehouse')

entry_warehouseid = ctk.CTkEntry(app, placeholder_text = "Warehouse id")
entry_warehouseid.place(relx=0.2 , rely=0.2)

entry_capacity = ctk.CTkEntry(app, placeholder_text = "Capacity")
entry_capacity.place(relx=0.2 , rely=0.3)

entry_warehousefactoryid = ctk.CTkEntry(app, placeholder_text = "Factory id")
entry_warehousefactoryid.place(relx=0.2 , rely=0.4)


def insert():
    try:
        connection =pyodbc.connect('DRIVER={SQL Server};'+
                                   'SERVER=YOUSSEFALBERT;'+
                                   'DATABASE=MedicineFactoryDB;'+
                                   'Trusted_connection= True;'
        )
        connection.autocommit= True
        connection.execute(f"insert into Warehouse values"+
                           f"( {entry_warehouseid.get()} , {entry_capacity.get()} , {entry_warehousefactoryid.get()} )")
        info_label.configure(text="INSERT COMPLETED!")

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text = "INSERT FAILED!")

insert_button = ctk.CTkButton(app, border_spacing=2,text="INSERT", command =insert, fg_color="green")
insert_button.place(relx=0.2 , rely=0.8)

table_label = ctk.CTkLabel(app , text ="Add a warehouse")
table_label.place(relx=0.2 , rely=0.1)

info_label = ctk.CTkLabel(app , text ="")
info_label.place(relx=0.2 , rely=0.9)

app.mainloop()