huimport random
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



