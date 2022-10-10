import sqlite3
import crud
import function
import os

quitter = False

while not quitter:
    # écran de connexion / inscription

    os.system("clear")
    choix_initial = input("Que voulez-vous faire :\n1 - Se connecter \n2 - Creer un compte\nq - Quitter\n\n")

    if choix_initial == "1":
        utilisateur = function.se_connecter()

        if utilisateur != None:
            if utilisateur[2] == 1:
                #Admin
                while True:
                    pass

            else:
                #User
                while True:
                    function.afficher_accueil_utilisateur()
                    reponse = input("Que voulez-vous faire ?\nc -> Creer un nouveau ticket\nv -> Consulter un ticket\nd -> Se déconnecter")

                    if reponse == "c":
                        #On appelle la fonction de création d'un ticket
                        pass
                    elif reponse == "v":
                        #On appelle la fonction pour lire un ticket
                        pass
                    elif reponse == "d":
                        break
                    else:
                        function.afficher_erreur()

        else:
            function.afficher_erreur()


    elif choix_initial == "2":
        function.creer_compte()

    elif choix_initial =="q":
        quitter = True
        
    else:
        function.afficher_erreur()


"""crud.creation_utilisateur("test@test.fr", "Antoine", "Meresse", "abc")

crud.ajouter_pc ("eefdfjxcw", 3, None)"""