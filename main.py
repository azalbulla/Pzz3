from cipher_classes import CaesarCipher, AtbashCipher


def demo():
    print("Шифр Цезаря:")
    caesar = CaesarCipher(3)
    text = "Hello World"
    encrypted = caesar.encrypt(text)
    decrypted = caesar.decrypt(encrypted)
    print(f"Исходный: {text}")
    print(f"Зашифрованный: {encrypted}")
    print(f"Расшифрованный: {decrypted}")

    print("\nШифр Атбаш:")
    atbash = AtbashCipher()
    encrypted2 = atbash.encrypt(text)
    decrypted2 = atbash.decrypt(encrypted2)
    print(f"Исходный: {text}")
    print(f"Зашифрованный: {encrypted2}")
    print(f"Расшифрованный: {decrypted2}")


if __name__ == "__main__":
    demo()
