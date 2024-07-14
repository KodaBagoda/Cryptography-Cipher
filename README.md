## Caesar Cipher in Python

This Python project implements a Caesar cipher for encryption and decryption. The Caesar cipher is a classic substitution cipher where each letter in the plaintext is shifted a certain number of positions down the alphabet.

**Features:**

- Encrypts and decrypts text using the Caesar cipher algorithm.
- Handles both uppercase and lowercase letters.
- Preserves non-alphabetic characters (punctuation, spaces, etc.).
- Offers flexibility with two implementation approaches:
  - **Function-based approach (`caesar_encrypt` and `caesar_decrypt`):** Provides a clear breakdown of the encryption and decryption logic.
  - **Dictionary-based approach (`caesar_cipher`):** Enhances efficiency for larger texts using a pre-built mapping dictionary.

**Dependencies:**

This project requires no external libraries and uses only the built-in Python `string` module.

**Usage:**

1. Clone this repository.
2. Open a terminal and navigate to the project directory.
3. Edit the `text` variable in the desired script (`caesar_encrypt.py`, `caesar_decrypt.py`, or `caesar_cipher.py`) with the text you want to encrypt or decrypt.
4. Edit the `shift` variable to specify the number of positions to shift the letters (positive for encryption, negative for decryption).
5. Run the script using `python script_name.py`. The encrypted or decrypted text will be printed to the console.

**Example:**

```
# Encrypting "Hello, world!" with a shift of 3 (function-based approach)
python caesar_encrypt.py

Khoor zruog!

# Decrypting "Khoor zruog!" with a shift of -3 (function-based approach)
python caesar_decrypt.py

Hello, world!

# Efficient encryption using the dictionary-based approach
python caesar_cipher.py
```

**Choosing the Right Script:**

- Use `caesar_encrypt.py` and `caesar_decrypt.py` for better understanding of the encryption/decryption process.
- Use `caesar_cipher.py` for potentially improved efficiency with repeated encryption/decryption or larger texts.

**Contributing:**

Feel free to fork this repository and make improvements! Here are some ideas:

- Implement support for other cipher algorithms (e.g., Vigenere cipher).
- Add a user interface for interactive input and output.
- Allow custom character sets for encryption (beyond the alphabet).

**Security Considerations:**

The Caesar cipher is a very weak encryption method and should not be used for sensitive information. It's easily cracked by brute force or frequency analysis techniques.
