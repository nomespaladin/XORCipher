#This version is made for all Windows and Linux OS 
import os
import platform

def check_os():
    os_type = platform.system()
    return os_type

def check_architecture():
    os_arch = platform.machine()
    return os_arch

def check_release():
    os_version = platform.release()
    return os_version

os_arch = check_architecture()
os_type = check_os()
os_version = check_release()
print(f"OS:{os_type}|{os_arch}|Version:{os_version}")


def walker():
    user = os.getlogin()
    print("Choose between : 'Desktop','Documents','Downloads','Images','Pictures'")
    target_directory = input("Enter Directory Name to find files:")
    dir_list = ['Desktop','Documents','Downloads','Images','Pictures']

    directory_list = []
    full_path_list = []
    full_file_path = []
    try:
        if target_directory in dir_list:
            if 'Windows' in os_type:
                relative_path = f"C:/Users/{user}/{target_directory}"
                print("Choosen 'Windows' path string")
            elif 'Linux' in os_type:
                relative_path = f"/home/{user}/{target_directory}"
                print("Choosen 'Linux' path string")

            for directory in os.listdir(relative_path):
                directory_list.append(f"{relative_path}/{directory}")
            #print(directory_list)

            for item in directory_list:
                if os.path.isdir(item):
                    try:
                    
                #print(f"Diles|{os.listdir(item)}| Found on >>> {item}")
                        for i in os.listdir(item):
                    #print(i,"Found on",item)
                            full_file_path.append(f"{item}/{i}")
                    except PermissionError:
                        continue
                else:
                    full_file_path.append(item)
            #print(full_final_path)
            for file in full_file_path:
                try:
                    
                    filename = file 
                    print(filename)
                except PermissionError:
                    continue
        else:
            raise OSError(f"Directory '{target_directory}' is not a CRITICAL directory or does NOT exist.")
    except OSError as ose:
        print(ose)
    except WindowsError:
        pass

walker()
