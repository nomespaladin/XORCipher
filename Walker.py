import os
import shutil
#from fileX import funcionX

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
