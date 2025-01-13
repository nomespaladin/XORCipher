# llama la funcion de backup en funcion al user_choice
def make_backup(relative_path,user_choice,backup_dir):
    if user_choice == relative_path:
        backup_files(relative_path,backup_dir)
    elif user_choice != relative_path:
        path = f"{relative_path}/{user_choice}"
        backup_files(path,backup_dir)
# crea una copia en el mismo directorio que el codigo
make_backup(relative_path,user_choice,backup_dir)