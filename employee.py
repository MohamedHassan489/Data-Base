import pyodbc
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x500")
app.title('Employee')

entry_ssn = ctk.CTkEntry(app, placeholder_text = "SSN")
entry_ssn.place(relx=0.2 , rely=0.2)

entry_fname = ctk.CTkEntry(app, placeholder_text = "First Name")
entry_fname.place(relx=0.2 , rely=0.3)

entry_lname = ctk.CTkEntry(app, placeholder_text = "Last Name")
entry_lname.place(relx=0.2 , rely=0.4)

entry_salary = ctk.CTkEntry(app, placeholder_text = "Salary")
entry_salary.place(relx=0.2 , rely=0.5)

entry_bdate = ctk.CTkEntry(app, placeholder_text = "Birth date")
entry_bdate.place(relx=0.2 , rely=0.6)

entry_role = ctk.CTkEntry(app, placeholder_text = "Role")
entry_role.place(relx=0.2 , rely=0.6)

entry_superssn = ctk.CTkEntry(app, placeholder_text = "Super SSN")
entry_superssn.place(relx=0.2 , rely=0.7)

entry_factoryid = ctk.CTkEntry(app, placeholder_text = "Factory id")
entry_factoryid.place(relx=0.2 , rely=0.8)

def insert():
    try:
        connection =pyodbc.connect('DRIVER={SQL Server};'+
                                   'SERVER=YOUSSEFALBERT;'+
                                   'DATABASE=MedicineFactoryDB;'+
                                   'Trusted_connection= True;'
        )
        connection.autocommit= True
        connection.execute(f"insert into Employee values"+
                           f"( {entry_ssn.get()} , '{entry_fname.get()}' ,'{entry_lname.get()}' , {entry_salary.get()},'{entry_bdate.get()}' , '{entry_role.get()}', {entry_superssn.get()} , {entry_factoryid.get()}  )")
        info_label.configure(text="INSERT COMPLETED!")

    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text = "INSERT FAILED!")

insert_button = ctk.CTkButton(app, border_spacing=2,text="INSERT", command =insert, fg_color="green")
insert_button.place(relx=0.2 , rely=0.9)

table_label = ctk.CTkLabel(app , text ="Add an employee")
table_label.place(relx=0.2 , rely=0.1)

info_label = ctk.CTkLabel(app , text ="")
info_label.place(relx=0.2 , rely=0.95)

app.mainloop()