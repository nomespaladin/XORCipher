
import random
import string
import os 
from datetime import datetime

def generate_token():
    token = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16))
    current_time = datetime.now()
    actual = current_time.strftime("%H:%M:%S %A %d %B %Y")
    #return f"Token: {token}, Time: {actual}"
    return token


"""def token_log(log):
    with open("log.txt", "a") as saves:
        saves.write(f"{log}\n")

if __name__ == "__main__":
    token_entry = generate_token()
    print(f"Generated Token Entry: {token_entry}")

    token_log(token_entry)"""
files_list = []
files_token= {}
for root,dirs,files in os.walk("C:\\Program Files (x86)"):
    for file in files:
        files_token[file]= generate_token()

for file, token in files_token.items():
    print(f"{file}:  {token}")       



