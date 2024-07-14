# Protecting User Password Keys at Rest

## Description

This project is an encryption and decryption tool designed to protect user password keys at rest (on disk). The application allows users to encrypt and decrypt files using AES-256 encryption, with the encryption key protected by a user-provided passphrase. The key is stored in a separate file, also encrypted using the passphrase. This ensures that sensitive information remains secure even if the encrypted files are accessed by unauthorized users.

## Features

- **File Encryption:** Encrypt files with AES-256 encryption.
- **Key Protection:** Encrypt the AES encryption key with a user-provided passphrase.
- **Secure Storage:** Store the encrypted key in a separate file.
- **File Decryption:** Decrypt files using the encrypted key and passphrase.
- **GUI Interface:** User-friendly interface for selecting files and entering passphrases.

## Requirements

- Python 3.x
- `tkinter` for GUI
- `cryptography` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://https://github.com/TammaliKarthik/Protecting-User-Password-Keys-at-Rest.git
    cd Protecting-User-Password-Keys-at-Rest
    ```

2. Install the required dependencies:
    ```bash
    pip install cryptography
    pip install tkinter
    ```

## Usage

### Running the Application

To start the application, run the following command:
```bash
python src/main.py
```

### GUI Overview

- **File:** Entry field to select the file to encrypt/decrypt.
- **Password:** Entry field for the user passphrase.
- **Key File:** Entry field to select the key file for decryption.
- **Encrypt Button:** Encrypts the selected file using the provided passphrase.
- **Decrypt Button:** Decrypts the selected file using the provided key file and passphrase.

### Encrypting a File

1. Click the "Browse" button next to the "File" field to select the file you want to encrypt.
2. Enter a secure passphrase in the "Password" field.
3. Click the "Encrypt" button.
4. The application will encrypt the file and create a key file with a `.key` extension in the same directory as the selected file.

### Decrypting a File

1. Click the "Browse" button next to the "File" field to select the encrypted file.
2. Click the "Browse" button next to the "Key File" field to select the corresponding key file.
3. Enter the passphrase used during the encryption process in the "Password" field.
4. Click the "Decrypt" button.
5. If the decryption is successful, the original file will be restored, and the key file will be deleted.

## Learning Outcomes

- Partitioning the high-level problem statement into workflow and smaller independent tasks.
- Understanding different cryptographic algorithms and their usage models.

## Contributors

- Team Member 1 Tammali Karthik(Lead)
- Team Member 2 Maria Punya
- Team Member 3 Alli Gopi

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Detailed Explanation of the Script

The provided script uses the `tkinter` library to create a GUI for encrypting and decrypting files. Here's a breakdown of its components and functionality:

### GUI Components

- **File Entry:** Allows the user to select a file to encrypt or decrypt.
- **Password Entry:** Allows the user to enter a passphrase for encrypting or decrypting the file.
- **Key File Entry:** Allows the user to select the key file used during the decryption process.
- **Encrypt Button:** Triggers the encryption process.
- **Decrypt Button:** Triggers the decryption process.

### Key Derivation

The script uses the `PBKDF2HMAC` function from the `cryptography` library to derive a key from the user-provided passphrase. This derived key is used to encrypt the randomly generated AES key.

### Encryption Process

1. Generate a random 256-bit AES key.
2. Derive a key from the user passphrase using PBKDF2HMAC.
3. Encrypt the AES key with the derived key and store it in a `.key` file along with the salt and IV.
4. Encrypt the selected file with the AES key and store the ciphertext in the original file.

### Decryption Process

1. Read the salt, IV, and encrypted AES key from the `.key` file.
2. Derive the key from the user passphrase using PBKDF2HMAC.
3. Decrypt the AES key with the derived key.
4. Decrypt the selected file with the AES key and restore the original plaintext.

### Error Handling

The script includes error handling to manage various issues, such as invalid passwords, missing files, and decryption failures. It uses `try-except` blocks to catch and display appropriate error messages.

### Security Notes

- **Passphrase Protection:** Ensure the passphrase is strong and not easily guessable.
- **Key File Security:** The key file should be stored securely and deleted after successful decryption.

By following these instructions, you can effectively use the application to secure your files with encryption and protect them with a user passphrase. If you have any further questions or need assistance, please refer to the documentation or contact the project contributors.
