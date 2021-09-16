# Caesar Cipher - Decryption
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def decryptWithCaeser(ciphertext, key):
    # Remove spaces from the plaintext and convert to uppercase
    message = ciphertext.replace(' ', '').upper()
    plaintext = ""
    for char in message:
        m_idx = ALPHABET.find(char)
        plaintext += ALPHABET[(m_idx + key) % 26]
    return plaintext

#########################################  PlainText   ####### Key    ###########
print(f"PlainText : {decryptWithCaeser('D', 3)}")