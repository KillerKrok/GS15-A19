import struct
import md5
from enum import Enum
from math import (
    floor,
    sin,
)

from bitarray import bitarray

## fonction de padding des sequences binaires
# chaine = chaine à bourrer
# rate = taille des futurs blocs
def padding(chaine, rate):
    #calcul du nombre de bits à ajouter
    complement = rate-(len(chaine)%rate)
    for i in list(range(complement)):
        chaine.append(0)
    return chaine


## fonction d'extraction d'une partie de la chaine fournie
# chaine = chaine d'origine
# taille = n premiers bits à extraire
def extract(chaine, taille):
    extracted = bitarray()
    extracted = chaine.copy()

    while extracted.length() > taille:
        extracted.pop()

    return extracted

"""-----------------------------------------------------------------"""

## fonction de hashage
# chaine = partie à hasher (en bit)
# taille_bloc = taille des blocs sur lesquels on  travail (r)
# nb_blocs = nombre de blocs de sortie
def hashing(chaine, taille_bloc, nb_blocs):
    chaine = bitarray(chaine)

    # initialisation des variables
    taille_pad = int(taille_bloc * 1.75) # c'est b

    etat = bitarray(taille_pad)
    etat.setall(0)
    etat_r = bitarray(taille_bloc) # etat de 1 à r
    etat_r.setall(0)

    bloc = bitarray()
    blocs = [] #tableau de bittarrays de taille taille_bloc

    sortie = [] # de taille nb_blocs

    # on complète la chaine pour avoir la taille de 1024 bits
    pad_chn = padding(chaine, taille_bloc)
    # découpage en blocs
    k=0
    for l in pad_chn:
        if k==taille_bloc:
            k=0
            blocs.append(bloc)
            bloc = bitarray()

        bloc.append(l)
        k = k+1
    blocs.append(bloc)

    ## absorption
    for i in blocs:
        temp = etat_r^i
        #md5_obj = nmd5.new(temp)
        #etat = md5_obj.digest
        md5_obj = md5.MD5.new(temp)
        etat = md5_obj.getmd5hash()
        etat_r = extract(etat, taille_bloc)

    # essorage
    for j in list(range(nb_blocs)):
        sortie.append(etat_r)
        #md5_obj = nmd5.new(etat)
        #etat = md5_obj.digest
        md5_obj = md5.MD5.new(etat)
        etat = md5_obj.getmd5hash()
        etat_r = extract(etat, taille_bloc)
    
    # retour en hexa
    sortie_hex = bitarray()
    for n in sortie:
        sortie_hex = sortie_hex + n
    return ''.join(["{:02x}".format(byte) for byte in bytearray(sortie_hex)])

