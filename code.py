 import random
 import string 
def generate_password(length, use_upper, use_lower, use_digits, use_symbols): characters = ""

if use_upper:
        characters +=
 string.ascii_uppercase
if use_lower:
        characters +=
 string.ascii_lowercase
if use_digits:
        characters +=
   string.digits
if use_symbols:
        characters +=
  string.punctuation
if characters == "":
        return None
password = ''.join(random.choice(characters) for _ in range(length))
    return password
def check_strength(password):
    strength = 0
if any(c.islower() for c in password):
        strength += 1
if any(c.isupper() for c in password):
        strength += 1
if any(c.isdigit() for c in password):
        strength += 1
if any(c in string.punctuation for c in password):
        strength += 1
if len(password) >= 12:
        strength += 1
if strength <= 2:
        return "Weak"
elif strength == 3:
        return "Medium"
else:
        return "Strong"
def save_to_file(password):
    with open("passwords.txt", "a") as
 file:
        file.write(password + "\n")
    print("Password saved to passwords.txt")
def main():
    while True:
        print("\n===== PASSWORD GENERATOR MENU =====")
        print("1. Generate Password")
        print("2. Exit")
    choice = input("Enter your choice: ")
if choice == "1":
            length = int(input("Enter password length: "))
print("\nSelect character types:")
use_upper = input("Include Uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include Lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include Digits? (y/n): ").lower() == 'y'
use_symbols = input("Include Special Symbols? (y/n): ").lower() == 'y'
password = generate_password(
                length,
                use_upper,
                use_lower,
                use_digits,
                use_symbols
              )

            if password is None:
                print("❌ Error: Select at least one character type.")
               else:
                print("\nGenerated Password:", password)





