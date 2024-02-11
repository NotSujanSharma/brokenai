from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def generate_key(password: str) -> bytes:
    """
    Generate a key using the provided password.
    """
    password_bytes = password.encode()  # Convert the password to bytes
    salt = os.urandom(16)  # Generate a random salt
    # Use PBKDF2HMAC to generate a key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))  # Generate the key
    return key, salt

def encrypt_message(message: str, password: str) -> bytes:
    """
    Encrypt the message using the generated key.
    """
    key, salt = generate_key(password)  # Generate the key
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())  # Encrypt the message
    return encrypted_message, salt

def decrypt_message(encrypted_message: bytes, password: str, salt: bytes) -> str:
    """
    Decrypt the message using the generated key.
    """
    key = generate_key_with_salt(password, salt)  # Generate the key using the original salt
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()  # Decrypt the message
    return decrypted_message

def generate_key_with_salt(password: str, salt: bytes) -> bytes:
    """
    Generate a key using the provided password and salt.
    """
    password_bytes = password.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    return key

# Example usage
password = "your_password_here"  # Use a strong, secure password
message = "Hello, World!"

# Encrypt the message
encrypted_message, salt = encrypt_message(message, password)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, password, salt)
print(f"Decrypted message: {decrypted_message}")

