def encrypt(plain_text: str, key: int) -> str:
    """
    Enkriptimi me zhvendosje eksponenciale.
    Për pozitën i (duke filluar nga 0), zhvendosja llogaritet si key^i mod 26.
    """
    cipher_text = ""

    for index, ch in enumerate(plain_text):
        if ch.isalpha():
            shift = pow(key, index, 26)

            if ch.isupper():
                cipher_text += chr((((ord(ch) - ord('A')) + shift) % 26) + ord('A'))
            else:
                cipher_text += chr((((ord(ch) - ord('a')) + shift) % 26) + ord('a'))
        else:
            cipher_text += ch

    return cipher_text


def decrypt(cipher_text: str, key: int) -> str:
    plain_text = ""

    for index, ch in enumerate(cipher_text):
        if ch.isalpha():
            shift = pow(key, index, 26)

            if ch.isupper():
                plain_text += chr((((ord(ch) - ord('A')) - shift) % 26) + ord('A'))
            else:
                plain_text += chr((((ord(ch) - ord('a')) - shift) % 26) + ord('a'))
        else:
            plain_text += ch

    return plain_text


def main():
    plain_text = input("Jepni tekstin: ")
    key = int(input("Jepni çelësin bazë: "))

    cipher_text = encrypt(plain_text, key)
    print("Teksti i enkriptuar:", cipher_text)

    decrypted_text = decrypt(cipher_text, key)
    print("Teksti i dekriptuar:", decrypted_text)


if __name__ == "__main__":
    main()
