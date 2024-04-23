import tkinter as tk
import os

root = tk.Tk()
root.geometry('300x500')
root.title('home page')


def open_add_user_window():
    add_user_window = CustomTkinterWindow(root)

def toggle_menu():
   def collapse_toggle_menu():
      toggle_menu_fm.destroy()
      toggle_btn.config(text='☰')
      toggle_btn.config(command=toggle_menu) 

   
   toggle_menu_fm = tk.Frame(root, bg='#158aff')
   def open_products_window():
        root.destroy()  # Close the current window
        os.system('python products.py')
   products_btn = tk.Button(toggle_menu_fm,text='Products',font=('bold',20),bd=0,bg='#158aff',fg='white',activebackground='#158aff',activeforeground='white',command=open_products_window)
   products_btn.place(x=15,y=20)

   export_btn = tk.Button(toggle_menu_fm,text='Export',font=('bold',20),bd=0,bg='#158aff',fg='white',activebackground='#158aff',activeforeground='white')
   export_btn.place(x=15,y=80)

   import_btn = tk.Button(toggle_menu_fm,text='Import',font=('bold',20),bd=0,bg='#158aff',fg='white',activebackground='#158aff',activeforeground='white')
   import_btn.place(x=15,y=140)

   add_supplier_btn = tk.Button(toggle_menu_fm,text='Add supplier',font=('bold',20),bd=0,bg='#158aff',fg='white',activebackground='#158aff',activeforeground='white')
   add_supplier_btn.place(x=15,y=200)

   def open_employee_window():
        root.destroy()  # Close the current window
        os.system('python employee.py')  

   add_user_btn = tk.Button(toggle_menu_fm,text='Add employee',font=('bold',20),bd=0,bg='#158aff',fg='white',activebackground='#158aff',activeforeground='white',command=open_employee_window)
   add_user_btn.place(x=15,y=260)

   add_pharmacy_btn = tk.Button(toggle_menu_fm,text='Add pharmacy',font=('bold',20),bd=0,bg='#158aff',fg='white',activebackground='#158aff',activeforeground='white')
   add_pharmacy_btn.place(x=15,y=320)

   window_height = root.winfo_height() 
   toggle_menu_fm.place(x=0, y=53,height=window_height,width=200)
   toggle_btn.config(text='X')
   toggle_btn.config(command=collapse_toggle_menu)

head_frame = tk.Frame(root, bg='#158aff',highlightbackground='white',highlightthickness=1)


toggle_btn = tk.Button(root, text='☰', bg='#158aff', fg='white',
                       font=('Bold', 20),bd=0,activebackground='#158aff', activeforeground='white',command=toggle_menu)     

toggle_btn.pack(side=tk.LEFT,anchor=tk.NW)


title_lb = tk.Label(head_frame,text='Menu',bg='#158aff',fg='white',font=('bold',20))

title_lb.pack(side=tk.LEFT)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=53)




root.mainloop()