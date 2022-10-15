import crud
import function

import os

from time import sleep

#crud.creation_administrateur("a@a.a", "a", "a", "a")


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
                    reponse = input("Que voulez-vous faire ?\nv -> Consulter les tickets ouverts\nc -> Chat\ns -> Statistiques\nd -> Se déconnecter\n")

                    if reponse == "v":
                        #Tout les tickets
                        function.afficher_tickets_admin()
                        sleep(3)

                    elif reponse == "c":
                        #Chat
                        function.clear()
                        function.afficher_tickets_admin()

                        choix_ticket = int(input("Quel ticket souhaitez-vous ouvrir ? : "))
                        
                        function.chat(choix_ticket, utilisateur[3])
                        function.clear()

                    elif reponse == "s":
                        #Statistiques
                        function.clear()
                        prete = crud.nombre_pc_prete()
                        panne = crud.nombre_de_panne()
                        print("Il y a actuellement", prete[0], "PC de prếtés et", panne[0], "panne en cours\n")
                        sleep(3)

                    elif reponse == "d":
                        break

                    else:
                        function.afficher_erreur()

            else:

                #User
                while True:
                    function.afficher_ticket_utilisateur(utilisateur[0])
                    reponse = input("Que voulez-vous faire ?\nt -> Creer un nouveau ticket\nc -> Chat\ng -> Gérer vos PC\nd -> Se déconnecter\n")

                    if reponse == "t":
                        #Création d'un ticket

                        function.clear()

                        print("Voici vos prêts en cours\n")
                        pret = function.afficher_pret(utilisateur[0])

                        choix = int(input("\nSur quel matériel avez-vous un problème ? : "))
                        
                        function.creer_ticket(pret[choix][0])

                    elif reponse == "c":
                        #Chat
                        function.clear()
                        function.afficher_ticket_utilisateur(utilisateur[0])

                        choix_ticket = int(input("Quel ticket souhaitez-vous ouvrir ? : "))
                        
                        function.chat(choix_ticket, utilisateur[3])
                        function.clear()

                    elif reponse == "g":
                        #Gestion des PC
                        function.clear()
                        gestion = input("1 - Ajouter un ordinateur\n2 - Supprimer un ordinateur\n")

                        if gestion == "1":
                            #Ajout ordi
                            function.clear()
                            function.ajouter_pc(utilisateur[0])
                            function.ajouter_info_pc()

                        elif gestion == "2":
                            #Suppresion ordi
                            function.clear()
                            function.retirer_pc(utilisateur[0])

                        else:
                            function.afficher_erreur()

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