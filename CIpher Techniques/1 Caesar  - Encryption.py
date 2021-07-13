# Caesar Cipher - Encryption
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def encryptWithCaeser(plaintext, key):
    # Remove spaces from the plaintext and convert to uppercase
    message = plaintext.replace(' ', '').upper()
    ciphertext = ""
    for char in message:
        m_idx = ALPHABET.find(char)
        ciphertext += ALPHABET[(m_idx + key) % 26]
    return ciphertext

#########################################  PlainText   ####### Key    ###########
print(f"Ciphertext : {encryptWithCaeser('ONE IF BY LAND AND TWO IF BY SEA', 3)}")

