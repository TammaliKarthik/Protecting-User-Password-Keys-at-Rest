# Protecting-User-Password-Keys-at-Rest
This project focuses on developing a secure application for file encryption, specifically designed to protect user password keys at rest (i.e., when stored on the disk). The application utilizes advanced cryptographic techniques to ensure that user passphrases and encryption keys are securely managed and not stored in plain text.
To prepare your GitHub report for the submission of your project, you'll want to include the following sections, based on the problem statement and project outputs from the document. Here's a detailed guide for structuring your GitHub repository and the report:

### 1. Repository Structure
Create a clear and organized repository structure. Here's a suggested layout:

```
project-name/
│
├── README.md
├── docs/
│   ├── project_description.md
│   ├── algorithm_justification.md
│   ├── test_plan.md
│   └── workflow_diagram.png
├── src/
│   ├── main.py
│   ├── encryption_module.py
│   └── decryption_module.py
├── tests/
│   ├── test_cases.py
│   └── corner_cases.py
├── requirements.txt
└── LICENSE
```

### 2. README.md
This is the first file people will see when they visit your repository. Include the following sections:

- **Project Title**
- **Description**
  - Briefly describe the project and its purpose.
- **Installation**
  - Provide instructions on how to set up the project locally.
- **Usage**
  - Explain how to use the application.
- **Contributors**
  - List the team members and their contributions.
- **License**
  - State the license under which the project is distributed.

### 3. Project Description (docs/project_description.md)
Include the detailed problem statement and scope. Highlight the infrastructure requirements and prerequisites.

### 4. High-Level Algorithm (docs/algorithm_justification.md)
Document the high-level algorithm used for the application, explaining the choice of the encryption method (AES-256) and the key derivation function (KDF).

### 5. Justification for Crypto Algorithms (docs/algorithm_justification.md)
Provide a detailed justification for the chosen cryptographic algorithms and their usage. Explain why AES-256 and the specific KDF were selected.

### 6. Application Workflow (docs/workflow_diagram.png)
Create a diagram representing the workflow of the application. Include steps for encryption, storing the key, user authentication, and decryption.

### 7. Source Code (src/)
Include all source code files with appropriate comments. Ensure your code is well-documented, and each function/module is explained clearly.

### 8. Test Plan (docs/test_plan.md)
Develop a comprehensive test plan. Include tests for:
- Simple cases (basic encryption and decryption)
- Corner cases (unusual or extreme inputs)

### 9. Actual Source Code with Comments (src/)
Ensure all source code is properly commented to explain the logic and flow. Archive the code in this directory.

### 10. Requirements File (requirements.txt)
List all dependencies required to run your project.

### 11. License (LICENSE)
Choose an appropriate open-source license for your project.

### Example of a README.md

```markdown
# Protecting User Password Keys at Rest

## Description
This project aims to develop an application for file encryption, protected by a user passphrase. The application encrypts a user-chosen file or directory using AES-256, stores the random key securely, and decrypts the file upon successful user authentication.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/project-name.git
   ```
2. Navigate to the project directory:
   ```
   cd project-name
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To encrypt a file:
```
python src/main.py encrypt <file_path>
```
To decrypt a file:
```
python src/main.py decrypt <file_path>
```

## Contributors
- Team Member 1 (Role)
- Team Member 2 (Role)
- Team Member 3 (Role)

## License
This project is licensed under the MIT License - see the LICENSE file for details.
```

