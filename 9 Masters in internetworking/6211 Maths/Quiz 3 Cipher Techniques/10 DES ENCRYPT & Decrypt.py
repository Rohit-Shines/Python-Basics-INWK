# DES/3DES Encryption     and decryption
from des import DesKey
def encryptWithDES(plaintext, key):
    handle = DesKey(key)
    return handle.encrypt(plaintext, padding=True)

###################### Des KEY #####################
key_des = b'OhCanada' # 64-bit key
key_3des = b'OhCanadaMyHomeAndNative.'
###################### Des KEY #####################

########################## PLAIN TEXT#######################
cipher1 = encryptWithDES(b'hello world', key_des)
cipher2 = encryptWithDES(b'hello world', key_3des)
########################## PLAIN TEXT#######################


print(f"DES Encryption : { cipher1 }")
print(f"3DES Encryption : { cipher2 }")

############ DECRYPT METHOD #################
def decryptWithDES(ciphertext, key):
    handle = DesKey(key)
    return handle.decrypt(ciphertext, padding=True)

plain1 = decryptWithDES(cipher1, key_des)
plain2 = decryptWithDES(cipher2, key_3des)

print(f"DES Decryption : { plain1 }")
print(f"3DES Decryption : { plain2 }")