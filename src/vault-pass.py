import os
import string
import random
import re
import colorama

# Function to generate a random password of a given length
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to save a password to a file
def save_passwords():
    password = input("Password: ")
    with open("passwords.pw", "a") as file:
        file.write(f"{password}\n")
        print(colorama.Fore.GREEN + "Password saved to passwords.pw")

# Function to read passwords from a file
def read_passwords():
    if os.path.exists("passwords.pw"):
        with open("passwords.pw", "r") as file:
            content = file.read()
            print(colorama.Fore.GREEN + content)
    else:
        print(colorama.Fore.YELLOW + "No passwords saved yet.")

# Function to evaluate the strength of a password
def evaluate_password_strength(password):
    # Check for the presence of uppercase letters, lowercase letters, digits, and special characters
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    strength = 0
    
    # Increment strength for each category of character present
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    
    # Return strength level based on the number of categories present
    if strength == 1:
        return (colorama.Fore.RED + "Low")
    elif strength == 2:
        return (colorama.Fore.YELLOW + "Medium")
    elif strength >= 3:
        return (colorama.Fore.GREEN + "Strong")
    else:
        return (colorama.Fore.RED + "Very Weak")

# Main menu loop
while True:
    # Display menu options
    print(colorama.Fore.WHITE + "\nGenerate password [01]")
    print(colorama.Fore.WHITE + "Save password to a pw file [02]")
    print(colorama.Fore.WHITE + "Read password from a pw file [03]")
    print(colorama.Fore.WHITE + "Check password [04]")
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
        with open("passwords.pw", "a") as file:
            file.write(f"{password}\n")
            print(colorama.Fore.GREEN + "Password saved to passwords.pw")

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
