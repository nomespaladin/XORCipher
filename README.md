# XORCipher Encryption Program

## Overview

The XORCipher is an encryption program designed for educational purposes. It simulates a ransomware-like behavior in a controlled environment, allowing users to encrypt files and generate decryption keys. The program is built using Python and utilizes various libraries for file handling, system information retrieval, and network communication.

You can visit hte project website at : http://seed.cybertrolls.cloud

**Disclaimer:** The authors and maintainers of this code assume NO responsibility for any consequences arising from its use, including cybercrimes and data loss. Use this code responsibly and ethically.

## Features

- **File Encryption:** Encrypts files using XOR encryption.
- **Backup Creation:** Creates backups of directories before encryption.
- **Decryption Key Generation:** Generates a unique decryption key for each file.
- **System Information Retrieval:** Gathers information about the user's operating system.
- **User -Friendly Interface:** Prompts users to select directories and files for encryption.
- **Network Communication:** Sends backup files and decryption keys to a specified server.

## Requirements

- Python 3.x
- Required Python libraries:
  - `os`
  - `random`
  - `platform`
  - `string`
  - `shutil`
  - `paramiko`
  - `time`
  - `warnings`
  - `requests`

You can install the required libraries using pip:

```sh
pip install paramiko requests
```

## Installation

1.Clone the repository:

````sh
git clone https://github.com/yourusername/xorcipher.git
````
Navigate to the project directory:

```sh
cd xorcipher
```

2.Install the required packages:

```sh
pip install -r requirements.txt
```

- Ensure you have the required libraries installed as mentioned above.

## Usage

Run the program:

````sh
python xorcipher.py
````



## Important Functions
- `generate_token(k_value)`: Generates a random token of specified length.
- ``get_system_info()``: Retrieves and displays system information.
- ``create_real_path(user)``: Creates a relative path based on the operating system.
- ``get_dirs(relative_path)``: Lists directories in the specified path.
- ``make_backup(relative_path, user_choice, backup_dir, current)``: Creates a backup of the selected directory.
- ``send_backup()``: Sends backup files to a server.
- ``xor_encrypt(tokenized_dict)``: Encrypts files using XOR encryption.
- ``custom_decipher_file(current, key_size, user)``: Creates a decryption program.

## Security Notice
This program is intended for educational purposes only. It is crucial to understand the ethical implications of using encryption and to ensure that you have permission to encrypt any files or directories. Misuse of this program can lead to legal consequences.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the **LICENSE** file for details.

## Acknowledgments
XORDeV Team for the original design and implementation.
The Python community for the libraries and resources that made this project possible.


