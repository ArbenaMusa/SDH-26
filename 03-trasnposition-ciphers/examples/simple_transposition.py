import math


def normalize_text(text: str) -> str:
    """
    Heq vetem hapesirat para enkriptimit/dekriptimit.

    Ne kete shembull didaktik fokusohemi te renditja e karaktereve,
    prandaj hapesirat hiqen qe matrica te lexohet me qarte.
    """
    return text.replace(" ", "")


def transposition_encrypt(plain_text: str, key: int) -> str:
    """
    Enkripton tekstin me simple columnar transposition.

    Ideja:
    1. Teksti vendoset ne matrice rresht pas rreshti.
    2. Ciphertext krijohet duke lexuar kolone pas kolone.
    """
    if key <= 0:
        raise ValueError("Celesi duhet te jete numer pozitiv.")

    normalized_text = normalize_text(plain_text)
    if not normalized_text:
        return ""

    row_count = math.ceil(len(normalized_text) / key)
    matrix = [["" for _ in range(key)] for _ in range(row_count)]
    text_index = 0

    for row in range(row_count):
        for column in range(key):
            if text_index < len(normalized_text):
                # Mbushim matricen nga majtas ne djathtas, rresht pas rreshti.
                matrix[row][column] = normalized_text[text_index]
                text_index += 1

    cipher_text = ""
    for column in range(key):
        for row in range(row_count):
            # Qelizat bosh injorohen kur rreshti i fundit nuk plotesohet i gjithi.
            if matrix[row][column]:
                cipher_text += matrix[row][column]

    return cipher_text


def transposition_decrypt(cipher_text: str, key: int) -> str:
    """
    Dekripton nje ciphertext te krijuar me simple columnar transposition.

    Gjate dekriptimit:
    - llogarisim sa rreshta ka pasur matrica
    - percaktojme sa karaktere i perkasin seciles kolone
    - rindertojme tekstin duke lexuar perseri rresht pas rreshti
    """
    if key <= 0:
        raise ValueError("Celesi duhet te jete numer pozitiv.")

    normalized_text = normalize_text(cipher_text)
    if not normalized_text:
        return ""

    row_count = math.ceil(len(normalized_text) / key)
    remainder = len(normalized_text) % key

    # Nese ka mbetje, vetem kolonat e para kane gjatesi te plote.
    full_columns = remainder if remainder != 0 else key
    column_lengths = [
        row_count if column < full_columns else row_count - 1
        for column in range(key)
    ]

    columns: list[list[str]] = []
    text_index = 0
    for column_length in column_lengths:
        next_index = text_index + column_length
        columns.append(list(normalized_text[text_index:next_index]))
        text_index = next_index

    plain_text = ""
    for row in range(row_count):
        for column in range(key):
            # Leximi rresht pas rreshti e rikthen plaintext-in fillestar.
            if row < len(columns[column]):
                plain_text += columns[column][row]

    return plain_text


def main() -> None:
    """Ekzekutim interaktiv i shembullit simple transposition."""
    plain_text = input("Jepni tekstin per enkriptim: ")
    key = int(input("Jepni celesin (numri i kolonave): "))

    cipher_text = transposition_encrypt(plain_text, key)
    print("Teksti i enkriptuar:", cipher_text)

    generated_plain_text = transposition_decrypt(cipher_text, key)
    print("Teksti i dekriptuar:", generated_plain_text)


if __name__ == "__main__":
    main()
