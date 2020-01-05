from random import randint
from primeGenerator import generation_premier, generation_petit_premier
from hash import hashing
import bitarray.util

# Sur la base de la page Wikipedia de DSA
class DSA():
    _p = 0
    _q = 0
    _z = 0.5
    _h = 0
    _g = 0
    _y = 0

    _pubKey = None
    _privKey = None

    # générateur d'un couple clé publique/clé privé 
    def generation_cles(self):
        L = 3072
        N = 256

        #définition de p
        #p = generation_premier(L)
        self._p = generation_petit_premier(L)

        #définition de q et z
        while int(self._z) != self._z:
            #q = generation_premier(N)
            self._q = generation_petit_premier(N)
            self._z = (self._p-1)/self._q
        self._z=int(self._z)

        #définition de h et g
        while self._h<1 or self._g<1:
            self._h = randint(2, self._p-2)
            self._g = (self._h**self._z)%self._p

        #définition de x
        self._privKey = randint(1, self._q-1)

        #calcul de y
        self._y = (self._g**self._privKey)%self._p

        self._pubKey = [self._p, self._q, self._g, self._y]


    # générateur de la signature
    def generation_signature(self, message):
        #définition de s
        s=0
        s1=0
        inv_s=0# inverse modulaire de s
        while s1==0 or inv_s==0:
            s = randint(2, self._q-1)
            inv_s = self._mod_inverse(s, self._q)
            s1 = ((self._g**s)%self._privKey)%self._q
        
        #transformation de la chaine en bits
        m = ''.join(format(i, 'b') for i in bytearray(message, encoding ='utf-8'))
        # hashage
        h =  hashing(m, 32, 2)
        # passage en integer
        h = bitarray.util.ba2int(h)
        
        #calcul de s2
        s2 = (h + s1 * self._privKey)*inv_s
        
        # retour de la signature
        return [s1, s2]


    def verif_signature(self, s1, s2, message):
        # si s1 et s2 sont incohérents
        if 0<s1 or s1<self._q or 0<s2 or s2<self._q:
            return False

        else:
            w = self._mod_inverse(s2, self._q)
            #transformation de la chaine en bits
            m = ''.join(format(i, 'b') for i in bytearray(message, encoding ='utf-8'))
            # hashage
            h =  hashing(m, 32, 2)
            # passage en integer
            h = bitarray.util.ba2int(h)
            # calculs de vérification
            u1 = (h*w)%self._q
            u2 = (s1*w)%self._q
            v = ((self._g**u1)*(self._y**u2)%self._p)%self._q

            if v==s1:# signature incorrecte
                return True
            else:
                return False



    # calcul de l'inverse modulaire
    def _mod_inverse(self, x,m):
        for n in range(m):
            if n == m-1:
                return 0
            elif (x * n) % m == 1:
                return n

