# Protecting User Password Keys at Rest

## Description

This project aims to develop an authorization application that protects user password keys at rest (on disk). The application encrypts a user-chosen file or directory using AES-256 encryption with a random key, which is then protected by a user passphrase. The project is designed for 5th-8th semester students specializing in system software and security.

## Features

- **File Encryption:** Encrypt a user-chosen file or directory using AES-256 encryption with a random key.
- **Key Protection:** Store the random key in a file protected by a user passphrase.
- **Secure Storage:** Ensure that neither the user passphrase nor the random key is stored in plain text.
- **Authentication and Decryption:** Decrypt the file using the file encryption key upon successful user passphrase authentication.

## Scope

- **Participants:** 5th-8th Semester Students
- **Team Size:** 2 or 3 Member Team
- **Category:** System Software, Security

## Pre-requisites

- Linux File System Operations
- Cryptographic Algorithms
- Programming in any language suited for system software (e.g., C, C++, Python)

## Infrastructure Requirements

- **Hardware:** Any x86 based Desktop or Server with Linux

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/project-name.git
    cd project-name
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Application

To run the application, execute the following command:

```bash
python src/main.py
```

### Encrypting a File

1. Click the "Browse" button to select the file you want to encrypt.
2. Enter a password in the "Password" field.
3. Click the "Encrypt" button.
4. The encrypted file and the key file will be generated. The key file will be saved with a `.key` extension.

### Decrypting a File

1. Click the "Browse" button to select the encrypted file you want to decrypt.
2. Click the "Browse" button next to the "Key File" field to select the corresponding key file.
3. Enter the password you used during the encryption process in the "Password" field.
4. Click the "Decrypt" button.
5. If the decryption is successful, the original file will be restored and the key file will be deleted.

## Project Outputs

1. **Application Workflow:** Detailed workflow of the application.
2. **High-level Algorithm:** Description of the algorithm used.
3. **Cryptographic Algorithm Justification:** Justification for the chosen cryptographic algorithms.
4. **Open Source and System Routines:** Description of open-source tools and system routines used.
5. **Test Plan:** Test plan for various simple and corner cases.
6. **Source Code:** Actual source code with appropriate comments archived in GitHub.

## Learning Outcomes

- Partitioning the high-level problem statement into workflow and smaller independent tasks.
- Understanding different cryptographic algorithms and their usage models.

## Contributors

- Team Member 1 (Role)
- Team Member 2 (Role)
- Team Member 3 (Role)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

### Instructions for Finalizing the README

1. Replace `https://github.com/yourusername/project-name.git` with the actual URL of your GitHub repository.
2. Replace placeholder names in the "Contributors" section with the actual names and roles of the team members.
3. Add the LICENSE file to your repository, if not already included.

Once these steps are completed, your README file will be ready for upload to your GitHub repository.
