# Diffie-Hellman Exchange
import pyDH

def keyExchangeWithDH():
    # Alice and Bob generate Public keys
    alice = pyDH.DiffieHellman()
    bob = pyDH.DiffieHellman()
    alice_pubkey = alice.gen_public_key()
    bob_pubkey = bob.gen_public_key()
    # Alice and Bob exchange key information
    # and create a shared key independently
    return {
        ###### Alice Key ###############################################################
        "Alice": alice.gen_shared_key(bob_pubkey),

        ###### Bob Key ###############################################################
        "Bob": bob.gen_shared_key(alice_pubkey)

            }


keys = keyExchangeWithDH()
print("Alice's Key : " + keys["Alice"])
print("Bob's Key : " + keys["Bob"])
print("Keys match ? " + str(keys["Alice"] == keys["Bob"]))
