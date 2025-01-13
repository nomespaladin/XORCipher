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
