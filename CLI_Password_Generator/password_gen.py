import secrets 
import string
import os
import datetime

if __name__ == "__main__": 
    #Interactive user input
    length = int(input("How many characters? (minimum 8): "))
    while length < 8:
        print("Password must be at least 8 characters long.")
        length = int(input("How many characters? (minimum 8): "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    #Password generation function
    def generate_password(length: int, use_uppercase: bool = True, use_digits: bool = True, use_special_chars: bool = True) -> str:
        """Generates a random password based on the specified criteria."""
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special_chars:
            characters += string.punctuation

        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print(f"Generated password: {password}")

    # Save the generated password to a file with a timestamp
    script_dir = os.path.dirname(os.path.abspath(__file__))
    password_file = os.path.join(script_dir, "passwords.txt")
    with open(password_file, "a") as file:    
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {password}\n")