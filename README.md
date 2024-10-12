# Vault Pass
Vault Pass is a program written in Python that allows you to save passwords, encrypt them, and then read them using cryptography.

## Features
- Encrypt passwords
- Save passwords
- Read passwords
- Generate passwords

## Requirements
To run this program, you will need to install the dependencies: Cryptography and Colorama. You can install them from the terminal by executing the following command:

```
pip install -r requirements.txt
```

## How to use
To use the program, first run it from your favorite code editor or from a terminal with the command:
```
python main.py
```
Once the command is executed, an options menu like the one shown below will be displayed:
```
Save passwords and encrypt [01]
Read encrypted passwords [02]
Generate Fernet key (Only if it was not generated before) [03]
Exit [04]
Select option:
```
Each option fulfills a specific function. Below is an explanation of what each one does:

- **Save Passwords and Encrypt**: This option saves a password and encrypts it using the AES encryption method with a key length of 128 bits, all done with the Python cryptography library. The passwords are saved in a ".vpef" file in the "data" folder. These passwords will be encrypted, and you will not be able to read them unless you have the correct key and the program.
  
- **Read Encrypted Passwords**: This option allows you to read previously saved encrypted passwords from a ".vpef" file, using the key stored in a ".key" file. It is essential to have the key in the corresponding "key" folder.

- **Generate Fernet Key**: This option generates a ".key" file in the "key" folder using Fernet from the Python cryptography library. It is important not to share this key with anyone or save it unprotected on your computer, as anyone with access to it could read all your passwords. Use this option only if you haven't generated a Fernet key before. If you generate a new key and use it to encrypt your passwords, the current key will be overwritten, and you will lose access to all previously encrypted passwords.

## Recommendations
To store your Fernet key, I recommend saving it on cloud services or an encrypted external drive.