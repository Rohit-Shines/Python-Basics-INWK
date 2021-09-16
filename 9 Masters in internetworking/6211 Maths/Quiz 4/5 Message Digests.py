# Message Digests
import hashlib
def getDigest(message, algo="MD5"):
    if algo == "MD5":
        m = hashlib.md5()
    elif algo == "SHA1":
        m = hashlib.sha1()
    elif algo == "SHA224":
        m = hashlib.sha224()
    else:
        exit("Select supported algorithm")
    m.update(message)
    return m.hexdigest()

################################ Enter Text ################
print(f"MD5 hash : {getDigest(b'Naarappa')}") # uses MD5
print(f"SHA1 hash : {getDigest(b'Munikanna', 'SHA1')}")
print(f"SHA224 hash : {getDigest(b'Sinnapa', 'SHA224')}")