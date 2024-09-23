import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    gender = gender_var.get()
    country = country_var.get()

    if name and email and password and gender and country:
        messagebox.showinfo("Success", f"Registration successful!\nName: {name}\nEmail: {email}")
    else:
        messagebox.showwarning("Error", "Please fill all fields!")

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")

# Title Label
title_label = tk.Label(root, text="Registration Form", font=("Arial", 16), pady=10)
title_label.pack()

# Name Field
label_name = tk.Label(root, text="Full Name", font=("Arial", 12))
label_name.pack(pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

# Email Field
label_email = tk.Label(root, text="Email", font=("Arial", 12))
label_email.pack(pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.pack(pady=5)

# Password Field
label_password = tk.Label(root, text="Password", font=("Arial", 12))
label_password.pack(pady=5)
entry_password = tk.Entry(root, show='*', width=30)
entry_password.pack(pady=5)

# Gender Field
label_gender = tk.Label(root, text="Gender", font=("Arial", 12))
label_gender.pack(pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack()

# Country Field
label_country = tk.Label(root, text="Country", font=("Arial", 12))
label_country.pack(pady=5)
country_var = tk.StringVar()
country_menu = tk.OptionMenu(root, country_var, "India", "USA", "UK", "Canada", "Australia")
country_menu.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=submit_form)
submit_button.pack(pady=20)

# Start the main event loop
root.mainloop()
