import iWantItAll
import diffie
import dsa
import chiffrement

# condition d'arrêt du programme
end = False
# objet contentant notamment la clé publique et la clé privée de l'utilisateur
# (il n'est donc pas possible de posséder plusieurs couples de clés) 
dsa_obj = dsa.DSA()

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
        #si aucun couple de clé n'a déjà été généré
        if(dsa_obj._pubKey == None):
            print("Génération d'une clé publique et d'une clé privée en cours ...\n")
            dsa_obj.generation_cles()
        else:
            print("Clés déjà générées !!")
        print("Les clés générées sont : clé privée = " + str(dsa_obj._privKey) + " ; clé publique = " + str(dsa_obj._pubKey))
    
    elif int(choice) == 2:
        print("Génération d'un certificat ...\n")
        # pas implémenté
    
    elif int(choice) == 3:
        print("Vérification de la validité d'un certificat ...\n")
        # pas implémenté
    
    elif int(choice) == 4:
        print("Partage d'une clé secrète ...\n")
        diffie.diffie_hellman()
    
    elif int(choice) == 5:
        chiffrage = input("""\n Taper ->1<- pour un chiffrement ECB
    Taper ->2<- pour un chiffrement CBC
    Taper ->3<- pour un chiffrement ECB \n""")
        type_message = input("""\n Taper ->1<- pour chiffrer un message
    Taper ->2<- pour chiffrer un fichier \n""")

        chiffrement.camelia(chiffrage, type_message)
        
    elif int(choice) == 6:
        chaine = input("Entrez le message à signer \n")
        #si aucun couple de clé n'a déjà été généré
        if(dsa_obj._pubKey == None):
            print("Génération d'une clé publique et d'une clé privée en cours ...\n")
            dsa_obj.generation_cles()
            print("Les clés générées sont : clé privée = " + str(dsa_obj._privKey) + " ; clé publique = " + str(dsa_obj._pubKey))
        print("Génération de la signature ...")
        sign = dsa_obj.generation_signature(chaine)
        print("Signature du message : " + str(sign) + "\n")
        sign[0] = sign[0]
        sign[1] = sign[1]
        print("Signature en hexadécimal : " + str(sign) + "\n")
    
    elif int(choice) == 7:
        print("Vérification d'une signature ...\n")
        if(dsa_obj._pubKey == None):
            print("/!/ Aucun couple de clé publique et clé privé généré. Ce message n'a pas été adressé par cet utilisateur !")
        else:
            message = input("Entrez le message signé ")
            s1 = input("Entrez la première partie de la signature ")
            s2 = input("Entrez la deuxième partie de la signature ")
            verif = dsa_obj.verif_signature(int(s1), int(s2), message)
            if verif:
                print("Signature correcte !")
            else:
                print("/!/ Signature incorrecte !")
    
    elif int(choice) == 8:
        iWantItAll.showItAll()
        # pas implémenté, mais résulte en une combinaison de tout ce qui est au-dessus
    
    elif int(choice) == 0:
        print("Merci d'avoir joué :)")
        end = True
    
    else:
        print("Votre choix n'est pas valide. Veuillez réessayer.\n")
