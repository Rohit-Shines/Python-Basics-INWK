#Vigenere Cipher - Decryption

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def decryptWithVignere(ciphertext, key):
    key = key.replace(' ', '').upper()
    message = ciphertext.replace(' ', '').upper()
    plaintext = ""
    for i in range(len(message)):
        m_idx = ALPHABET.find(message[i])
        k_idx = ALPHABET.find(key[i % len(key)])
        plaintext += ALPHABET[(m_idx - k_idx) % 26]
    return plaintext


#########################################  Cipher Text   ####### Key    ###########
print(f"Plaintext : {decryptWithVignere('cryptography', 'lemon')}")
