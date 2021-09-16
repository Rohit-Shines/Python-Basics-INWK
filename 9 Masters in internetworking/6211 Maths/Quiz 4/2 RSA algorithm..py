# Encryption and Decryption using RSA Algorithm

import rsa

def messageExchangeWithRSA(tx_message):
    # Bob generates keys and shares his public key
    ###### ################CIPHER MESSAGE KEY ###############################################################
    (pubkey, privkey) = rsa.newkeys(330)

    # Alice encrypts a message to Bob with his public key
    ciphertext = rsa.encrypt(tx_message, pubkey)

    # Bob receives the message and decrypts it with his private key
    rx_message = rsa.decrypt(ciphertext, privkey)
    return ciphertext, rx_message

#############ORIGINAL MESSAGE ##########################################################
tx_message = b'NARAPPA - SADKO SINNAPA'

ciphertext, rx_message = messageExchangeWithRSA(tx_message)


print(f"Original message FROM ALICE :): {tx_message}\n")


print(f"Ciphertext GENERATED with RSA KEY : {ciphertext}\n")

#######RECEIVED MESSAGE ##########################################################
print(f"Received message AFTER DECRIPTION : {rx_message}\n")