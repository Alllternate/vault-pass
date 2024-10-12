import os
import sys
import time
import colorama
from cryptography.fernet import Fernet
from cryptography.fernet import MultiFernet  # For future use, to implement multiple keys

# Platform, version, and developer info
platform = sys.platform
version = "Vault Pass 1.0.0"
developer = "Alternate"

# Define options for the menu
option1 = "01"
option2 = "02"
option3 = "03"
option4 = "04"

# Display the developer, platform, and version information with colored text
print(colorama.Fore.LIGHTMAGENTA_EX + platform)
print(colorama.Fore.LIGHTMAGENTA_EX + version)
print(colorama.Fore.LIGHTMAGENTA_EX + developer)

# Function to display ASCII art splash screen
def ascii_splash():
    splash = (colorama.Fore.LIGHTYELLOW_EX + """
____   _________   ____ ___.____  ___________ __________  _____    _________ _________
\\   \\ /   /  _  \\ |    |   \\    | \\__    ___/ \\______   \\/  _  \\  /   _____//   _____/
 \\   Y   /  /_\\  \\|    |   /    |   |    |     |     ___/  /_\\  \\ \\_____  \\ \\_____  \\ 
  \\     /    |    \\    |  /|    |___|    |     |    |  /    |    \\/        \\/        \\ 
   \\___/\\____|__  /______/ |_______ \\____|     |____|  \\____|__  /_______  /_______  / 
                \\/                 \\/                          \\/        \\/        \\/ 
    """)
    print(splash)

# Call the function to display the splash screen
ascii_splash()

# Function to generate and save the Fernet encryption key
def save_key():
    key = Fernet.generate_key()  # Generate the key

    # Save the key to a file named 'key.key'
    with open("key/key.key", "wb") as file:
        file.write(key)

# Function to save encrypted passwords to a file
def save_passwords():
    if not os.path.exists("key/key.key"):  # Check if key exists
        print(colorama.Fore.LIGHTRED_EX + "Please generate a Fernet key.")
        sys.exit()

    # Load the encryption key
    with open("key/key.key", "rb") as file:
        key_file = file.read()

    cipher = Fernet(key_file)  # Initialize the Fernet cipher

    # Get user input for password and name
    password = input(colorama.Fore.LIGHTGREEN_EX + f"Password: {colorama.Fore.LIGHTCYAN_EX}").encode()
    name = input(colorama.Fore.LIGHTGREEN_EX + f"Name: {colorama.Fore.LIGHTCYAN_EX}").encode()

    # Encrypt the password and name
    encrypt_data = cipher.encrypt(password + name)

    # Create the password file if it doesn't exist
    if not os.path.exists("data/passwords.vpef"):
            with open("data/passwords.vpef", "wb"):
                pass

    # Append the encrypted data to the file
    with open("data/passwords.vpef", "ab") as file:
        file.write(encrypt_data + b"\n")

    print(colorama.Fore.LIGHTGREEN_EX + "Password saved successfully.")

# Function to read and decrypt saved passwords from the file
def read_passwords():
    if not os.path.exists("key/key.key"):  # Check if key exists
        print(colorama.Fore.LIGHTRED_EX + "Please generate a Fernet key.")
        sys.exit()

    # Load the encryption key
    with open("key/key.key", "rb") as file:
        key_file = file.read()

    cipher = Fernet(key_file)  # Initialize the Fernet cipher

    # Create the password file if it doesn't exist
    if not os.path.exists("data/passwords.vpef"):
            with open("data/passwords.vpef", "wb"):
                pass

    # Read and decrypt each line (password) in the file
    with open("data/passwords.vpef", "rb") as file:
            for line in file:
                decrypted_data = cipher.decrypt(line.strip())
                print(colorama.Fore.LIGHTGREEN_EX + f"Passwords: {colorama.Fore.LIGHTCYAN_EX}" + decrypted_data.decode())

# Main function to display the menu and handle user input
def main():
    while True:
        # Print menu options with colored text
        print(colorama.Fore.LIGHTMAGENTA_EX + "\nSave passwords and encrypt [01]")
        print(colorama.Fore.LIGHTMAGENTA_EX + "Read encrypted passwords [02]")
        print(colorama.Fore.LIGHTMAGENTA_EX + "Generate Fernet key (Only if it was not generated before) [03]")
        print(colorama.Fore.LIGHTMAGENTA_EX + "Exit [04]")

        # Prompt user for input
        promt = input(colorama.Fore.LIGHTGREEN_EX + f"Select Option: {colorama.Fore.LIGHTCYAN_EX}")

        # Perform action based on user input
        if promt == option1:
            save_passwords()
    
        elif promt == option2:
            read_passwords()

        elif promt == option3:
            save_key()

        elif promt == option4:
            print(colorama.Fore.LIGHTYELLOW_EX + "Exit the program...")
            sys.exit()

# Entry point of the script
if __name__ == "__main__":
    main()
