# Vault Pass(Preliminary version)

Vault Pass is an open source password manager programmed in Python, which allows you to save your passwords, read them, check them, and generate them.
Passwords are saved in an .evpf file (Encryption Vault Pass File) encrypted with the crytography library and using 128-bit encryption.

# Features

* Password encryption

* User encryption

* Generate strong passwords

* Save passwords

* Password check

* Open Source

# Clone repository

## Clone with HTTPS

````
git clone https://github.com/Alllternate/vault-pass.git
````
## Clone with SSH

````
git@github.com:Alllternate/vault-pass.git
````

# Security recommendations

It is highly recommended to save the generated 'key.key' file in a safe place, all this in order to avoid compromising your security, here are some recommendations for saving your 'key.key' file:

## Cloud services

* OneDrive

* Drive

* Dropbox

## USB drives or external drives encrypted with

* BitLocker(For Windows)

* VeraCrypt(For Windows and MacOS)

* FileVault(For MacOS)

* LUKS(For Linux)

* ecryptfs(For Linux)

# How to use

## Save passwords

You will need to provide a username and password, these will be saved in an .evpf file.

## Read passwords

You will need to provide your username and password that you created when you started the program for the first time, you need to have your key 'key.key' in the same directory, without these the program will not be able to read your passwords.

## Generate passwords

You will need to provide a password length from the code, since the per-entry option is not implemented at the moment.
This generates a password based on the length provided.

## Check passwords

You must provide your password, the program will define if your password is secure using a system of points for the characters and their length, these points will be added at the end and this sum will define the security of your password, the levels are: Very Weak, Low , Medium, Strong.

## Install dependencies

For the project to run correctly you must install the project dependencies, you can do it with the following command.

````
pip install -r requirements.txt
````


