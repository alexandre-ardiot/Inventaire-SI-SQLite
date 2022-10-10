import sqlite3
import crud
import function

<<<<<<< HEAD
connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()


=======
>>>>>>> e00d4e1adb12fed00f0d584e9a6410694144404f
"""
choix_initial = input("Que voulez-vous faire :\n1 - Creer un compte \n2 - Se connecter\n\n")


if choix_initial == "1":
    function.creer_compte()

elif choix_initial == "2":
    print("test")
    
else:
    print("nope")

"""

crud.creation_utilisateur("Antoine", "Meresse", "abc")

<<<<<<< HEAD
connexion.commit()
connexion.close()
"""
crud.creation_utilisateur("jr" , "nom" , "abc")
=======
crud.ajouter_pc ("eefdfjxck", 1 , None)
>>>>>>> e00d4e1adb12fed00f0d584e9a6410694144404f
