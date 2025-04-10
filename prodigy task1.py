def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (number): "))

    if choice == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice! Please choose 'E' or 'D'.")

if __name__ == "__main__":
    main()
