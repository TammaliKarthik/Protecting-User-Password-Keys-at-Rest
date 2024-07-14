import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.exceptions import InvalidKey

class FileEncryptorDecryptorApp:
    HEADER = b"FILE_ENCRYPTED"  # Known header for verification

    def __init__(self, root):
        self.root = root
        self.root.title("𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐧𝐠 𝐔𝐬𝐞𝐫 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 𝐊𝐞𝐲𝐬 𝐚𝐭 𝐑𝐞𝐬𝐭 (𝐨𝐧 𝐭𝐡𝐞 𝐃𝐢𝐬𝐤)")
        self.root.geometry("600x300")  # Adjusted height to accommodate "TEAM BETA"
        self.root.configure(bg="black")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.root.columnconfigure(2, weight=1)

        # Labels and Entries
        tk.Label(self.root, text="File:", bg="black", fg="green").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.file_entry = tk.Entry(self.root, width=50, bg="black", fg="green", insertbackground="green")
        self.file_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        tk.Button(self.root, text="Browse", command=self.select_file, bg="green", fg="black", activebackground="dark green").grid(row=0, column=2, padx=10, pady=5)

        tk.Label(self.root, text="Password:", bg="black", fg="green").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(self.root, show='*', width=50, bg="black", fg="green", insertbackground="green")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        tk.Label(self.root, text="Key File:", bg="black", fg="green").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.key_file_entry = tk.Entry(self.root, width=50, bg="black", fg="green", insertbackground="green")
        self.key_file_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        tk.Button(self.root, text="Browse", command=self.select_key_file, bg="green", fg="black", activebackground="dark green").grid(row=2, column=2, padx=10, pady=5)

        # Encrypt and Decrypt Buttons
        tk.Button(self.root, text="Encrypt", command=self.encrypt_action, width=15, bg="green", fg="black", activebackground="dark green").grid(row=3, column=0, padx=10, pady=20, sticky="e")
        tk.Button(self.root, text="Decrypt", command=self.decrypt_action, width=15, bg="White", fg="black", activebackground="dark green").grid(row=3, column=1, padx=10, pady=20, sticky="w")

        # TEAM BETA Label with increased font size
        tk.Label(self.root, text="TEAM BETA", bg="black", fg="white", font=("Helvetica", 16, "bold")).grid(row=8, column=0, columnspan=6, pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)

    def select_key_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.key_file_entry.delete(0, tk.END)
            self.key_file_entry.insert(0, file_path)

    def derive_key(self, password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(password.encode())

    def encrypt_file(self, file_path, password):
        try:
            key = os.urandom(32)

            salt = os.urandom(16)
            key_encryption_key = self.derive_key(password, salt)
            iv_key = os.urandom(16)
            cipher_key = Cipher(algorithms.AES(key_encryption_key), modes.CFB(iv_key), backend=default_backend())
            encryptor_key = cipher_key.encryptor()
            encrypted_key = encryptor_key.update(key) + encryptor_key.finalize()

            key_file_path = file_path + ".key"
            with open(key_file_path, 'wb') as key_file:
                key_file.write(salt + iv_key + encrypted_key)
            print(f"Key file saved to {key_file_path}")

            iv = os.urandom(16)
            with open(file_path, 'rb+') as f:
                plaintext = f.read()

                # Add header before encryption
                data_to_encrypt = self.HEADER + plaintext

                cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
                encryptor = cipher.encryptor()
                ciphertext = encryptor.update(data_to_encrypt) + encryptor.finalize()

                f.seek(0)
                f.write(self.HEADER)
                f.write(iv)
                f.write(ciphertext)
                f.truncate()
            print(f"File encrypted successfully.")

            messagebox.showinfo("Success", f"File encrypted successfully. Key file: {key_file_path}")
        except Exception as e:
            print(f"Encryption failed: {str(e)}")
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt_file(self, file_path, key_file_path, password):
        try:
            print(f"Reading key file: {key_file_path}")
            with open(key_file_path, 'rb') as key_file:
                data = key_file.read()
            salt = data[:16]
            iv_key = data[16:32]
            encrypted_key = data[32:]

            key_encryption_key = self.derive_key(password, salt)
            cipher_key = Cipher(algorithms.AES(key_encryption_key), modes.CFB(iv_key), backend=default_backend())
            decryptor_key = cipher_key.decryptor()
            try:
                key = decryptor_key.update(encrypted_key) + decryptor_key.finalize()
            except InvalidKey:
                raise ValueError("Invalid password or key file.")

            with open(file_path, 'rb+') as f:
                tag = f.read(len(self.HEADER))
                if tag != self.HEADER:
                    raise ValueError("File is not encrypted or incorrect key.")

                iv = f.read(16)
                ciphertext = f.read()

                cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
                decryptor = cipher.decryptor()
                decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

                # Verify header
                if decrypted_data.startswith(self.HEADER):
                    # Remove header
                    decrypted_data = decrypted_data[len(self.HEADER):]

                    f.seek(0)
                    f.write(decrypted_data)
                    f.truncate()
                    print(f"File decrypted successfully.")
                    messagebox.showinfo("Success", "File decrypted successfully.")
                    os.remove(key_file_path)
                    print(f"Key file deleted: {key_file_path}")
                else:
                    raise ValueError("Decryption failed. The file may be corrupted or the password is incorrect.")
        except ValueError as ve:
            print(f"Decryption failed: {str(ve)}")
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            print(f"Decryption failed: {str(e)}")
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def encrypt_action(self):
        file_path = self.file_entry.get()
        password = self.password_entry.get()
        if file_path and password:
            print(f"Encrypting file: {file_path}")
            self.encrypt_file(file_path, password)
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def decrypt_action(self):
        file_path = self.file_entry.get()
        key_file_path = self.key_file_entry.get()
        password = self.password_entry.get()
        if file_path and key_file_path and password:
            try:
                print(f"Decrypting file: {file_path} using key file: {key_file_path}")
                self.decrypt_file(file_path, key_file_path, password)
            except Exception as e:
                print(f"Decryption failed: {str(e)}")
                messagebox.showerror("Error", f"Decryption failed: {str(e)}")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileEncryptorDecryptorApp(root)
    root.mainloop()
