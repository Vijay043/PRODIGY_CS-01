def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

message = input("Enter message: ")
shift = int(input("Enter shift: "))

encrypted = caesar_cipher(message, shift)
decrypted = caesar_cipher(encrypted, -shift)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
