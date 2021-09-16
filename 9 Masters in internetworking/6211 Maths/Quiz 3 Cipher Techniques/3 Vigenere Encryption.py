


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encryptWithVignere(plaintext, key):
    # Remove spaces from the plaintext and key and convert to uppercase
    key = key.replace(' ', '').upper()
    message = plaintext.replace(' ', '').upper()
    ciphertext = ""
    for i in range(len(message)):
        m_idx = ALPHABET.find(message[i])
        k_idx = ALPHABET.find(key[i % len(key)])
        ciphertext += ALPHABET[(m_idx + k_idx) % 26]
    return ciphertext

#########################################  PlainText   ####### Key    ###########
print(f"Ciphertext : {encryptWithVignere('cryptography', 'LUCKY')}")
#########################################  PlainText   ####### Key    ###########