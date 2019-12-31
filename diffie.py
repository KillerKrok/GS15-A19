from random import randint
from primeGenerator import generation_premier


def diffie_hellman():
    print("Difiie-Hellman")

    #prime = 23
    prime = generation_premier()

    # génération de la base
    base = randint(1, prime - 1)

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
        print("clé partagée crée : " + str(secret_Kb))
    else :
        print("/!/ échec de la génération de la clé partagée ...")
