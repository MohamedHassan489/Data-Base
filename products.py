from tkinter import *

def open_add_medicine_window():
    # Hide the main window
    root.withdraw()
    
    # Create a new window for adding medicine
    add_medicine_window = Toplevel()
    add_medicine_window.geometry("400x200")
    add_medicine_window.title("Add Medicine")
    
    # Add widgets for adding medicine
    Label(add_medicine_window, text="Add Medicine", font=("Arial", 14, "bold")).pack(pady=10)
    # Add more widgets here for adding medicine
    
   
def search_medicine_window():
    root.withdraw()
    search_medicine_window = Toplevel()
    search_medicine_window.geometry("500x300")
    search_medicine_window.title("Search Medicine")
    Label(search_medicine_window, text="Search Medicine", font=("Arial", 14, "bold")).pack(pady=10)



root = Tk()
root.geometry("500x300")
root.title("Medicines")

label_font = ("Arial", 11, "bold")
button_bg = "#4CAF50" 

Label(root, text="All medicines we have:", font=("Arial", 14, "bold"), bg="#f0f0f0", anchor="center").grid(row=0, column=0, pady=10)
Button(root, text="Add Medicine", font=label_font, bg=button_bg, fg="white", command=open_add_medicine_window).grid(row=1, column=0, pady=10)
Button(root, text="Search Medicine", font=label_font, bg=button_bg, fg="white",  command=search_medicine_window).grid(row=1, column=2, pady=10)
root.mainloop()