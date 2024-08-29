import random  # Importing random module for shuffling
import string  # Importing string module for character sets

# Create a list of characters including space, punctuation, digits, and letters
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)  # Convert the string of characters into a list

# Create a copy of the characters list for the key
key = chars.copy()

# Shuffle the key to create a random mapping for encryption
random.shuffle(key)

# Encrypt
plain_text = input("Enter a message to encrypt: ")  # Get user input for the message to encrypt
cipher_text = ""

# Create a dictionary to map each character to its encrypted counterpart
encryption_dict = dict(zip(chars, key))

# Encrypt the plain text using the dictionary
for letter in plain_text:
    cipher_text += encryption_dict[letter]  # Get the encrypted character from the dictionary

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Decrypt
cipher_text = input("Enter a message to decrypt: ")  # Get user input for the message to decrypt
plain_text = ""

# Create a dictionary to map each encrypted character back to its original character
decryption_dict = dict(zip(key, chars))

# Decrypt the cipher text using the dictionary
for letter in cipher_text:
    plain_text += decryption_dict[letter]  # Get the original character from the dictionary

print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
