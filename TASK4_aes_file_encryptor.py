from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt_file(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    with open(filename + ".enc", 'wb') as f:
        f.write(iv + encrypted)

    print("File encrypted successfully.")

def decrypt_file(filename, key):
    with open(filename, 'rb') as f:
        iv = f.read(16)
        encrypted_data = f.read()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    original = unpadder.update(decrypted) + unpadder.finalize()

    with open(filename.replace(".enc", ""), 'wb') as f:
        f.write(original)

    print("File decrypted successfully.")

choice = input("Choose (E)ncrypt or (D)ecrypt: ").lower()
file_name = input("Enter file name: ")

key = b'12345678901234567890123456789012'  # 32 bytes = AES-256

if choice == 'e':
    encrypt_file(file_name, key)
elif choice == 'd':
    decrypt_file(file_name, key)
else:
    print("Invalid choice")
