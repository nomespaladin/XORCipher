import random
import string
from datetime import datetime
import os


def generate_token():
    token = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 16 ))
    current_time = datetime.now()
    actual_time = current_time.strftime("%H:%M:%S %A %d %B %Y")
    return {'Token':token,'Time':actual_time}

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


    

