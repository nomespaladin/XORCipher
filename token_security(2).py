
import random
import random
import platform
import string
import shutil
def generate_token(k_value):
    token = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=k_value))
    return token

def get_system_info():
    system_info = []
    os_type = platform.system()
    system_info.append(os_type)
    os_arch = platform.machine()
    system_info.append(os_arch)
    os_version = platform.release()
    system_info.append(os_version)
    print(f"OS:{system_info[0]} | Architecture:{system_info[1]} | Version:{system_info[2]} ")
    return system_info

sysinfo = get_system_info()

