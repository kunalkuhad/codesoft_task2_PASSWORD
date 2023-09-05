import tkinter as tk
import random
import string

def generate_password():
    username = username_entry.get()
    password_length = int(length_slider.get())

    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(password_length))

    generated_password = username + password
    password_label.config(text="Generated Password: " + generated_password, fg="blue")

def clear_password():
    password_label.config(text="Generated Password: ")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create the username entry field
username_label = tk.Label(window, text="Username:", font=("Helvetica", 12))
username_label.pack()
username_entry = tk.Entry(window, width=20, font=("Helvetica", 12))
username_entry.pack(pady=5)

# Create slider for password length
length_slider = tk.Scale(window, from_=6, to=30, orient=tk.HORIZONTAL, length=200, font=("Helvetica", 12))
length_slider.set(12)  # Set default length to 12
length_slider.pack(pady=10)

# Create the Generate Password button
generate_button = tk.Button(window, text="Generate Password", command=generate_password, font=("Helvetica", 12), bg="green", fg="white")
generate_button.pack(pady=5)

# Create the Clear Password button
clear_button = tk.Button(window, text="Clear Password", command=clear_password, font=("Helvetica", 12), bg="red", fg="white")
clear_button.pack(pady=5)

# Create a label to display the generated password
password_label = tk.Label(window, text="Generated Password: ", font=("Helvetica", 14))
password_label.pack(pady=10)

window.mainloop()
