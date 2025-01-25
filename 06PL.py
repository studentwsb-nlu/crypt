"""Hill cipher PL"""
import numpy as np


def mod_inverse(a, m):
    """Znajdź odwrotność modularną liczby a pod modulo m za pomocą algorytmu rozszerzonego Euklidesa."""
    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError(f"{a} nie ma odwrotności modularnej pod modulo {m}")
    if t < 0:
        t = t + m
    return t


def hill_encrypt(message, key_matrix):
    """Szyfruj wiadomość za pomocą szyfru Hill'a."""
    # Zapewnij, aby długość wiadomości była wielokrotnością rozmiaru macierzy (2 lub 3)
    while len(message) % len(key_matrix) != 0:
        message += 'x'  # Dodaj wypełnienie 'x' jeśli to konieczne

    # Przekształć wiadomość na liczby (a = 0, b = 1, ..., z = 25)
    message_numbers = [ord(c.lower()) - 97 for c in message]

    # Podziel wiadomość na bloki o odpowiednim rozmiarze (2 lub 3)
    message_blocks = [message_numbers[i:i + len(key_matrix)] for i in range(0, len(message_numbers), len(key_matrix))]

    # Szyfruj każdy blok
    encrypted_message = []
    for block in message_blocks:
        encrypted_block = np.dot(key_matrix, block) % 26  # Mnożenie bloku przez macierz klucza i zastosowanie mod 26
        encrypted_message.extend(encrypted_block)

    # Przekształć zaszyfrowane liczby z powrotem na litery
    encrypted_message = ''.join(chr(num + 97) for num in encrypted_message)

    return encrypted_message


def hill_decrypt(message, key_matrix):
    """Deszyfruj wiadomość za pomocą szyfru Hill'a (obliczając odwrotność macierzy klucza)."""
    # Oblicz odwrotność modularną macierzy klucza modulo 26
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    det_inv = mod_inverse(det, 26)  # Oblicz odwrotność wyznacznika
    key_matrix_inv = np.round(det_inv * np.linalg.inv(key_matrix) * np.linalg.det(key_matrix)) % 26
    key_matrix_inv = key_matrix_inv.astype(int)

    # Zapewnij, aby długość wiadomości była wielokrotnością rozmiaru macierzy (2 lub 3)
    while len(message) % len(key_matrix) != 0:
        message += 'x'  # Dodaj wypełnienie 'x' jeśli to konieczne

    # Przekształć wiadomość na liczby (a = 0, b = 1, ..., z = 25)
    message_numbers = [ord(c.lower()) - 97 for c in message]

    # Podziel wiadomość na bloki o odpowiednim rozmiarze (2 lub 3)
    message_blocks = [message_numbers[i:i + len(key_matrix)] for i in range(0, len(message_numbers), len(key_matrix))]

    # Deszyfruj każdy blok
    decrypted_message = []
    for block in message_blocks:
        decrypted_block = np.dot(key_matrix_inv, block) % 26  # Mnożenie przez odwrotną macierz i zastosowanie mod 26
        decrypted_message.extend(decrypted_block)

    # Przekształć odszyfrowane liczby z powrotem na litery
    decrypted_message = ''.join(chr(num + 97) for num in decrypted_message)

    return decrypted_message


def main():
    # Zapytaj o rozmiar macierzy
    matrix_size = int(input("Wprowadź rozmiar macierzy (2 dla 2x2 lub 3 dla 3x3): "))

    if matrix_size == 2:
        # Pobierz macierz 2x2 od użytkownika
        print("Wprowadź macierz 2x2 (2 wiersze po 2 liczby w każdym):")
        key_matrix = []
        for i in range(2):
            row = list(map(int, input(f"Wiersz {i + 1}: ").split()))
            key_matrix.append(row)
        key_matrix = np.array(key_matrix)

    elif matrix_size == 3:
        # Pobierz macierz 3x3 od użytkownika
        print("Wprowadź macierz 3x3 (3 wiersze po 3 liczby w każdym):")
        key_matrix = []
        for i in range(3):
            row = list(map(int, input(f"Wiersz {i + 1}: ").split()))
            key_matrix.append(row)
        key_matrix = np.array(key_matrix)

    else:
        print("Nieprawidłowy rozmiar macierzy! Proszę wybrać 2 lub 3.")
        return

    # Zapytaj, czy użytkownik chce szyfrować czy deszyfrować wiadomość
    action = input("Czy chcesz zaszyfrować czy odszyfrować wiadomość? (e/d): ").lower()

    if action == 'e':
        # Pobierz wiadomość do szyfrowania
        message = input("Wprowadź wiadomość do zaszyfrowania: ")
        # Szyfruj wiadomość
        encrypted_message = hill_encrypt(message, key_matrix)
        print(f"Zaszyfrowana wiadomość: {encrypted_message}")

    elif action == 'd':
        # Pobierz wiadomość do deszyfrowania
        message = input("Wprowadź wiadomość do odszyfrowania: ")
        # Deszyfruj wiadomość
        decrypted_message = hill_decrypt(message, key_matrix)
        print(f"Odszyfrowana wiadomość: {decrypted_message}")

    else:
        print("Nieprawidłowa akcja. Proszę wybrać 'e' do szyfrowania lub 'd' do deszyfrowania.")


if __name__ == "__main__":
    main()
