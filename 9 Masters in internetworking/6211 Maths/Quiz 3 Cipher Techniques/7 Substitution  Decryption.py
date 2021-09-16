# Substitution Cipher - Decryption
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 'NQGLKHCOMXAVFJWZTYBDPISURE'

def decryptWithSubstitution(ciphertext, key):
    plaintext = [ALPHABET[key.find(c)] for c in ciphertext]
    return ''.join(plaintext)

#########################################  Cipher Text   ####### Key    ###########
print(f"Plaintext : {decryptWithSubstitution('OKVVWFRSWYVL', key)}")