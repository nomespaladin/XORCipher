import os
import platform
import shutil
import paramiko


# variables globales del proyecto
user = os.getlogin()
current = os.getcwd()
backup_dir = f"{current}/cipher_backup/"
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