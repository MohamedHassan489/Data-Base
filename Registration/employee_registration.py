from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Employee Registration Form")

# Function to handle form submission
def submit_value():
    print("Your information has been saved successfully")

# Function to open login window and hide registration form window
def open_login_window():
    login_window = Toplevel(root)
    login_window.title("Login Form")
    login_window.geometry("300x200")
    Label(login_window, text="Login Form", font=("Arial", 16, "bold")).pack(pady=10)
    # Add login form widgets here...
    # Hide registration form window
    root.withdraw()
# Styling
label_font = ("Arial", 11, "bold")
entry_font = ("Arial", 10)

# Colors
background_color = "#f2f2f2"
label_bg = "#f2f2f2"
entry_bg = "white"
button_bg = "#4CAF50"  # Green color for submit button
button_fg = "white"
link_color = "blue"

# Title Label
Label(root, text="Employee Registration Form", font=("Arial", 14, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)

# Form Labels
labels = ["Name:", "Email:", "ID:", "Address:", "Gender:"]
for i, label_text in enumerate(labels):
    Label(root, text=label_text, font=label_font, bg=label_bg).grid(row=i+1, column=0, sticky="w", padx=10)

# Form Entries
name_value = StringVar()
email_value = StringVar()
address_value = StringVar()
id_value = StringVar()
gender_value = StringVar()
check_value = IntVar()

entries = [
    Entry(root, textvariable=name_value, font=entry_font, bg=entry_bg),
    Entry(root, textvariable=email_value, font=entry_font, bg=entry_bg),
    Entry(root, textvariable=id_value, font=entry_font, bg=entry_bg),
    Entry(root, textvariable=address_value, font=entry_font, bg=entry_bg),
    Entry(root, textvariable=gender_value, font=entry_font, bg=entry_bg),
]
for i, entry in enumerate(entries):
    entry.grid(row=i+1, column=1, sticky="w", padx=10)

# Remember me Checkbox
Checkbutton(root, text="Remember me?", variable=check_value, font=label_font, bg="#f0f0f0").grid(row=len(labels)+1, column=1, sticky="w", padx=10)
# Underlined Label for "I already registered"
login_label = Label(root, text="I already registered", font=label_font, fg=link_color, cursor="hand2")
login_label.grid(row=len(labels)+1, column=0, sticky="w", padx=10, pady=5)
login_label.bind("<Button-1>", lambda event: open_login_window())

# Submit Button
Button(root, text="Submit", command=submit_value, font=label_font, bg=button_bg, fg="white").grid(row=len(labels)+2, column=1, pady=10)

root.mainloop()
