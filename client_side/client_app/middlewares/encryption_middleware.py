from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

class EncryptionMiddleware:
    """
    Middleware to handle AES encryption and decryption of text.
    """

    def __init__(self, get_response):
        """
        Initialize the middleware and set up the encryption key.
        """
        self.get_response = get_response
        # Generate a secure key using a password and salt
        self.key = self._generate_key(password=b'thisisthepassword', salt=b'hello')

    def __call__(self, request):
        """
        Process the incoming request and generate a response.
        """
        response = self.get_response(request)
        return response

    def _generate_key(self, password, salt):
        """
        Generate a secure encryption key using PBKDF2.
        
        Args:
            password (bytes): The password used for key derivation.
            salt (bytes): A unique salt to ensure secure key generation.

        Returns:
            bytes: The derived encryption key.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # AES-256 requires a 32-byte key
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(password)

    def encrypt_text(self, plain_text):
        """
        Encrypt the given plain text using AES encryption.

        Args:
            plain_text (str): The text to be encrypted.

        Returns:
            str: The encrypted text, base64-encoded.
        """
        # Generate a random initialization vector (IV)
        iv = os.urandom(16)
        
        # Set up the AES cipher
        cipher = Cipher(
            algorithms.AES(self.key),
            modes.CFB(iv),
            backend=default_backend()
        )
        
        # Perform encryption
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plain_text.encode('utf-8')) + encryptor.finalize()
        
        # Combine IV and ciphertext, then encode in base64
        encrypted_data = base64.b64encode(iv + ciphertext).decode('utf-8')
        return encrypted_data

    def decrypt_text(self, encrypted_text):
        """
        Decrypt the given encrypted text using AES decryption.

        Args:
            encrypted_text (str): The base64-encoded encrypted text.

        Returns:
            str: The decrypted plain text.
        """
        # Decode the base64-encoded input
        encrypted_bytes = base64.b64decode(encrypted_text)
        
        # Extract the IV and ciphertext
        iv = encrypted_bytes[:16]
        ciphertext = encrypted_bytes[16:]
        
        # Set up the AES cipher
        cipher = Cipher(
            algorithms.AES(self.key),
            modes.CFB(iv),
            backend=default_backend()
        )
        
        # Perform decryption
        decryptor = cipher.decryptor()
        plain_text = decryptor.update(ciphertext) + decryptor.finalize()
        
        return plain_text.decode('utf-8')
