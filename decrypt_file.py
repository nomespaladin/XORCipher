def xor_decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        encrypted_char = encrypted_message[i]
        key_char = key[i % len(key)]
        
        # Convertir cada carácter a su valor numérico
        encrypted_char_value = ord(encrypted_char)
        key_char_value = ord(key_char)
        
        # Realizar la operación XOR
        decrypted_char_value = encrypted_char_value ^ key_char_value
        
        # Convertir el valor numérico del carácter desencriptado a su carácter original
        decrypted_char = chr(decrypted_char_value)
        
        decrypted_message += decrypted_char
    return decrypted_message

def read_encrypted_file(encrypted_file_path):
    # Abrir el archivo encriptado en modo lectura de binario, como archivo encriptado
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    return encrypted_data

def decrypt_file(encrypted_file_path, decrypted_file_path, key):
    # Llamada a la función read_encrypted_file() con encrypted_file_path como argumento
    # Esta función lee el archivo encriptado y devuelve su contenido
    encrypted_data = read_encrypted_file(encrypted_file_path)
    
    # Llamada a la función xor_decrypt() con encrypted_data y key como argumentos
    # Esta función realiza la desencriptación XOR de los datos encriptados usando la clave dada
    decrypted_data = xor_decrypt(encrypted_data, key)

    # Abrir el archivo decrypted_file_path en modo binario ('wb')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        # Escribir los datos desencriptados en el archivo decrypted_file
        decrypted_file.write(decrypted_data)

# Uso del ejemplo
encrypted_file_path = 'encrypted_file.txt'
decrypted_file_path = 'decrypted_file.txt'
key = 'my_secret_key'

# Llamada a la función decrypt_file() con los parámetros adecuados
decrypt_file(encrypted_file_path, decrypted_file_path, key)