import iWantItAll
import diffie
from hash import MD5

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
        diffie.diffie_hellman()
    elif int(choice) == 2:
        print("Génération d'un certificat ...\n")
    elif int(choice) == 3:
        print("Vérification de la validité d'un certificat ...\n")
    elif int(choice) == 4:
        print("Partage d'une clé secrète ...\n")
    elif int(choice) == 5:
        print("Chiffrement d'un message ...\n")
    elif int(choice) == 6:
        print("Signature d'un message ...\n")
        signature = MD5()
        signatureHashee = signature.hashhash("moietmoiseul")
        print("Signature : " + str(signatureHashee) + "\n")
    elif int(choice) == 7:
        print("Vérification d'une signature ...\n")
    elif int(choice) == 8:
        iWantItAll.showItAll()
    elif int(choice) == 0:
        print("Merci d'avoir joué :)")
        end = True
    else:
        print("Votre choix n'est pas valide. Veuillez réessayer.\n\n")


