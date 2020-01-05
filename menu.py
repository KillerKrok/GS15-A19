import iWantItAll
import diffie
from hash import hashing


end = False

while end == False:
    choice = input("""\nBonjour ô maître ! Que souhaitez vous faire aujourd’hui ?
->1<- Générer des couples de clés publiques / privées.
->2<- Générer un certificat.
->3<- Vérifier la validité d’un certificat.
->4<- Partager une clé secrète.
->5<- Chiffrer un message.
->6<- Signer un message.
->7<- Vérifier une signature.
->8<- I WANT IT ALL !! I WANT IT NOW !!
->0<- Quitter le programme\n""")

    if int(choice) == 1:
        print("Génération d'une clé publique et d'une clé privée en cours ...\n")
    elif int(choice) == 2:
        print("Génération d'un certificat ...\n")
    elif int(choice) == 3:
        print("Vérification de la validité d'un certificat ...\n")
    elif int(choice) == 4:
        print("Partage d'une clé secrète ...\n")
        diffie.diffie_hellman()
    elif int(choice) == 5:
        print("Chiffrement d'un message ...\n")
    elif int(choice) == 6:
        print("Signature d'un message ...\n")
        chaine = "Hello world"
        #transformation de la chaine en bits
        chaine = ''.join(format(i, 'b') for i in bytearray(chaine, encoding ='utf-8'))
        sign = hashing(chaine, 32, 2)
        print("Signature : " + str(sign) + "\n")
    elif int(choice) == 7:
        print("Vérification d'une signature ...\n")
    elif int(choice) == 8:
        iWantItAll.showItAll()
    elif int(choice) == 0:
        print("Merci d'avoir joué :)")
        end = True
    else:
        print("Votre choix n'est pas valide. Veuillez réessayer.\n\n")
