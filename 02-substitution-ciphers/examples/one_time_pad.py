def text_to_numbers(text: str) -> list[int]:
    """
    Kthen tekstin ne lista numrash [0..25].

    Shembull: "ABC" -> [0, 1, 2]
    Vetem shkronjat merren parasysh.
    """
    return [ord(ch.upper()) - ord('A') for ch in text if ch.isalpha()]


def otp_encrypt(plain_text: str, key: str) -> str:
    """
    Enkripton me One-Time Pad.

    Formula:
    C_i = (P_i + K_i) mod 26
    Kerkese kritike: celesi duhet te kete gjatesi te njejte me tekstin.
    """
    plain = text_to_numbers(plain_text)
    key_nums = text_to_numbers(key)

    if len(plain) != len(key_nums):
        raise ValueError("Çelësi duhet të ketë gjatësi të njëjtë me tekstin.")

    cipher_text = ""
    for p, k in zip(plain, key_nums):
        # Per secilen shkronje aplikojme mbledhje modulo 26.
        cipher_text += chr(((p + k) % 26) + ord('A'))

    return cipher_text


def otp_decrypt(cipher_text: str, key: str) -> str:
    """
    Dekripton tekstin e One-Time Pad.

    Formula:
    P_i = (C_i - K_i) mod 26
    """
    cipher = text_to_numbers(cipher_text)
    key_nums = text_to_numbers(key)

    if len(cipher) != len(key_nums):
        raise ValueError("Çelësi duhet të ketë gjatësi të njëjtë me tekstin.")

    plain_text = ""
    for c, k in zip(cipher, key_nums):
        # Ne dekriptim zbritet celesi per secilin indeks.
        plain_text += chr(((c - k) % 26) + ord('A'))

    return plain_text


def main():
    """Ekzekutim interaktiv i shembullit OTP."""
    plain_text = input("Jepni tekstin (vetëm shkronja): ")
    key = input("Jepni çelësin me gjatësi të njëjtë: ")

    cipher_text = otp_encrypt(plain_text, key)
    print("Teksti i enkriptuar:", cipher_text)

    decrypted_text = otp_decrypt(cipher_text, key)
    print("Teksti i dekriptuar:", decrypted_text)


if __name__ == "__main__":
    main()
