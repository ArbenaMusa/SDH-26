def vigenere_encrypt(plain_text: str, key: str) -> str:
    """
    Enkripton tekstin me Vigenere Cipher.

    Formula:
    C_i = (P_i + K_i) mod 26
    ku K_i merret nga celesi ne menyre ciklike.
    """
    cipher_text = ""
    # E normalizojme celesin ne uppercase qe llogaritja te jete konsistente.
    key = key.upper()
    # key_index rritet vetem kur hasim shkronja (jo per hapesira/shenja).
    key_index = 0

    for ch in plain_text:
        if ch.isalpha():
            # Kthejme shkronjen e celesit aktual ne vlere 0-25.
            internal_key = ord(key[key_index % len(key)]) - ord('A')

            if ch.isupper():
                # Encrypt per uppercase sipas C = (P + K) mod 26.
                cipher_text += chr((((ord(ch) - ord('A')) + internal_key) % 26) + ord('A'))
            else:
                # Encrypt per lowercase me bazen 'a'.
                cipher_text += chr((((ord(ch) - ord('a')) + internal_key) % 26) + ord('a'))

            # Celesi zhvendoset ne shkronjen tjeter vetem pasi kompletohet shkronja aktuale.
            key_index += 1
        else:
            cipher_text += ch

    return cipher_text


def vigenere_decrypt(cipher_text: str, key: str) -> str:
    """
    Dekripton tekstin e Vigenere.

    Formula:
    P_i = (C_i - K_i) mod 26
    """
    plain_text = ""
    key = key.upper()
    key_index = 0

    for ch in cipher_text:
        if ch.isalpha():
            internal_key = ord(key[key_index % len(key)]) - ord('A')

            if ch.isupper():
                # Ne dekriptim zbritet celesi i brendshem.
                plain_text += chr((((ord(ch) - ord('A')) - internal_key) % 26) + ord('A'))
            else:
                plain_text += chr((((ord(ch) - ord('a')) - internal_key) % 26) + ord('a'))

            key_index += 1
        else:
            plain_text += ch

    return plain_text


def main():
    """Ekzekutim interaktiv per enkriptim dhe dekriptim me Vigenere."""
    plain_text = input("Jepni tekstin që dëshironi të enkriptoni: ")
    key = input("Jepni çelësin: ")

    cipher_text = vigenere_encrypt(plain_text, key)
    print("Teksti i enkriptuar:", cipher_text)

    decrypted_text = vigenere_decrypt(cipher_text, key)
    print("Teksti i dekriptuar:", decrypted_text)


if __name__ == "__main__":
    main()
