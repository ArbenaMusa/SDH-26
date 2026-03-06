import secrets


def xor_bytes(data: bytes, key: bytes) -> bytes:
    """
    Aplikon XOR byte-per-byte.

    Formula e Vernam OTP:
    C_i = P_i XOR K_i
    P_i = C_i XOR K_i
    """
    if len(data) != len(key):
        raise ValueError("Data dhe celesi duhet te kene te njejten gjatesi ne bytes.")

    return bytes(d ^ k for d, k in zip(data, key))


def generate_random_key(length: int) -> bytes:
    """
    Gjeneron celes rastesor kriptografik me gjatesi fikse (ne bytes).
    Per OTP, celesi duhet te perdoret vetem nje here.
    """
    return secrets.token_bytes(length)


def vernam_encrypt(plain_text: str, key: bytes) -> bytes:
    """
    Enkripton plaintext (UTF-8) me celes bytes duke perdorur XOR.
    """
    plain_bytes = plain_text.encode("utf-8")
    return xor_bytes(plain_bytes, key)


def vernam_decrypt(cipher_bytes: bytes, key: bytes) -> str:
    """
    Dekripton ciphertext bytes me celesin e njejte dhe kthen tekst UTF-8.
    """
    plain_bytes = xor_bytes(cipher_bytes, key)
    return plain_bytes.decode("utf-8")


def main():
    """
    Shembull praktik:
    - merr plaintext
    - gjeneron celes OTP me gjatesi te njejte ne bytes
    - enkripton me XOR
    - dekripton me te njejtin celes
    """
    plain_text = input("Jepni plaintext: ")

    plain_bytes = plain_text.encode("utf-8")
    key = generate_random_key(len(plain_bytes))

    cipher_bytes = vernam_encrypt(plain_text, key)
    decrypted_text = vernam_decrypt(cipher_bytes, key)

    print("Plaintext (UTF-8 bytes):", plain_bytes.hex())
    print("Celesi OTP (hex):", key.hex())
    print("Ciphertext (hex):", cipher_bytes.hex())
    print("Teksti i dekriptuar:", decrypted_text)


if __name__ == "__main__":
    main()
