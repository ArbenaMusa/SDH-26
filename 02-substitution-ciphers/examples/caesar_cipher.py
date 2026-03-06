def encrypt(plain_text: str, key: int) -> str:
    """
    Enkripton tekstin me Caesar Cipher.

    Formula matematikore:
    C = (P + k) mod 26
    ku P dhe C jane pozitat e shkronjave ne alfabet (A=0, ..., Z=25),
    ndersa k eshte celesi.
    """
    cipher_text = ""

    for ch in plain_text:
        if ch.isalpha():
            if ch.isupper():
                # Per shkronja te medha: kthejme shkronjen ne numer 0-25,
                # aplikojme zhvendosjen me modulo 26, pastaj e kthejme ne shkronje.
                cipher_text += chr((((ord(ch) - ord('A')) + key) % 26) + ord('A'))
            else:
                # E njejta logjike si me siper, por me bazen 'a' per lowercase.
                cipher_text += chr((((ord(ch) - ord('a')) + key) % 26) + ord('a'))
        else:
            # Shenjat qe nuk jane shkronja (hapesira, pike, numra) mbeten njejte.
            cipher_text += ch

    return cipher_text


def decrypt(cipher_text: str, key: int) -> str:
    """
    Dekripton tekstin e enkriptuar me Caesar Cipher.

    Formula matematikore:
    P = (C - k) mod 26
    """
    plain_text = ""

    for ch in cipher_text:
        if ch.isalpha():
            if ch.isupper():
                # Ne dekriptim, celesi zbritet ne vend qe te shtohet.
                plain_text += chr((((ord(ch) - ord('A')) - key) % 26) + ord('A'))
            else:
                plain_text += chr((((ord(ch) - ord('a')) - key) % 26) + ord('a'))
        else:
            plain_text += ch

    return plain_text


def brute_force(cipher_text: str) -> None:
    """
    Provon te gjithe celesat e mundshem (0-25) per te gjetur tekstin origjinal.

    Per Caesar ka vetem 26 kombinime, prandaj brute-force eshte praktik.
    """
    for key in range(26):
        plain_text = decrypt(cipher_text, key)
        print(f"Çelësi: {key:2d} | Teksti: {plain_text}")


def frequency_analysis(cipher_text: str) -> dict:
    """
    Numeron sa here paraqitet secila shkronje ne tekstin e enkriptuar.

    Kjo ndihmon ne sulmet statistikore: shkronja me frekuence te larte
    shpesh korrespondojne me shkronjat me te shpeshta te gjuhes.
    """
    statistics = {}

    for ch in cipher_text:
        if ch.isalpha():
            # Normalizojme ne uppercase qe 'a' dhe 'A' te numerohen bashke.
            upper_ch = ch.upper()
            statistics[upper_ch] = statistics.get(upper_ch, 0) + 1

    return statistics


def main():
    """Ekzekutim interaktiv i shembujve: encrypt/decrypt, brute-force dhe frekuenca."""
    plain_text = input("Jepni tekstin: ")
    key = int(input("Jepni çelësin: "))

    cipher_text = encrypt(plain_text, key)
    print("Teksti i enkriptuar:", cipher_text)

    decrypted_text = decrypt(cipher_text, key)
    print("Teksti i dekriptuar:", decrypted_text)
    
    cipher_text = input("Jepni tekstin e enkriptuar: ")
    brute_force(cipher_text)

    stats = frequency_analysis(cipher_text)

    print("Frekuencat:")
    for letter, count in sorted(stats.items()):
        print(f"{letter}: {count}")


if __name__ == "__main__":
    main()
