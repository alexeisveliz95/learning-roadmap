import secrets 
import string
import os
import datetime
from profiles import load_profile

#Load the default profile settings
profile = load_profile("default")

#Password generation function
def generate_password(profile: dict) -> str:
    """Generates a random password based on the specified criteria."""
    characters = string.ascii_lowercase
    if profile["use_uppercase"]:
        characters += string.ascii_uppercase
    if profile["use_digits"]:
        characters += string.digits
    if profile["use_special_chars"]:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(profile["length"]))
    return password

if __name__ == "__main__":

    #Interactive user input
    """def get_password_length() -> int:
        Prompts the user for the desired password length and validates it.
        while True:
            try:
                length = int(input("How many characters? (minimum 8, maximum 128): "))
                if 8 <= length <= 128:
                    return length
                else:
                    print("Password must be between 8 and 128 characters long.")
            except (ValueError, TypeError):
                exit_input = input("Invalid input. Do you want to exit? (y/n): ").lower()
                if exit_input == 'y':
                    exit()
                print("Invalid input. Please enter a valid number. Try again.")
            
    length = get_password_length()
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'"""

    password = generate_password(profile)
    print(f"Generated password: {password}")

    save = input("Do you want to save the password to a file? (y/n): ").lower() == 'y'
    if save:
        # Save the generated password to a file with a timestamp
        script_dir = os.path.dirname(os.path.abspath(__file__))
        password_file = os.path.join(script_dir, "passwords.txt")
        with open(password_file, "a") as file:    
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - {password}\n")