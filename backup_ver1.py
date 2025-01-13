import shutil
import os
import time

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

