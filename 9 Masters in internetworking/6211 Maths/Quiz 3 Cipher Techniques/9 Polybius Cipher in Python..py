# Polybius Cipher - Encryption
ALPHABET_NOJ = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # without J
def encryptWithPolybius(plaintext):
    # Convert to uppercase, remove spaces and replace J with I
    message = plaintext.upper().replace(' ', '').replace('J', 'I')
    ciphertext = ""
    for char in message:
        # Find the row and column for each character in the Polybius matrix
        row = ALPHABET_NOJ.find(char) // 5 + 1
        col = ALPHABET_NOJ.find(char) % 5 + 1
        ciphertext += str(row) + str(col)
    return ciphertext


print(f"Ciphertext : {encryptWithPolybius('To Boldly Go Where No One Has Gone Before')}")