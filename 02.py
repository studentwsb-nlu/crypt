from math import gcd


def odwrotnosc_modulo(a, m):
    """
    Znajduje odwrotność liczby a modulo m za pomocą rozszerzonego algorytmu Euklidesa.
    Jeśli odwrotność nie istnieje, zwraca None.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def szyfr_afiniczny(text, a, b, tryb="szyfruj"):
    """
    Szyfruje lub odszyfrowuje tekst za pomocą szyfru afinicznego.

    Args:
        text (str): Tekst do przetworzenia.
        a (int): Klucz mnożący (musi być względnie pierwszy z 26).
        b (int): Klucz dodający.
        tryb (str): "szyfruj" lub "odszyfruj".

    Returns:
        str: Zaszyfrowany lub odszyfrowany tekst.
    """
    if gcd(a, 26) != 1:
        raise ValueError("Klucz 'a' musi być względnie pierwszy z 26!")

    wynik = ""
    m = 26
    a_odwrotny = odwrotnosc_modulo(a, m) if tryb == "odszyfruj" else None

    for char in text:
        if char.isalpha():
            x = ord(char.upper()) - ord('A')  # Pozycja litery w alfabecie
            if tryb == "szyfruj":
                y = (a * x + b) % m
            elif tryb == "odszyfruj":
                y = (a_odwrotny * (x - b)) % m
            wynik += chr(y + ord('A'))
        else:
            wynik += char  # Nie zmieniamy innych znaków
    return wynik


# Zadanie 1: Zaszyfrowanie tekstu 'MATH' z kluczem a = 5, b = 8
tekst_1 = "MATH"
a_1, b_1 = 5, 8
wynik_1 = szyfr_afiniczny(tekst_1, a_1, b_1, tryb="szyfruj")
print("Zadanie 1:", wynik_1)

# Zadanie 2: Odszyfrowanie tekstu 'OIVR' z kluczem a = 5, b = 8
tekst_2 = "OIVR"
a_2, b_2 = 5, 8
wynik_2 = szyfr_afiniczny(tekst_2, a_2, b_2, tryb="odszyfruj")
print("Zadanie 2:", wynik_2)

# Zadanie 3: Zaszyfrowanie tekstu 'CODE' z kluczem a = 3, b = 7
tekst_3 = "CODE"
a_3, b_3 = 3, 7
wynik_3 = szyfr_afiniczny(tekst_3, a_3, b_3, tryb="szyfruj")
print("Zadanie 3:", wynik_3)
