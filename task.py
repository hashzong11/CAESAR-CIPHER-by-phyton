def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# User Input
print("Welcome to Caesar Cipher Program!")
choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
message = input("Enter your message: ")
shift = int(input("Enter shift value (number): "))

# Process
if choice == 'E':
    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)
elif choice == 'D':
    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)
else:
    print("Invalid choice. Please type 'E' or 'D'.")