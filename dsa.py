from random import randint
from primeGenerator import generation_premier, generation_petit_premier
from hash import hashing

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
    _signature = None

    # générateur d'un couple clé publique/clé privé 
    def generation_cles(self):
        L = 600# conseillé : 3072
        N = 50# conseillé : 256
        #L = 3072
        #N = 256

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
        while self._h<1 and self._g<1:
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
        """while s1==0:
            s = randint(2, self._q-1)
            s1 = ((self._g**s)%self._privKey)%self._q"""
        s = randint(2, self._q-1)
        s1 = ((self._g**s)%self._privKey)%self._q
        
        #transformation de la chaine en bits
        m = ''.join(format(i, 'b') for i in bytearray(message, encoding ='utf-8'))
        h =  hashing(m, 32, 2)

        return h
