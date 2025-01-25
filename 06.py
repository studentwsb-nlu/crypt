"""Hill cipher"""
import numpy as np


def mod_inverse(a, m):
    """Find the modular inverse of a under modulo m using the Extended Euclidean Algorithm."""
    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError(f"{a} has no modular inverse under modulo {m}")
    if t < 0:
        t = t + m
    return t


def hill_encrypt(message, key_matrix):
    """Encrypt the message using the Hill cipher."""
    # Ensure message length is a multiple of the matrix size (2 or 3)
    while len(message) % len(key_matrix) != 0:
        message += 'x'  # Add padding 'x' if necessary

    # Convert the message into numbers (a = 0, b = 1, ..., z = 25)
    message_numbers = [ord(c.lower()) - 97 for c in message]

    # Reshape the message into blocks of the appropriate size (2 or 3)
    message_blocks = [message_numbers[i:i + len(key_matrix)] for i in range(0, len(message_numbers), len(key_matrix))]

    # Encrypt each block
    encrypted_message = []
    for block in message_blocks:
        encrypted_block = np.dot(key_matrix, block) % 26  # Multiply the block by the key matrix and apply mod 26
        encrypted_message.extend(encrypted_block)

    # Convert the encrypted numbers back to letters
    encrypted_message = ''.join(chr(num + 97) for num in encrypted_message)

    return encrypted_message


def hill_decrypt(message, key_matrix):
    """Decrypt the message using the Hill cipher (by finding the inverse of the key matrix)."""
    # Compute the modular inverse of the key matrix modulo 26
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    det_inv = mod_inverse(det, 26)
    key_matrix_inv = np.round(det_inv * np.linalg.inv(key_matrix) * np.linalg.det(key_matrix)) % 26
    key_matrix_inv = key_matrix_inv.astype(int)

    # Ensure message length is a multiple of the matrix size (2 or 3)
    while len(message) % len(key_matrix) != 0:
        message += 'x'  # Add padding 'x' if necessary

    # Convert the message into numbers (a = 0, b = 1, ..., z = 25)
    message_numbers = [ord(c.lower()) - 97 for c in message]

    # Reshape the message into blocks of the appropriate size (2 or 3)
    message_blocks = [message_numbers[i:i + len(key_matrix)] for i in range(0, len(message_numbers), len(key_matrix))]

    # Decrypt each block
    decrypted_message = []
    for block in message_blocks:
        decrypted_block = np.dot(key_matrix_inv, block) % 26  # Multiply by the inverse matrix and apply mod 26
        decrypted_message.extend(decrypted_block)

    # Convert the decrypted numbers back to letters
    decrypted_message = ''.join(chr(num + 97) for num in decrypted_message)

    return decrypted_message


def main():
    # Prompt for matrix size
    matrix_size = int(input("Enter matrix size (2 for 2x2 or 3 for 3x3): "))

    if matrix_size == 2:
        # Get the 2x2 key matrix from the user
        print("Enter a 2x2 matrix key (2 rows with 2 integers each):")
        key_matrix = []
        for i in range(2):
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            key_matrix.append(row)
        key_matrix = np.array(key_matrix)

    elif matrix_size == 3:
        # Get the 3x3 key matrix from the user
        print("Enter a 3x3 matrix key (3 rows with 3 integers each):")
        key_matrix = []
        for i in range(3):
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            key_matrix.append(row)
        key_matrix = np.array(key_matrix)

    else:
        print("Invalid matrix size! Please choose either 2 or 3.")
        return

    # Ask whether to encode or decode
    action = input("Do you want to encode or decode the message? (e/d): ").lower()

    if action == 'e':
        # Get the message to encode
        message = input("Enter the message to encode: ")
        # Encode the message
        encrypted_message = hill_encrypt(message, key_matrix)
        print(f"Encrypted message: {encrypted_message}")

    elif action == 'd':
        # Get the message to decode
        message = input("Enter the message to decode: ")
        # Decode the message
        decrypted_message = hill_decrypt(message, key_matrix)
        print(f"Decrypted message: {decrypted_message}")

    else:
        print("Invalid action. Please choose 'e' for encoding or 'd' for decoding.")


if __name__ == "__main__":
    main()
