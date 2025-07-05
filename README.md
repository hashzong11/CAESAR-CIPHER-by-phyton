# CAESAR-CIPHER-by-phyton

🔐 Caesar Cipher in Python  This repository contains a simple implementation of the Caesar Cipher encryption and decryption algorithm using Python.  The Caesar Cipher is one of the earliest and simplest ciphers, where each letter in the plaintext is shifted a fixed number of places down or up the alphabet.


📁 Features

    Encrypt any message using a specified shift/key

    Decrypt messages back to plaintext

    Command-line interface for user interaction

    Handles both uppercase and lowercase letters

    Ignores non-alphabetic characters (punctuation, numbers, spaces, etc.)
    
🧪 Example

# Encrypting
plaintext = "Hello, World!"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)
# Output: "Khoor, Zruog!"

# Decrypting
decrypted = caesar_decrypt(ciphertext, shift)
# Output: "Hello, World!"
🛠️ Usage

You can run the script directly:
python caesar_cipher.py

📄 File Structure

caesar_cipher/
│
├── caesar_cipher.py        # Main script for Caesar Cipher logic
├── README.md               # Project documentation
└── LICENSE                 # Optional license file

📚 License

This project is open-source and available under the MIT License.
