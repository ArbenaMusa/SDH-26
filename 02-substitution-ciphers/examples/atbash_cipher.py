def transform(text: str) -> str:
    """
    Transformon tekstin me Atbash Cipher.

    Formula:
    C = 25 - P
    (e njejta formule perdoret edhe per dekriptim).
    Atbash eshte involutive: T(T(x)) = x.
    """
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                # A <-> Z, B <-> Y, ..., duke punuar me indeks 0-25.
                result += chr(ord('Z') - (ord(ch) - ord('A')))
            else:
                result += chr(ord('z') - (ord(ch) - ord('a')))
        else:
            result += ch

    return result


def main():
    """Ekzekutim interaktiv: nje transformim per encrypt, nje i dyte per kthim."""
    plain_text = input("Jepni tekstin: ")
    cipher_text = transform(plain_text)
    print("Teksti i transformuar:", cipher_text)

    original_text = transform(cipher_text)
    print("Teksti i kthyer:", original_text)


if __name__ == "__main__":
    main()
