# Substitution Cipher - Encryption

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 'NQGLKHCOMXAVFJWZTYBDPISURE'
def encryptWithSubstitution(plaintext, key):
    message = plaintext.replace(' ', '').upper()
    ciphertext = [key[ALPHABET.find(c)] for c in message]
    return ''.join(ciphertext)

####################################        Plaintext   ####### Key    ###########
print(f"Ciphertext : {encryptWithSubstitution('hello my world', key)}")