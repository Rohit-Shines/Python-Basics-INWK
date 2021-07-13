# Transposition Cipher - Encryption

def encryptWithTransposition(plaintext, key):
    message = plaintext.replace(' ', '').upper()
    ciphertext = [''] * key
    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext)

####################################        Plaintext   ####### Key    ###########
print(f"Ciphertext : {encryptWithTransposition('GTWALTIHONOOVERDAMESDCKE', 2)}")