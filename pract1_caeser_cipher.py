def caesar(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result


msg = input("Enter message: ")
shift = int(input("Enter shift value: "))
enc = caesar(msg, shift)
dec = caesar(enc, -shift)
print(f"\nOriginal:  {msg}")
print(f"Encrypted: {enc}")
print(f"Decrypted: {dec}")
