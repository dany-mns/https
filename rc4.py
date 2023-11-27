def rc4(key, plaintext):
    # Key Scheduling Algorithm (KSA)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    ciphertext = []
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        ciphertext.append(char ^ k)

    return bytes(ciphertext)

# Example usage
key = b"SecretKey"
plaintext = b"Hello, RC4_128!"

# Encryption
ciphertext = rc4(key, plaintext)
print("Encrypted:", ciphertext)

# Decryption (RC4 is symmetric, so the decryption process is the same as encryption)
decrypted_text = rc4(key, ciphertext)
print("Decrypted:", decrypted_text.decode('utf-8'))
