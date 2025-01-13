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
        
    