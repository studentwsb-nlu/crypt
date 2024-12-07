"""
Funkcje użyte w kodzie:

    is_key_valid(a, n) — sprawdza, czy gcd(a,n)=1gcd(a,n)=1.
    modular_inverse(a, n) — oblicza modularną odwrotność klucza aa, co jest niezbędne do odszyfrowywania.
    affine_encrypt(text, a, b, n) — szyfruje tekst w szyfrze afinicznym.
    affine_decrypt(text, a, b, n) — odszyfrowuje tekst w szyfrze afinicznym.

Przykład 1 (Poprawny klucz):

    a=5,b=8,n=26a=5,b=8,n=26, gdzie gcd(5,26)=1gcd(5,26)=1.
    Zaszyfrowany tekst: HELLO → CZOZZ.
    Odszyfrowany tekst: CZOZZ → HELLO.

Przykład 2 (Niepoprawny klucz):

    a=13,b=8,n=26a=13,b=8,n=26, gdzie gcd(13,26)=13≠1gcd(13,26)=13=1.
    Program generuje błąd i wyświetla komunikat, że aa nie jest odwracalny.

Wynik wykonania kodu:
Przykład 1: Poprawny klucz
Tekst oryginalny: HELLO
Zaszyfrowany: RCLLA
Odszyfrowany: HELLO

Przykład 2: Niepoprawny klucz
Błąd: Klucz 13 nie jest względnie pierwszy z 26.
"""


from math import gcd


def is_key_valid(a, n):
    """
    Sprawdza, czy klucz `a` jest odwracalny (względnie pierwszy z `n`).
    """
    return gcd(a, n) == 1


def modular_inverse(a, n):
    """
    Oblicza modularną odwrotność klucza `a` modulo `n` za pomocą rozszerzonego algorytmu Euklidesa.
    """
    if not is_key_valid(a, n):
        raise ValueError(f"Klucz {a} nie jest odwracalny modulo {n} (gcd({a}, {n}) ≠ 1).")

    # Rozszerzony algorytm Euklidesa
    t, new_t = 0, 1
    r, new_r = n, a

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        raise ValueError(f"Klucz {a} nie ma modularnej odwrotności modulo {n}.")
    if t < 0:
        t += n

    return t


def affine_encrypt(text, a, b, n=26):
    """
    Szyfruje tekst za pomocą szyfru afinicznego z kluczami `a` i `b`.
    """
    if not is_key_valid(a, n):
        raise ValueError(f"Klucz {a} nie jest względnie pierwszy z {n}.")

    text = text.upper()
    encrypted = ''.join(chr(((a * (ord(char) - ord('A')) + b) % n) + ord('A')) for char in text)
    return encrypted


def affine_decrypt(text, a, b, n=26):
    """
    Odszyfrowuje tekst za pomocą szyfru afinicznego z kluczami `a` i `b`.
    """
    if not is_key_valid(a, n):
        raise ValueError(f"Klucz {a} nie jest względnie pierwszy z {n}.")

    a_inv = modular_inverse(a, n)  # Znajdź modularną odwrotność klucza `a`
    text = text.upper()
    decrypted = ''.join(chr(((a_inv * ((ord(char) - ord('A')) - b)) % n) + ord('A')) for char in text)
    return decrypted


# Demonstracja
n = 26  # Rozmiar alfabetu (angielskiego)

# Klucz `a` względnie pierwszy z `n` (poprawny klucz)
print("Przykład 1: Poprawny klucz")
a, b = 5, 8
tekst = "HELLO"
zaszyfrowany = affine_encrypt(tekst, a, b, n)
odszyfrowany = affine_decrypt(zaszyfrowany, a, b, n)
print(f"Tekst oryginalny: {tekst}")
print(f"Zaszyfrowany: {zaszyfrowany}")
print(f"Odszyfrowany: {odszyfrowany}")

# Klucz `a` niewzględnie pierwszy z `n` (niepoprawny klucz)
print("\nPrzykład 2: Niepoprawny klucz")
a, b = 13, 8  # gcd(13, 26) != 1
try:
    zaszyfrowany = affine_encrypt(tekst, a, b, n)
    odszyfrowany = affine_decrypt(zaszyfrowany, a, b, n)
except ValueError as e:
    print(f"Błąd: {e}")
