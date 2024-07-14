import string

def ceasar_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def ceasar_decrypt(encrypted_text, shift):
    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def caesar_cipher(text, shift, encrypt=True):
    shift = shift % 26
    mapping = {chr(i): chr((i - ord('a') + shift) % 26 + ord('a')) for i in range(ord('a'), ord('z') + 1)}
    mapping.update({chr(i): chr((i - ord('A') + shift) % 26 + ord('A')) for i in range(ord('A'), ord('Z') + 1)})

    result = ''
    for char in text:
        if char.isalpha():
            result += mapping[char] if encrypt else mapping[char.swapcase()].swapcase()
        else:
            result += char

    return result