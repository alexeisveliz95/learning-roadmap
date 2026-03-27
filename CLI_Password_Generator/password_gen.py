import secrets 
import string

length = 12
use_digits = True
use_special_chars = True
use_uppercase = True

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

