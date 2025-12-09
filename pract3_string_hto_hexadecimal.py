
import hashlib
from getpass import getpass # getpass()-->lets you take input without showing the characters on the screen.

def sha256_hash(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()       #password.encode("utf-8")Converts the password (string) to bytes.
                                                                      #Hash algorithms only work on bytes, not normal strings.
def main():
    password = getpass("Enter password (typing is hidden): ")
    hex_digest = sha256_hash(password)
    print("SHA-256 (hex):", hex_digest)

if __name__ == "__main__":
    main()