from random import randint


def rabin_miller(n):
    # Test la primalite de n (avance)

    s = n - 1
    d = 0
    while s % 2 == 0:
        # calcul de s et d
        s = s // 2
        d += 1

    for k in list(range(5)):  # test la primalite de n 5 fois
        a = randint(2, n-1)
        v = pow(a, s, n)
        if v != 1:
            i = 0
            while v != (n-1):
                if i == d-1:
                    return False
                else:
                    i = i+1
                    v = (v**2) % n
    return True


def test_primalite(n):
    # Teste la primalite de plusieurs facons

    if (n < 2):
        return False  # gerte 0, 1 et tous les nombres negatifs

    # Test rapide de primalite avec des nombres premiers simples
    premiers_simples = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                        101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
                        223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
                        349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
                        479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
                        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761,
                        769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919,
                        929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if n in premiers_simples:
        return True

    for prime in premiers_simples:
        if (n % prime == 0):
            return False

    # Test de Rabin_Miller si ca echoue
    return rabin_miller(n)

# fonction appelée par un fichier externe


def generation_premier(keysize=512):
    # Cherche un nombre premier
    while True:
        n = randint(1, 2**(keysize))
        if test_primalite(n):
            return n

def generation_petit_premier(keysize=997):
    # Cherche un nombre premier
    while True:
        n = randint(1, keysize)
        if test_primalite(n):
            return n

