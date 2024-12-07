"""
Po uruchomieniu powyższego kodu, uzyskasz następujące rezultaty:
    Zadanie 1: Zaszyfrowanie „CRYPTO” kluczem „KEY” → „MVWZXM”
    Zadanie 2: Odszyfrowanie „MVWZXM” kluczem „KEY” → „CRYPTO”
    Zadanie 3: Zaszyfrowanie „HELLO” kluczem „WORLD” → „DSCWR”
    Zadanie 4: Odszyfrowanie „DSCWR” kluczem „WORLD” → „HELLO”
    Zadanie 5: Zaszyfrowanie „ATTACKATDAWN” kluczem „LEMON” → „LXFOPVEFRNHR”
    Zadanie 6: Odszyfrowanie „LXFOPVEFRNHR” kluczem „LEMON” → „ATTACKATDAWN”

Wyjaśnienia:
    Funkcja automatycznie obsługuje zarówno szyfrowanie, jak i odszyfrowywanie w zależności od trybu.
    Klucz jest powtarzany cyklicznie, aby pasował do długości tekstu.
    Działa na literach A-Z i ignoruje różnicę między wielkimi i małymi literami.
"""


def vigenere_cipher(text, key, mode="encrypt"):
    """
    Funkcja do szyfrowania lub odszyfrowywania tekstu za pomocą kryptosystemu Vigenera.

    Args:
        text (str): Tekst do przetworzenia.
        key (str): Klucz szyfrujący.
        mode (str): "encrypt" (szyfruj) lub "decrypt" (odszyfruj).

    Returns:
        str: Wynik przetwarzania (zaszyfrowany lub odszyfrowany tekst).
    """
    result = []
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(k) - ord('A') for k in key]
    text_as_int = [ord(t) - ord('A') for t in text.upper()]

    for i, char in enumerate(text_as_int):
        if mode == "encrypt":
            value = (char + key_as_int[i % key_length]) % 26
        elif mode == "decrypt":
            value = (char - key_as_int[i % key_length]) % 26
        result.append(chr(value + ord('A')))

    return ''.join(result)


# Zadania:
# Zadanie 1: Szyfrowanie tekstu 'CRYPTO' kluczem 'KEY'
tekst_1 = "CRYPTO"
klucz_1 = "KEY"
wynik_1 = vigenere_cipher(tekst_1, klucz_1, mode="encrypt")
print("Zadanie 1:", wynik_1)

# Zadanie 2: Odszyfrowanie tekstu 'MVWZXM' kluczem 'KEY'
tekst_2 = "MVWZXM"
klucz_2 = "KEY"
wynik_2 = vigenere_cipher(tekst_2, klucz_2, mode="decrypt")
print("Zadanie 2:", wynik_2)

# Zadanie 3: Szyfrowanie tekstu 'HELLO' kluczem 'WORLD'
tekst_3 = "HELLO"
klucz_3 = "WORLD"
wynik_3 = vigenere_cipher(tekst_3, klucz_3, mode="encrypt")
print("Zadanie 3:", wynik_3)

# Zadanie 4: Odszyfrowanie tekstu 'DSCWR' kluczem 'WORLD'
tekst_4 = "DSCWR"
klucz_4 = "WORLD"
wynik_4 = vigenere_cipher(tekst_4, klucz_4, mode="decrypt")
print("Zadanie 4:", wynik_4)

# Zadanie 5: Szyfrowanie tekstu 'ATTACKATDAWN' kluczem 'LEMON'
tekst_5 = "ATTACKATDAWN"
klucz_5 = "LEMON"
wynik_5 = vigenere_cipher(tekst_5, klucz_5, mode="encrypt")
print("Zadanie 5:", wynik_5)

# Zadanie 6: Odszyfrowanie tekstu 'LXFOPVEFRNHR' kluczem 'LEMON'
tekst_6 = "LXFOPVEFRNHR"
klucz_6 = "LEMON"
wynik_6 = vigenere_cipher(tekst_6, klucz_6, mode="decrypt")
print("Zadanie 6:", wynik_6)
