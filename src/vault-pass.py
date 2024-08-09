import os
import string
import random
import re
from cryptography.fernet import Fernet
import colorama

# Initialize colorama
colorama.init()

# Function to generate a random password of a given length
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to generate and save an encryption key (do this once)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the encryption key
def load_key():
    if not os.path.exists("key.key"):
        print(colorama.Fore.RED + "Encryption key file not found. Generating a new key.")
        generate_key()
    return open("key.key", "rb").read()

# Function to create a new user and save credentials encrypted
def create_user():
    if os.path.exists("user.evpf"):
        print(colorama.Fore.YELLOW + "User already exists.")
        return

    username = input("Enter username: ")
    password = input("Enter password: ")
    password_repeat = input("Repeat password: ")

    if password != password_repeat:
        print(colorama.Fore.RED + "Passwords do not match!")
        return

    key = load_key()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())

    with open("user.evpf", "wb") as file:
        file.write(username.encode() + b'\n' + encrypted_password)

    print(colorama.Fore.GREEN + "User created successfully.")

# Function to save a password to an encrypted file
def save_passwords():
    if not os.path.exists("user.evpf"):
        print(colorama.Fore.RED + "No user found. Please create a user first.")
        return

    username = input("Enter username: ")
    password = input("Password: ")
    encrypted_password = encrypt_message(password)
    with open("passwords.evpf", "ab") as file:
        file.write(username.encode() + b',' + encrypted_password + b'\n')
        print(colorama.Fore.GREEN + "Password saved to passwords.pw")

# Function to read passwords from an encrypted file
def read_passwords():
    if not verify_user():
        print(colorama.Fore.RED + "User verification failed.")
        return

    if os.path.exists("passwords.evpf"):
        if os.path.exists("key.key"):
            with open("passwords.evpf", "rb") as file:
                for line in file:
                    parts = line.strip().split(b',', 1)
                    if len(parts) == 2:
                        username, encrypted_password = parts
                        decrypted_password = decrypt_message(encrypted_password)
                        print(colorama.Fore.GREEN + f"Username: {username.decode()}, Password: {decrypted_password}")
                    else:
                        print(colorama.Fore.RED + "Malformed line in passwords.pw")
        else:
            print(colorama.Fore.RED + "Encryption key file is missing.")
    else:
        print(colorama.Fore.YELLOW + "No passwords saved yet.")

# Function to evaluate the strength of a password
def evaluate_password_strength(password):
    min_length = 12  # Define the minimum length for a strong password
    length_score = len(password) / min_length  # Score based on length
    
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    strength = 0
    
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    
    # Increase strength score based on length
    if length_score >= 1:
        strength += 1

    if strength == 1:
        return (colorama.Fore.RED + "Low")
    elif strength == 2:
        return (colorama.Fore.YELLOW + "Medium")
    elif strength >= 3:
        return (colorama.Fore.GREEN + "Strong")
    else:
        return (colorama.Fore.RED + "Very Weak")

# Function to encrypt a message
def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Function to verify user credentials
def verify_user():
    if os.path.exists("user.evpf"):
        with open("user.evpf", "rb") as file:
            username = file.readline().decode().strip()
            encrypted_password = file.readline()

        input_username = input("Enter username: ")
        input_password = input("Enter password: ")

        if input_username == username:
            key = load_key()
            cipher = Fernet(key)
            try:
                decrypted_password = cipher.decrypt(encrypted_password).decode()
                if input_password == decrypted_password:
                    return True
                else:
                    print(colorama.Fore.RED + "Incorrect password.")
            except:
                print(colorama.Fore.RED + "Error decrypting password.")
        else:
            print(colorama.Fore.RED + "Incorrect username.")
    else:
        print(colorama.Fore.YELLOW + "No user file found.")
    return False

# Initial user setup
if not os.path.exists("user.evpf"):
    print(colorama.Fore.YELLOW + "No user found. Please create a user.")
    create_user()

# Main menu loop
while True:
    # Display menu options
    print(colorama.Fore.WHITE + "\nGenerate password [01]")
    print(colorama.Fore.WHITE + "Save password to an encrypted file [02]")
    print(colorama.Fore.WHITE + "Read passwords from an encrypted file [03]")
    print(colorama.Fore.WHITE + "Check password strength [04]")
    print(colorama.Fore.WHITE + "Exit [05]")

    # Get user input for selecting an option
    select = input("Select an option: ")

    # Define option values
    option1 = "01"
    option2 = "02"
    option3 = "03"
    option4 = "04"
    option5 = "05"

    # Execute the selected option
    if select == option1:
        password = generate_password(16)
        print(f"Generated password: {colorama.Fore.GREEN + password}")

    elif select == option2:
        save_passwords()

    elif select == option3:
        read_passwords()

    elif select == option4:
        password = input("Check password: ")
        strength = evaluate_password_strength(password)
        print(f"The password strength level is: {strength}")

    elif select == option5:
        print("Exiting the program...")
        break

    else:
        print(colorama.Fore.RED + "Invalid option selected. Please select a valid option.")
