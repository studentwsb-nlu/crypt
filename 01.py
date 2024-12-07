def szyfr_cezara_uniwersalny(text, k, tryb="szyfruj"):
    """
    Szyfruje lub odszyfrowuje tekst za pomocą szyfru Cezara z przesunięciem k.

    Args:
        text (str): Tekst do zaszyfrowania lub odszyfrowania.
        k (int): Liczba oznaczająca przesunięcie.
        tryb (str): "szyfruj" lub "odszyfruj".

    Returns:
        str: Zaszyfrowany lub odszyfrowany tekst.
    """
    if tryb == "odszyfruj":
        k = -k  # Odszyfrowanie to przesunięcie w przeciwnym kierunku
    wynik = ""
    for char in text:
        if char.isalpha():  # Sprawdzamy, czy znak jest literą
            base = ord('A') if char.isupper() else ord('a')
            wynik += chr((ord(char) - base + k) % 26 + base)
        else:
            wynik += char  # Nie zmieniamy innych znaków
    return wynik

# Zadanie 1: Szyfrowanie tekstu 'HELLO' z przesunięciem k = 3
tekst_1 = "HELLO"
k_1 = 3
wynik_1 = szyfr_cezara_uniwersalny(tekst_1, k_1, tryb="szyfruj")
print("Zadanie 1:", wynik_1)

# Zadanie 2: Odszyfrowanie tekstu 'WKHQ' z kluczem k = 3
tekst_2 = "WKHQ"
k_2 = 3
wynik_2 = szyfr_cezara_uniwersalny(tekst_2, k_2, tryb="odszyfruj")
print("Zadanie 2:", wynik_2)

# Zadanie 3: Szyfrowanie tekstu 'CAT' z przesunięciem k = 25
tekst_3 = "CAT"
k_3 = 25
wynik_3 = szyfr_cezara_uniwersalny(tekst_3, k_3, tryb="szyfruj")
print("Zadanie 3:", wynik_3)
