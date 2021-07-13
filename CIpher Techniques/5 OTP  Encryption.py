
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encryptWithOTP(plaintext, key):
    key = key.replace(' ', '').upper()
    message = plaintext.replace(' ', '').upper()
    if len(key) < len(message):
        exit("Try longer key")

    ciphertext = ""
    for i in range(len(message)):
        m_idx = ALPHABET.find(message[i])
        k_idx = ALPHABET.find(key[i])
        ciphertext += ALPHABET[(m_idx + k_idx) % 26]
        return ciphertext

####################################  Plaintext   ####### Key    ###########
print(f"Ciphertext : {encryptWithOTP('inwk is good', 'wclnbtdefj')}")