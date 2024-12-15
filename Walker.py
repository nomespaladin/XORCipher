import shutil
import os

# #This can help more with de BackupFunction I think
# #Copy single files 
# shutil.copy('file.txt', 'file_copy.txt')
# #Copy directories
# shutil.copytree('folder', 'folder_copy')
# #Can move directories and files
# shutil.move('folder_copy','new_destination/folder_copy')
# #function to copy the permission bits
# shutil.copystat('folder', 'folder_copy')
# #If we want to remove a directory and all its contents
# shutil.rmtree('directory')


def walker():
    user = os.getlogin()
    user_path = f"C:\Usuarios\{user}"
    print(f"The basic directory is: {user_path}")
    #In this line I'm trying to list the content of the directory I keep trying to figure out how to do it
    print(os.listdir(user_path))
    directory  = input("Write the directory you want to sript: ")
    #This line is because when you use the os.path.join its have problems with \ or /
    path = os.path.normpath(os.path.join(user_path, directory))
    print(f"{path}")

#prueba
#This function lists the directories in the current directory and then displays the contents of the directory it tells you
#May be useful later

def prueba():
    print(os.listdir(os.getcwd()))
    directory  = input("Write the directory you want to list the content: ")
    print(os.listdir(directory))

prueba()