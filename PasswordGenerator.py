import random
import string

def generate_password(length=8, include_digits=True, include_special_chars=True):

    """
    Generate a random password.
    Args:
         length (int): Length of the password (default is 8).
         include_digits (bool): Whether to include digits in the password (default is True)
         innclude_special_chars (bool): Whether to include special characters in the password (default is true)

    Returns: 
         str: The generated password.
         """
    
    #define characters set for password (lowercase letters are always included)
    chars = string.ascii_lowercase
    if include_digits:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation

    # Generate the password randomly by selecting characters from character set
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# get user input for password length and complexity preferences
length = int(input("Enter the length of the password: "))
include_digits = input("include digits? (yes/no): ").lower() == "yes"
include_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

# generate password
password = generate_password(length, include_digits, include_special_chars)

# display generated password
print("Generated Password:", password)