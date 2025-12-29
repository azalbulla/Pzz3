class CaesarCipher:
    def __init__(self, shift=3):
        self.shift = shift

    def encrypt(self, text, shift=None):
        if shift is None:
            shift = self.shift

        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26
                result.append(chr(base + shifted))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, text, shift=None):
        if shift is None:
            shift = self.shift
        return self.encrypt(text, -shift)


class AtbashCipher:
    def encrypt(self, text):
        result = []
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result.append(chr(ord('Z') - (ord(char) - ord('A'))))
                else:
                    result.append(chr(ord('z') - (ord(char) - ord('a'))))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, text):
        return self.encrypt(text)
