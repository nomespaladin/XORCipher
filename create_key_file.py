
def create_keyfile_dict(file_path_list):
    keyfile_dict = {}
    for file in file_path_list:
        keyfile_dict[file] = generate_token(101)
    return keyfile_dict
# convierte el diccionario a una variable

tokenized_dict = create_keyfile_dict(file_path_list)