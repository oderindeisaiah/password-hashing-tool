# Password Hashing Tool (Python)

A simple authentication system that demonstrates how passwords should
be securely handled using cryptographic hashing instead of plain text.

This project was built to understand core cybersecurity concepts such as
password protection, verification, and secure storage.

---

## 🔐 Features

- Secure password hashing using SHA-256
- Password verification without revealing the original password
- File-based storage for persistence
- Simple authentication flow (setup + login)

---

## 🧠 What I Learned

- Why passwords should never be stored as plain text
- How cryptographic hashing works
- How authentication systems verify users securely
- Basic file handling in Python
- Writing clean and reusable functions

---

## 🛠️ Technologies Used

- Python
- hashlib
- os

---

## 🚀 How It Works

1. First run:
   - User creates a password
   - Password is hashed and saved securely

2. Next runs:
   - User enters password
   - Program compares hash values
   - Access is granted or denied

---

## ⚠️ Security Note

The password file is intentionally excluded from version control
using `.gitignore` to prevent sensitive data exposure.

---

## 📌 Purpose

This project is part of my journey into Python and cybersecurity,
focused on learning real-world security fundamentals.
