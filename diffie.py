from random import randint
from primeGenerator import generation_premier, generation_petit_premier
from hash import hashing
from bitarray import bitarray


def diffie_hellman():
    print("Difiie-Hellman")

    #prime = generation_premier()

    # impossible de passer par le générateur, car l'élévation d'un nombre
    #  à une puissance de 512 bits est trop coûteuse en ressources. 
    # A défaut, utilisation d'un premier plus petit
    prime = generation_petit_premier(1000)

    # génération de la base
    base = generation_petit_premier(prime)

    # choix des secrets
    secret_A = randint(2, prime - 1)
    secret_B = randint(2, prime - 1)

    # calcul y1=a^x1 mod p
    A = (base ** secret_A) % prime

    # calcul y2=a^x2 mod p
    B = (base ** secret_B) % prime

    # calcul y2^x1=K
    secret_Ka = (B ** secret_A) % prime

    # calcul y1^x2=K
    secret_Kb = (A ** secret_B) % prime

    if secret_Ka == secret_Kb:
        # hashage pour avoir une clé de 64 bits
        secret_hash = hashing(bitarray(bin(secret_Kb)[2:]), 32, 2)
        print("clé partagée crée : " + str(secret_hash))
    else:
        print("/!/ échec de la génération de la clé partagée ...")
