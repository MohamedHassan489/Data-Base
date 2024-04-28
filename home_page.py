import tkinter as tk
import os

root = tk.Tk()
root.geometry('300x700')
root.title('home page')

def open_add_user_window():
    add_user_window = CustomTkinterWindow(root)

def toggle_menu():
    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='☰')
        toggle_btn.config(command=toggle_menu)

    toggle_menu_fm = tk.Frame(root, bg='#158aff')

    products_btn = tk.Button(toggle_menu_fm, text='Products', font=('bold', 20), bd=0, bg='#158aff', fg='white', activebackground='#158aff', activeforeground='white', command=open_products_window)
    products_btn.place(x=15, y=20)

    export_btn = tk.Button(toggle_menu_fm, text='Export', font=('bold', 20), bd=0, bg='#158aff', fg='white', activebackground='#158aff', activeforeground='white', command=open_export_window)
    export_btn.place(x=15, y=80)

    import_btn = tk.Button(toggle_menu_fm, text='Import', font=('bold', 20), bd=0, bg='#158aff', fg='white', activebackground='#158aff', activeforeground='white', command=open_import_window)
    import_btn.place(x=15, y=140)

    add_supplier_btn = tk.Button(toggle_menu_fm, text='Supplier', font=('bold', 20), bd=0, bg='#158aff', fg='white', activebackground='#158aff', activeforeground='white',command=open_supplier_window)
    add_supplier_btn.place(x=15, y=200)

    add_user_btn = tk.Button(toggle_menu_fm, text='Employee', font=('bold', 20), bd=0, bg='#158aff', fg='white', activebackground='#158aff', activeforeground='white', command=open_employee_window)
    add_user_btn.place(x=15, y=260)

    add_pharmacy_btn = tk.Button(toggle_menu_fm, text='Pharmacy', font=('bold', 20), bd=0, bg='#158aff', fg='white', activebackground='#158aff', activeforeground='white',command=open_pharmacy_window)
    add_pharmacy_btn.place(x=15, y=320)

    add_factory_btn = tk.Button(toggle_menu_fm, text='Factory', font=('bold', 20), bd=0, bg='#158aff', fg='white', activebackground='#158aff', activeforeground='white',command=open_factory_window)
    add_factory_btn.place(x=15, y=380)

    add_machines_btn = tk.Button(toggle_menu_fm, text='Machine', font=('bold', 20), bd=0, bg='#158aff', fg='white', activebackground='#158aff', activeforeground='white',command=open_machine_window)
    add_machines_btn.place(x=15, y=440)

    add_medicine_btn = tk.Button(toggle_menu_fm, text='Medicine', font=('bold', 20), bd=0, bg='#158aff', fg='white', activebackground='#158aff', activeforeground='white',command=open_medicine_window)
    add_medicine_btn.place(x=15, y=500)

    add_rawmaterial_btn = tk.Button(toggle_menu_fm, text='Raw material', font=('bold', 20), bd=0, bg='#158aff', fg='white', activebackground='#158aff', activeforeground='white',command=open_rawmaterial_window)
    add_rawmaterial_btn.place(x=15, y=560)

    add_stored_in_btn = tk.Button(toggle_menu_fm, text='Stored in', font=('bold', 20), bd=0, bg='#158aff', fg='white', activebackground='#158aff', activeforeground='white',command=open_stored_in_window)
    add_stored_in_btn.place(x=15, y=620)

   

    window_height = root.winfo_height() 
    toggle_menu_fm.place(x=0, y=53, height=window_height, width=250)
    toggle_btn.config(text='X')
    toggle_btn.config(command=collapse_toggle_menu)

def open_import_window():
    root.destroy()  # Close the current window
    os.system('python imports.py')

def open_products_window():
    root.destroy()  # Close the current window
    os.system('python products.py')

def open_export_window():
    root.destroy()  # Close the current window
    os.system('python exports.py') 
def open_supplier_window():
    root.destroy()  # Close the current window
    os.system('python supplier.py') 
def open_employee_window():
    root.destroy()  # Close the current window
    os.system('python employee.py') 
def open_pharmacy_window():
    root.destroy()  # Close the current window
    os.system('python pharmacy.py')  
def open_factory_window():
    root.destroy()  # Close the current window
    os.system('python factory.py') 

def open_machine_window():
    root.destroy()  # Close the current window
    os.system('python machines.py') 
def open_medicine_window():
    root.destroy()  # Close the current window
    os.system('python medicine.py') 
def open_rawmaterial_window():
    root.destroy()  # Close the current window
    os.system('python raw_materials.py')
def open_stored_in_window():
    root.destroy()  # Close the current window
    os.system('python stored_in.py')  

toggle_btn = tk.Button(root, text='☰', bg='#158aff', fg='white', font=('Bold', 20), bd=0, activebackground='#158aff', activeforeground='white', command=toggle_menu)     
toggle_btn.pack(side=tk.LEFT, anchor=tk.NW)

head_frame = tk.Frame(root, bg='#158aff', highlightbackground='white', highlightthickness=1)
title_lb = tk.Label(head_frame, text='Menu', bg='#158aff', fg='white', font=('bold', 20))
title_lb.pack(side=tk.LEFT)
head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=53)

root.mainloop()
