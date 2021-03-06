import numpy as np
import random


MASK8   = 0xff
MASK32  = 0xffffffff
MASK64  = 0xffffffffffffffff
MASK128 = 0xffffffffffffffffffffffffffffffff

Sigma1 = 0xA09E667F3BCC908B
Sigma2 = 0xB67AE8584CAA73B2
Sigma3 = 0xC6EF372FE94F82BE
Sigma4 = 0x54FF53A5F1D36F1C
Sigma5 = 0x10E527FADE682D1D
Sigma6 = 0xB05688C2B3E6C1FD


# fonction pour definir tous les elements du polynome irreductible
def create_Table():

	tableau_polynome = []
	tableau_polynome.append(2**0)
	tableau_polynome.append(2**1)
	tableau_polynome.append(2**2)	
	tableau_polynome.append(2**3)
	tableau_polynome.append(2**4)
	tableau_polynome.append(2**5)
	tableau_polynome.append(2**6)
	tableau_polynome.append(2**7)
	tableau_polynome.append(2**5 + 2**3 + 2**0 + 2**0)
	tableau_polynome.append(2**6 + 2**4 + 2**3 + 2**1)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**2)
	tableau_polynome.append(2**6 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**3 + 2**1)
	tableau_polynome.append(2**5 + 2**4 + 2**3 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**2)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**1 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**4 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**4 + 2**3 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**5 + 2**4 + 2**2 + 2**1)
	tableau_polynome.append(2**6 + 2**5 + 2**3 + 2**2)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**3)
	tableau_polynome.append(2**7 + 2**4 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**4 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**5 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**6 + 2**4 + 2**3 + 2**2)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**3)
	tableau_polynome.append(2**6 + 2**4 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**3 + 2**1)
	tableau_polynome.append(2**6 + 2**4 + 2**3 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**1)
	tableau_polynome.append(2**6 + 2**3 + 2**0)
	tableau_polynome.append(2**7 + 2**4 + 2**1)
	tableau_polynome.append(2**3 + 2**0)
	tableau_polynome.append(2**4 + 2**1)
	tableau_polynome.append(2**5 + 2**2)
	tableau_polynome.append(2**6 + 2**3)
	tableau_polynome.append(2**7 + 2**4)
	tableau_polynome.append(2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**4 + 2**3 + 2**1)
	tableau_polynome.append(2**5 + 2**4 + 2**2)
	tableau_polynome.append(2**6 + 2**5 + 2**3)
	tableau_polynome.append(2**7 + 2**6 + 2**4)
	tableau_polynome.append(2**7 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**5 + 2**4 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**3 + 2**2)
	tableau_polynome.append(2**7 + 2**4 + 2**2 + 2**0)
	tableau_polynome.append(2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**4 + 2**3 + 2**2)
	tableau_polynome.append(2**5 + 2**4 + 2**3)
	tableau_polynome.append(2**6 + 2**5 + 2**4)
	tableau_polynome.append(2**7 + 2**6 + 2**5)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**4 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**2 + 2**1)
	tableau_polynome.append(2**6 + 2**0)
	tableau_polynome.append(2**7 + 2**1)
	tableau_polynome.append(2**5 + 2**3 + 2**0)
	tableau_polynome.append(2**6 + 2**4 + 2**1)
	tableau_polynome.append(2**7 + 2**5 + 2**2)
	tableau_polynome.append(2**6 + 2**5 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**3 + 2**1)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**3 + 2**0)
	tableau_polynome.append(2**6 + 2**4 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**6 + 2**4 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**1)
	tableau_polynome.append(2**6 + 2**5 + 2**3 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**1)
	tableau_polynome.append(2**7 + 2**3 + 2**0)
	tableau_polynome.append(2**5 + 2**4 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**3 + 2**2)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**5 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**3 + 2**2)
	tableau_polynome.append(2**5 + 2**4 + 2**2 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**3 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**2)
	tableau_polynome.append(2**7 + 2**2 + 2**0)
	tableau_polynome.append(2**5 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**4 + 2**3 + 2**2)
	tableau_polynome.append(2**4 + 2**2 + 2**0)
	tableau_polynome.append(2**5 + 2**3 + 2**1)
	tableau_polynome.append(2**6 + 2**4 + 2**2)
	tableau_polynome.append(2**7 + 2**5 + 2**3)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**3 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**3 + 2**0)
	tableau_polynome.append(2**7 + 2**4 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**4 + 2**1 + 2**0)
	tableau_polynome.append(2**5 + 2**2 + 2**1)
	tableau_polynome.append(2**6 + 2**3 + 2**2)
	tableau_polynome.append(2**7 + 2**4 + 2**3)
	tableau_polynome.append(2**4 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**5 + 2**4 + 2**3 + 2**1)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**2)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**3)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**1 + 2**0)
	tableau_polynome.append(2**5 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**4 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**5 + 2**3 + 2**2)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**3 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**3 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**4 + 2**1 + 2**0)
	tableau_polynome.append(2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**4 + 2**2 + 2**1)
	tableau_polynome.append(2**5 + 2**3 + 2**2)
	tableau_polynome.append(2**6 + 2**4 + 2**3)
	tableau_polynome.append(2**7 + 2**5 + 2**4)
	tableau_polynome.append(2**6 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**4 + 2**3 + 2**1)
	tableau_polynome.append(2**4 + 2**3 + 2**0)
	tableau_polynome.append(2**5 + 2**4 + 2**1)
	tableau_polynome.append(2**6 + 2**5 + 2**2)
	tableau_polynome.append(2**7 + 2**6 + 2**3)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**6 + 2**4 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**3 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**5 + 2**4 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**3 + 2**2)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**0)
	tableau_polynome.append(2**5 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**4 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**3 + 2**2)
	tableau_polynome.append(2**6 + 2**4 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**3 + 2**1)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**3 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**3 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**4 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**2 + 2**1)
	tableau_polynome.append(2**6 + 2**5 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**1)
	tableau_polynome.append(2**7 + 2**5 + 2**3 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**3 + 2**2 + 2**11)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**0)
	tableau_polynome.append(2**7 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**5 + 2**4 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**3 + 2**2)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**2 + 2**0)
	tableau_polynome.append(2**6 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**5 + 2**4 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**2)
	tableau_polynome.append(2**7 + 2**5 + 2**2 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**0)
	tableau_polynome.append(2**6 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**4 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**4 + 2**0)
	tableau_polynome.append(2**5 + 2**1)
	tableau_polynome.append(2**6 + 2**2)
	tableau_polynome.append(2**7 + 2**3)
	tableau_polynome.append(2**5 + 2**4 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**3 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**2)
	tableau_polynome.append(2**7 + 2**6 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**5 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**4 + 2**0)
	tableau_polynome.append(2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**4 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**5 + 2**4 + 2**3 + 2**2)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**3)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4)
	tableau_polynome.append(2**7 + 2**6 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**2 + 2**1)
	tableau_polynome.append(2**5 + 2**0)
	tableau_polynome.append(2**6 + 2**1)
	tableau_polynome.append(2**7 + 2**2)
	tableau_polynome.append(2**5 + 2**2 + 2**0)
	tableau_polynome.append(2**6 + 2**3 + 2**1)
	tableau_polynome.append(2**7 + 2**4 + 2**2)
	tableau_polynome.append(2**2 + 2**0)
	tableau_polynome.append(2**3 + 2**1)
	tableau_polynome.append(2**4 + 2**2)
	tableau_polynome.append(2**5 + 2**3)
	tableau_polynome.append(2**6 + 2**4)
	tableau_polynome.append(2**7 + 2**5)
	tableau_polynome.append(2**6 + 2**5 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**3 + 2**1)
	tableau_polynome.append(2**7 + 2**4 + 2**3 + 2**0)
	tableau_polynome.append(2**4 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**5 + 2**4 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**3 + 2**2)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**3)
	tableau_polynome.append(2**7 + 2**6 + 2**4 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**7 + 2**4 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**1 + 2**0)
	tableau_polynome.append(2**2 + 2**1)
	tableau_polynome.append(2**3 + 2**2)
	tableau_polynome.append(2**4 + 2**3)
	tableau_polynome.append(2**5 + 2**4)
	tableau_polynome.append(2**6 + 2**5)
	tableau_polynome.append(2**7 + 2**6)
	tableau_polynome.append(2**7 + 2**5 + 2**3 + 2**2 + 2**0)
	tableau_polynome.append(2**6 + 2**5 + 2**4 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**3 + 2**2 + 2**1)
	tableau_polynome.append(2**7 + 2**6 + 2**5 + 2**4 + 2**0)
	tableau_polynome.append(2**7 + 2**6 + 2**3 + 2**2 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**5 + 2**4 + 2**1 + 2**0)
	tableau_polynome.append(2**6 + 2**3 + 2**1 + 2**0)
	tableau_polynome.append(2**7 + 2**4 + 2**2 + 2**1)
	tableau_polynome.append(2**0)

	return tableau_polynome	

#fonction pour générer une clé de 128 bits
def gen_Key():
	key = random.getrandbits(128)
	return key

#fonction pour décaler à gauche KA ou KL de n bits        
def left_Rotation(cle, n):
        m = n % 128
        i = 0
        kb = cle
        #print("kb vaut : ",kb)
        kc = cle
        #print(kc)
        while i <= m-1:
                #print("i vaut : ",i)
                a = 0b00000001
                #print( "a vaut :", a)
                b = (kc << 1)
                #print( "b vaut :", b)
                b = b & ((2**64)-1)
                #print( "b vaut :", b)
                k = a | b
                kb = k
                kc = k
                #print( "k vaut :", k)
                i = i + 1
        return k



#fonction pour ranger le message en blocs et les chiffrer
def arrange_ECB(message):
        i = 0
        block = []
        while ( i < length):
                if ( i % 16 != 0):
                        block.append(ord(message[i]))
                else:
                        block.append(ord(message[i]))
                        encryption_ECB(block)
                i = i + 1


def arrange_CBC(message):
        i = 0
        block = []
        while ( i < length - 16):
                if ( i % 16 != 0):
                        block.append(ord(message[i]))
                elif (value_CBC == 0):
                        block.append(ord(message[i]))
                        encryption_CBC(block)
                        i = i - 1
                else:
                        block.append(ord(message[i]))
                        encryption_CBC(block)
                i = i + 1
        
def arrange_PCBC(message):
        i = 0
        block = []
        while ( i < length - 16):
                if ( i % 16 != 0):
                        block.append(ord(message[i]))
                elif (value_CBC == 0):
                        block.append(ord(message[i]))
                        encryption_CBC(block)
                        i = i - 1
                else:
                        block.append(ord(message[i]))
                        encryption_PCBC(block)
                i = i + 1       



#on met m au format ASCII et on fait comme dit la RFC
def encryption_ECB(block):

        x0 = block[0]
        x1 = block[1]
        x2 = block[2]
        x3 = block[3]
        x4 = block[4]
        x5 = block[5]
        x6 = block[6]
        x7 = block[7]

        m = x0
        decalage_eight(m)
        m = m + x1
        decalage_eight(m)
        m = m + x2
        decalage_eight(m)
        m = m + x3
        decalage_eight(m)
        m = m + x4
        decalage_eight(m)
        m = m + x5
        decalage_eight(m)
        m = m + x6
        decalage_eight(m)
        m = m + x7

        D1 = m 
        D2 = m & MASK64

        D1 = D1 ^ kw1
        D2 = D2 ^ kw2
        D2 = D2 ^ function_F(D1, k1) #round 1
        D1 = D1 ^ function_F(D2, k2) #round 2
        D2 = D2 ^ function_F(D1, k3) #round 3
        D1 = D1 ^ function_F(D2, k4) #round 4
        D2 = D2 ^ function_F(D1, k5) #round 5
        D1 = D1 ^ function_F(D2, k6) #round 6
        D1 = function_FL(D1, ke1)
        D2 = function_FL_INV(D2, ke2)
        D2 = D2 ^ function_F(D1, k7) #round 7
        D1 = D1 ^ function_F(D2, k8) #round 8
        D1 = D2 ^ function_F(D1, k9) #round 9
        D1 = D1 ^ function_F(D2, k10) #round 10
        D2 = D2 ^ function_F(D1, k11) #round 11
        D1 = D1 ^ function_F(D2, k12) #round 12
        D1 = function_FL(D1, ke3)
        D2 = function_FL_INV(D2, ke4)
        D2 = D2 ^ function_F(D1, k13) #round 13
        D1 = D1 ^ function_F(D2, k14) #round 14
        D2 = D2 ^ function_F(D1, k15) #round 15
        D1 = D1 ^ function_F(D2, k16) #round 16
        D2 = D2 ^ function_F(D1, k17) #round 17
        D1 = D1 ^ function_F(D2, k18) #round 18
        D2 = D2 ^ kw3
        D1 = D1 ^ kw4

        ciphered = (D2 << 64) | D1
        encrypted_data(ciphered)


def arrange_ECB_decryption(message):
        i = 0
        block = []
        while ( i < length):
                if ( i % 16 != 0):
                        block.append(ord(message[i]))
                else:
                        block.append(ord(message[i]))
                        decryption_ECB(block)
                i = i + 1

def decryption_ECB(block):

        x0 = block[0]
        x1 = block[1]
        x2 = block[2]
        x3 = block[3]
        x4 = block[4]
        x5 = block[5]
        x6 = block[6]
        x7 = block[7]
        m = x0
        decalage_eight(m)
        m = m + x1
        decalage_eight(m)
        m = m + x2
        decalage_eight(m)
        m = m + x3
        decalage_eight(m)
        m = m + x4
        decalage_eight(m)
        m = m + x5
        decalage_eight(m)
        m = m + x6
        decalage_eight(m)
        m = m + x7

        D1 = m 
        D2 = m & MASK64

        D1 = D1 ^ kw1d
        D2 = D2 ^ kw2d
        D2 = D2 ^ function_F(D1, k1d) #round 1
        D1 = D1 ^ function_F(D2, k2d) #round 2
        D2 = D2 ^ function_F(D1, k3d) #round 3
        D1 = D1 ^ function_F(D2, k4d) #round 4
        D2 = D2 ^ function_F(D1, k5d) #round 5
        D1 = D1 ^ function_F(D2, k6d) #round 6
        D1 = function_FL(D1, ke1d)
        D2 = function_FL_INV(D2, ke2d)
        D2 = D2 ^ function_F(D1, k7d) #round 7
        D1 = D1 ^ function_F(D2, k8d) #round 8
        D1 = D2 ^ function_F(D1, k9d) #round 9
        D1 = D1 ^ function_F(D2, k10d) #round 10
        D2 = D2 ^ function_F(D1, k11d) #round 11
        D1 = D1 ^ function_F(D2, k12d) #round 12
        D1 = function_FL(D1, ke3d)
        D2 = function_FL_INV(D2, ke4d)
        D2 = D2 ^ function_F(D1, k13d) #round 13
        D1 = D1 ^ function_F(D2, k14d) #round 14
        D2 = D2 ^ function_F(D1, k15d) #round 15
        D1 = D1 ^ function_F(D2, k16d) #round 16
        D2 = D2 ^ function_F(D1, k17d) #round 17
        D1 = D1 ^ function_F(D2, k18d) #round 18
        D2 = D2 ^ kw3d
        D1 = D1 ^ kw4d

        ciphered = (D2 << 64) | D1
        decrypted_data(ciphered)
        

        
        
        
        
        
def encryption_CBC(block):

        if (value_CBC == 0):
                iniatisation_vector = [random.randrange(0, 255, 1) for i in range(16)]
                value_CBC = 1
                x0 = block[0] ^ iniatisation_vector[0]
                x1 = block[1] ^ iniatisation_vector[1]
                x2 = block[2] ^ iniatisation_vector[2]
                x3 = block[3] ^ iniatisation_vector[3]
                x4 = block[4] ^ iniatisation_vector[4]
                x5 = block[5] ^ iniatisation_vector[5]
                x6 = block[6] ^ iniatisation_vector[6]
                x7 = block[7] ^ iniatisation_vector[7]
                
        else:
                x0 = block[0] ^ prec_block_CBC[0]
                x1 = block[1] ^ prec_block_CBC[1]
                x2 = block[2] ^ prec_block_CBC[2]
                x3 = block[3] ^ prec_block_CBC[3]
                x4 = block[4] ^ prec_block_CBC[4]
                x5 = block[5] ^ prec_block_CBC[5]
                x6 = block[6] ^ prec_block_CBC[6]
                x7 = block[7] ^ prec_block_CBC[7]
                
        prec_block_CBC[0] = block[0]
        prec_block_CBC[1] = block[1]
        prec_block_CBC[2] = block[2]
        prec_block_CBC[3] = block[3]
        prec_block_CBC[4] = block[4]
        prec_block_CBC[5] = block[5]
        prec_block_CBC[6] = block[6]
        prec_block_CBC[7] = block[7]

        m = x0
        decalage_eight(m)
        m = m + x1
        decalage_eight(m)
        m = m + x2
        decalage_eight(m)
        m = m + x3
        decalage_eight(m)
        m = m + x4
        decalage_eight(m)
        m = m + x5
        decalage_eight(m)
        m = m + x6
        decalage_eight(m)
        m = m + x7

        D1 = m 
        D2 = m & MASK64

        D1 = D1 ^ kw1
        D2 = D2 ^ kw2
        D2 = D2 ^ function_F(D1, k1) #round 1
        D1 = D1 ^ function_F(D2, k2) #round 2
        D2 = D2 ^ function_F(D1, k3) #round 3
        D1 = D1 ^ function_F(D2, k4) #round 4
        D2 = D2 ^ function_F(D1, k5) #round 5
        D1 = D1 ^ function_F(D2, k6) #round 6
        D1 = function_FL(D1, ke1)
        D2 = function_FL_INV(D2, ke2)
        D2 = D2 ^ function_F(D1, k7) #round 7
        D1 = D1 ^ function_F(D2, k8) #round 8
        D1 = D2 ^ function_F(D1, k9) #round 9
        D1 = D1 ^ function_F(D2, k10) #round 10
        D2 = D2 ^ function_F(D1, k11) #round 11
        D1 = D1 ^ function_F(D2, k12) #round 12
        D1 = function_FL(D1, ke3)
        D2 = function_FL_INV(D2, ke4)
        D2 = D2 ^ function_F(D1, k13) #round 13
        i = 15
        while ( i != 0):
                cipher_to_send = ciphered & ((2**8)-1)
                deciphered_list.append(cipher_to_send)
                ciphered >> 8
                i = i - 1


def camelia(mode, fichier):
        

        if (int(fichier) == 2):
                print("veuillez ecrire le message à chiffrer s'il vous plait : ")
                message = input()
                length = len(message)
                block_Length = 16
                message = padding(message)
                if (int(mode) == 1):
                        arrange_ECB(message)
                        message_ciphered =  ''.join(map(chr, ciphered_list))
                        print("Votre message est chiffré est s'écrit : ", message_ciphered)
                        print("voulez vous le déchiffrer ? y/n")
                        answer = input()
                        if (answer == "y"):
                                arrange_ECB_decryption(message_ciphered)
                                message_deciphered =  ''.join(map(chr, deciphered_list))
                                print("Votre message est déchiffré est s'écrit : ", message_decipheredciphered)
                if (int(mode) == 2):
                        arrange_CBC(message)
                if (int(mode) == 3):
                        arrange_PCBC(message)

        

ciphered_list = []
deciphered_list = []
        
K = gen_Key()

KL = K 
KR = 0
value_CBC = 0
prec_block_CBC = []
prec_block_PCBC = []
        


# 128-bit variables KA and KB generated from KL. D1 and D2 are 64-bit temporary variables.
D1 = (KL ^ KR) >> 64
D2 = (KL ^ KR) & MASK64
D2 = D2 ^ F(D1, Sigma1)
D1 = D1 ^ F(D2, Sigma2)
D1 = D1 ^ (KL >> 64)
D2 = D2 ^ (KL & MASK64)
D2 = D2 ^ F(D1, Sigma3)
D1 = D1 ^ F(D2, Sigma4)
KA = (D1 << 64) | D2
D1 = (KA ^ KR) >> 64
D2 = (KA ^ KR) & MASK64
D2 = D2 ^ F(D1, Sigma5)
D1 = D1 ^ F(D2, Sigma6)
KB = (D1 << 64) | D2
kw1 = KL >> 64
kw2 = KL & MASK64
k1  = KA >> 64
k2  = KA & MASK64
k3  = (left_Rotation(KL, 15)) >> 64
k4  = (left_Rotation(KL, 15)) & MASK64
k5  = (left_Rotation(KA, 15)) >> 64
k6  = (left_Rotation(KA, 15)) & MASK64
ke1 = (left_Rotation(KA, 30)) >> 64
ke2 = (left_Rotation(KA, 30)) & MASK64
k7  = (left_Rotation(KL, 45)) >> 64
k8  = (left_Rotation(KL, 45)) & MASK64
k9  = (left_Rotation(KA, 45)) >> 64
k10 = (left_Rotation(KL, 60)) & MASK64
k11 = (left_Rotation(KA, 60)) >> 64
k12 = (left_Rotation(KA, 60)) & MASK64
ke3 = (left_Rotation(KL, 77)) >> 64
ke4 = (left_Rotation(KL, 77)) & MASK64
k13 = (left_Rotation(KL, 94)) >> 64
k14 = (left_Rotation(KL, 94)) & MASK64
k15 = (left_Rotation(KA, 94)) >> 64
k16 = (left_Rotation(KA, 94)) & MASK64
k17 = (left_Rotation(KL, 111)) >> 64
k18 = (left_Rotation(KL, 111)) & MASK64
kw3 = (left_Rotation(KA, 111)) >> 64
kw4 = (left_Rotation(KA, 111)) & MASK64

#pour décrypter
kw1d = kw3
kw2d = kw4
k1d = k18
k2d = k17
k3d = k16
k4d = k15
k5d = k14
k6d = k13
k7d = k12
k8d = k11
k9d = k10
ke1d = ke4
ke2d = ke3
kw3d = kw1
kw4d = kw2
k18d = k1
k17d = k2
k16d = k3
k15d = k4
k14d = k5
k13d = k6
k12d = k7
k11d = k8
k10d = k9
ke4d = ke1
ke3d = ke2
D1 = D1 ^ function_F(D2, k14) #round 14
D2 = D2 ^ function_F(D1, k15) #round 15
D1 = D1 ^ function_F(D2, k16) #round 16
D2 = D2 ^ function_F(D1, k17) #round 17
D1 = D1 ^ function_F(D2, k18) #round 18
D2 = D2 ^ kw3
D1 = D1 ^ kw4

ciphered = (D2 << 64) | D1
encrypted_data(ciphered)
message_ciphered =  ''.join(map(chr, ciphered_list))
print("Votre message est chiffré est s'écrit : ", message_ciphered)
value_CBC = 0
        

def encryption_PCBC(block):

        if (value_CBC == 0):
                iniatisation_vector = [random.randrange(0, 255, 1) for i in range(16)]
                value_CBC = 1
                x0 = block[0] ^ iniatisation_vector[0]
                x1 = block[1] ^ iniatisation_vector[1]
                x2 = block[2] ^ iniatisation_vector[2]
                x3 = block[3] ^ iniatisation_vector[3]
                x4 = block[4] ^ iniatisation_vector[4]
                x5 = block[5] ^ iniatisation_vector[5]
                x6 = block[6] ^ iniatisation_vector[6]
                x7 = block[7] ^ iniatisation_vector[7]
                
        else:
                x0 = block[0] ^ prec_block_CBC[0]
                x1 = block[1] ^ prec_block_CBC[1]
                x2 = block[2] ^ prec_block_CBC[2]
                x3 = block[3] ^ prec_block_CBC[3]
                x4 = block[4] ^ prec_block_CBC[4]
                x5 = block[5] ^ prec_block_CBC[5]
                x6 = block[6] ^ prec_block_CBC[6]
                x7 = block[7] ^ prec_block_CBC[7]
                
        prec_block_CBC[0] = block[0]
        prec_block_CBC[1] = block[1]
        prec_block_CBC[2] = block[2]
        prec_block_CBC[3] = block[3]
        prec_block_CBC[4] = block[4]
        prec_block_CBC[5] = block[5]
        prec_block_CBC[6] = block[6]
        prec_block_CBC[7] = block[7]

        m = x0
        decalage_eight(m)
        m = m + x1
        decalage_eight(m)
        m = m + x2
        decalage_eight(m)
        m = m + x3
        decalage_eight(m)
        m = m + x4
        decalage_eight(m)
        m = m + x5
        decalage_eight(m)
        m = m + x6
        decalage_eight(m)
        m = m + x7

        D1 = m 
        D2 = m & MASK64

        D1 = D1 ^ kw1
        D2 = D2 ^ kw2
        D2 = D2 ^ function_F(D1, k1) #round 1
        D1 = D1 ^ function_F(D2, k2) #round 2
        D2 = D2 ^ function_F(D1, k3) #round 3
        D1 = D1 ^ function_F(D2, k4) #round 4
        D2 = D2 ^ function_F(D1, k5) #round 5
        D1 = D1 ^ function_F(D2, k6) #round 6
        D1 = function_FL(D1, ke1)
        D2 = function_FL_INV(D2, ke2)
        D2 = D2 ^ function_F(D1, k7) #round 7
        D1 = D1 ^ function_F(D2, k8) #round 8
        D1 = D2 ^ function_F(D1, k9) #round 9
        D1 = D1 ^ function_F(D2, k10) #round 10
        D2 = D2 ^ function_F(D1, k11) #round 11
        D1 = D1 ^ function_F(D2, k12) #round 12
        D1 = function_FL(D1, ke3)
        D2 = function_FL_INV(D2, ke4)
        D2 = D2 ^ function_F(D1, k13) #round 13
        D1 = D1 ^ function_F(D2, k14) #round 14
        D2 = D2 ^ function_F(D1, k15) #round 15
        D1 = D1 ^ function_F(D2, k16) #round 16
        D2 = D2 ^ function_F(D1, k17) #round 17
        D1 = D1 ^ function_F(D2, k18) #round 18
        D2 = D2 ^ kw3
        D1 = D1 ^ kw4

        ciphered = (D2 << 64) | D1
        encrypted_data(ciphered)
        message_ciphered =  ''.join(map(chr, ciphered_list))
        print("Votre message est chiffré est s'écrit : ", message_ciphered)
        value_CBC = 0
        
        #prec_block_PCBC[0] = x0 ^


#fonction F de la RFC de Camélia
def function_F(F_IN, KE):
        x = 0
        x = F_IN ^ KE
        t1 = x >> 56
        t2 = (x >> 48) & MASK8
        t3 = (x >> 40) & MASK8
        t4 = (x >> 32) & MASK8
        t5 = (x >> 24) & MASK8
        t6 = (x >> 16) & MASK8
        t7 = (x >>  8) & MASK8
        t8 = x & MASK8
        t1 = sbox1(t1)
        t2 = sbox2(t2)
        t3 = sbox3(t3)
        t4 = sbox4(t4)
        t5 = sbox5(t5)
        t6 = sbox6(t6)
        t7 = sbox3(t7)
        t8 = sbox8(t8)
        y1 = t1 ^ t3 ^ t4 ^ t6 ^ t7 ^ t8
        y2 = t1 ^ t2 ^ t4 ^ t5 ^ t7 ^ t8
        y3 = t1 ^ t2 ^ t3 ^ t5 ^ t6 ^ t8
        y4 = t2 ^ t3 ^ t4 ^ t5 ^ t6 ^ t7
        y5 = t1 ^ t2 ^ t6 ^ t7 ^ t8
        y6 = t2 ^ t3 ^ t5 ^ t7 ^ t8
        y7 = t3 ^ t4 ^ t5 ^ t6 ^ t8
        y8 = t1 ^ t4 ^ t5 ^ t6 ^ t7
        FL_OUT = (y1 << 56) | (y2 << 48) | (y3 << 40) | (y4 << 32) | (y5 << 24) | (y6 << 16) | (y7 <<  8) | y8
        return FL_OUT


#fonction FL de la RFC de Camélia
def function_FL(FL_IN, KE):
        x1, x2 = 0,0
        k1, k2 = 0,0
        x1 = FL_IN >> 32
        x2 = FL_IN & MASK32
        k1 = KE >> 32
        k2 = KE & MASK32
        x2 = x2 ^ ( left_Rotation(x1 & k1,1))
        x1 = x1 ^ (x2 | k2)
        FL_OUT = (x1 << 32) | x2
        return FL_OUT


# fonction définissant la sbox 1
def sbox1(t):
        t = multiplication(t, 6)
        t = addition(t, 4)
        t = addition(t, 3)
        t = addition(t, 1)
        return t


# fonction définissant la sbox 2
def sbox2(t):
        t = inverse(t)
        return t        


# fonction définissant la sbox 3 et 7
def sbox3(t):
        t = addition(t, 7)
        t = addition(t, 6)
        t = addition(t, 5)
        t = addition(t, 4)
        t = addition(t, 3)
        t = addition(t, 2)
        t = addition(t, 1)
        t = addition(t, 0)
        return t 

# fonction définissant la sbox 4        
def sbox4(t):
        t = addition(t, 6)
        t = addition(t, 4)
        t = addition(t, 2)
        t = addition(t, 0)
        t = multiplication(t, 7)
        t = addition(t, 5)
        t = addition(t, 3)
        t = addition(t, 1)
        return t

# fonction définissant la sbox 5
def sbox5(t):
        t = multiplication(t, 5)
        t = addition(t, 2)
        t = addition(t, 0)
        return t 

# fonction définissant la sbox 6
def sbox6(t):
        t = multiplication(t, 3)
        t = addition(t, 3)
        t = addition(t, 2)
        t = addition(t, 1)
        t = addition(t, 0)
        t = inverse(t)
        return t 

# fonction définissant la sbox 8
def sbox8(t):
        t = addition(t, 7)
        t = addition(t, 5)
        t = addition(t, 3)
        t = addition(t, 1)
        t = multiplcation(t, 6)
        t = addition(t, 4)
        t = addition(t, 2)
        t = addition(t, 0)
        return t 



#fonction pour additioner
def addition(t, degre):
        t ^ (2**degre)
        return t

#fonction pour multiplier t par une puissance du polynôme
def multiplication(t, degre):
        x0, x1, x2, x3, x4, x5, x6, x7, power = 0,0,0,0,0,0,0,0,0
        if (t & 2**7 == 1):
                power = 7 + degre
                x7 = tableau_Polynome[power]

        if (t & 2**6 == 1):
                power = 6 + degre
                x6 = tableau_Polynome[power]

        if (t & 2**5 == 1):
                power = 5 + degre
                x5 = tableau_Polynome[power]

        if (t & 2**4 == 1):
                power = 4 + degre
                x4 = tableau_Polynome[power]

        if (t & 2**3 == 1):
                power = 3 + degre
                x3 = tableau_Polynome[power]

        if (t & 2**2 == 1):
                power = 2 + degre
                x2 = tableau_Polynome[power]

        if (t & 2**1 == 1):
                power = 1 + degre
                x1 = tableau_Polynome[power]

        if (t & 2**0 == 1):
                power = 0 * degre
                x0 = tableau_Polynome[power]

        x = x0 ^ x1 ^ x2 ^ x3 ^ x4 ^ x5 ^ x6 ^ x7

        result = 0
        if (result & 2**7 == 1):
                result = result + 2**7
        if (result & 2**6 == 1):
                result = result + 2**6
        if (result & 2**5 == 1):
                result = result + 2**5
        if (result & 2**4 == 1):
                result = result + 2**4
        if (result & 2**3 == 1):
                result = result + 2**3
        if (result & 2**2 == 1):
                result = result + 2**2
        if (result & 2**1 == 1):
                result = result + 2**1
        if (result & 2**0 == 1):
                result = result + 2**0
        return result

#fonction pour trouver l'inverse de t
def inverse(t):
        inverse = 0
        power = 0
        result = 0
        if (t & 2**7 == 1):
                power = power + 2**7

        if (t & 2**6 == 1):
                power = power + 2**6

        if (t & 2**5 == 1):
                power = power + 2**5

        if (t & 2**4 == 1):
                power = power + 2**4

        if (t & 2**3 == 1):
                power = power + 2**3

        if (t & 2**2 == 1):
                power = power + 2**2

        if (t & 2**1 == 1):
                power = power + 2**1

        if (t & 2**0 == 1):
                power = power + 2**0

        inverse = tableau_Polynome[256 - 1 - power]
        
        if ( inverse & 2**7 == 1):
                result = result + 2**7


        if ( inverse & 2**6 == 1):
                result = result + 2**6


        if ( inverse & 2**5 == 1):
                result = result + 2**5


        if ( inverse & 2**4 == 1):
                result = result + 2**4


        if ( inverse & 2**3 == 1):
                result = result + 2**3


        if ( inverse & 2**2 == 1):
                result = result + 2**2


        if ( inverse & 2**1 == 1):
                result = result + 2**1


        if ( inverse & 2**0 == 1):
                result = result + 2**0
        
        return result

#fonction de padding si la longueur du message ou fichier n'est pas divisible par 16
def padding(message):
        space = length % block_Length
        if ( space != 0):
                add = length + (block_Length - space)
                x = message.ljust(add, '0')
                return x
                
        else:
                print("Aucun besoin de padding n'est requis")
                return message

#fonction pour ajouter cote à cote              
def convert(list): 
      
    # Converting integer list to string list 
    # and joining the list using join() 
    res = int("".join(map(str, list))) 
      
    return res 

#décale de 8 bits à gauche un nombre    
def decalage_eight(m):
        m << 8
        return m

#fonction pour ajouter les données chiffrer dans une liste      
def encrypted_data(ciphered):
        i = 15
        while ( i != 0):
                cipher_to_send = ciphered & ((2**8)-1)
                ciphered_list.append(cipher_to_send)
                ciphered >> 8
                i = i - 1

def decrypted_data(ciphered):
        i = 15
        while ( i != 0):
                cipher_to_send = ciphered & ((2**8)-1)
                deciphered_list.append(cipher_to_send)
                ciphered >> 8
                i = i - 1


def camelia(mode, fichier):
        

        if (int(fichier) == 2):
                print("veuillez ecrire le message à chiffrer s'il vous plait : ")
                message = input()
                length = len(message)
                block_Length = 16
                message = padding(message)
                if (int(mode) == 1):
                        arrange_ECB(message)
                        message_ciphered =  ''.join(map(chr, ciphered_list))
                        print("Votre message est chiffré est s'écrit : ", message_ciphered)
                        print("voulez vous le déchiffrer ? y/n")
                        answer = input()
                        if (answer == "y"):
                                arrange_ECB_decryption(message_ciphered)
                                message_deciphered =  ''.join(map(chr, deciphered_list))
                                print("Votre message est déchiffré est s'écrit : ", message_decipheredciphered)
                if (int(mode) == 2):
                        arrange_CBC(message)
                if (int(mode) == 3):
                        arrange_PCBC(message)

        

ciphered_list = []
deciphered_list = []
        
K = gen_Key()

KL = K 
KR = 0
value_CBC = 0
prec_block_CBC = []
prec_block_PCBC = []
        


# 128-bit variables KA and KB generated from KL. D1 and D2 are 64-bit temporary variables.
D1 = (KL ^ KR) >> 64
D2 = (KL ^ KR) & MASK64
D2 = D2 ^ F(D1, Sigma1)
D1 = D1 ^ F(D2, Sigma2)
D1 = D1 ^ (KL >> 64)
D2 = D2 ^ (KL & MASK64)
D2 = D2 ^ F(D1, Sigma3)
D1 = D1 ^ F(D2, Sigma4)
KA = (D1 << 64) | D2
D1 = (KA ^ KR) >> 64
D2 = (KA ^ KR) & MASK64
D2 = D2 ^ F(D1, Sigma5)
D1 = D1 ^ F(D2, Sigma6)
KB = (D1 << 64) | D2
kw1 = KL >> 64
kw2 = KL & MASK64
k1  = KA >> 64
k2  = KA & MASK64
k3  = (left_Rotation(KL, 15)) >> 64
k4  = (left_Rotation(KL, 15)) & MASK64
k5  = (left_Rotation(KA, 15)) >> 64
k6  = (left_Rotation(KA, 15)) & MASK64
ke1 = (left_Rotation(KA, 30)) >> 64
ke2 = (left_Rotation(KA, 30)) & MASK64
k7  = (left_Rotation(KL, 45)) >> 64
k8  = (left_Rotation(KL, 45)) & MASK64
k9  = (left_Rotation(KA, 45)) >> 64
k10 = (left_Rotation(KL, 60)) & MASK64
k11 = (left_Rotation(KA, 60)) >> 64
k12 = (left_Rotation(KA, 60)) & MASK64
ke3 = (left_Rotation(KL, 77)) >> 64
ke4 = (left_Rotation(KL, 77)) & MASK64
k13 = (left_Rotation(KL, 94)) >> 64
k14 = (left_Rotation(KL, 94)) & MASK64
k15 = (left_Rotation(KA, 94)) >> 64
k16 = (left_Rotation(KA, 94)) & MASK64
k17 = (left_Rotation(KL, 111)) >> 64
k18 = (left_Rotation(KL, 111)) & MASK64
kw3 = (left_Rotation(KA, 111)) >> 64
kw4 = (left_Rotation(KA, 111)) & MASK64

#pour décrypter
kw1d = kw3
kw2d = kw4
k1d = k18
k2d = k17
k3d = k16
k4d = k15
k5d = k14
k6d = k13
k7d = k12
k8d = k11
k9d = k10
ke1d = ke4
ke2d = ke3
kw3d = kw1
kw4d = kw2
k18d = k1
k17d = k2
k16d = k3
k15d = k4
k14d = k5
k13d = k6
k12d = k7
k11d = k8
k10d = k9
ke4d = ke1
ke3d = ke2
