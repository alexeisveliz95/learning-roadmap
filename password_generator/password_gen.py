import secrets 
import string
import os
import datetime
from profiles import load_profile

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
    # Load the password generation profile
    profile = load_profile("default")
    # Generate the password based on the loaded profile
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