# Create Digital Signature with RSA
import rsa
def digitalSignatureWithRSA(message):
    # Alice generates keys and shares her public key
    ###### ################CIPHER MESSAGE KEY ###############################################################
    (pubkey, privkey) = rsa.newkeys(512)
    # Alice creates a hash using 'SHA-1' algorithm then
    # sign the hash with her private key
    signature = rsa.sign(message, privkey, 'SHA-1')
    # Bob receives the message then verify the signature using Alice public key
    verification = rsa.verify(message, signature, pubkey)
    return signature, verification
# Alice creates a message for Bob

#############ORIGINAL MESSAGE ##########################################################
message = b'Kutha Ramp Puttistam'
# Received signature and verification
signature, verification = digitalSignatureWithRSA(message)

print(f"Original message : {message}")
print(f"Signature : {signature}")
print(f"Verified : {verification}")