import sqlite3
import crud
import function

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()


"""
choix_initial = input("Que voulez-vous faire :\n1 - Creer un compte \n2 - Se connecter\n\n")


if choix_initial == "1":
    function.creer_compte()

elif choix_initial == "2":
    print("test")
    
else:
    print("nope")



connexion.commit()
connexion.close()
"""
crud.creation_utilisateur("jr" , "nom" , "abc")