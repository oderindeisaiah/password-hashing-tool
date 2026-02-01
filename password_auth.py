import hashlib
import os
import getpass
import sys

PASSWORD_FILE = "password.txt"
MAX_ATTEMPTS = 3


def hash_password(password: str) -> str:
    """Return SHA-256 hash of a password."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def save_password(hashed_password: str) -> None:
    """Save hashed password to file."""
    with open(PASSWORD_FILE, "w") as file:
        file.write(hashed_password)


def load_password() -> str:
    """Load hashed password from file."""
    with open(PASSWORD_FILE, "r") as file:
        return file.read().strip()


def setup_password():
    print("=== Initial Setup ===")
    password = getpass.getpass("Create a password: ")
    confirm = getpass.getpass("Confirm password: ")

    if password != confirm:
        print("Passwords do not match. Exiting.")
        sys.exit(1)

    save_password(hash_password(password))
    print("Password saved securely.")


def login():
    print("=== Secure Login ===")
    stored_hash = load_password()

    for attempt in range(1, MAX_ATTEMPTS + 1):
        password = getpass.getpass("Enter password: ")

        if hash_password(password) == stored_hash:
            print("Access granted.")
            return

        remaining = MAX_ATTEMPTS - attempt
        print(f"Incorrect password. Attempts left: {remaining}")

    print("Too many failed attempts. Access locked.")
    sys.exit(1)


def main():
    if not os.path.exists(PASSWORD_FILE):
        setup_password()
    else:
        login()


if __name__ == "__main__":
    main()