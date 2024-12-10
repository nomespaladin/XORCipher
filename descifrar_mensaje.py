#import base64

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

























# Ejemplo de uso con una cadena codificada en base64
#encrypted_message = "YmV2YXIgZWFzeQ=="  # Mensaje encriptado (codificado en base64)
#key = "secret_key"  # Clave utilizada para desencriptar

# Decodificar la cadena base64
#decoded_encrypted_message = base64.b64decode(encrypted_message).decode('utf-8')

# Desencriptar el mensaje
#decrypted_message = xor_decrypt(decoded_encrypted_message, key)

#print("Mensaje desencriptado:", decrypted_message)