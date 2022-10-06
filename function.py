import sqlite3
import crud

def creer_compte() -> None:
    """Demande le prénom, nom et mot de passe du compte a creer puis le crée"""

    prenom = input("Quel est votre prénom : ")
    nom = input("Quel est votre nom : ")
    mdp = input("Choisissez un mot de passe : ")

    crud.creation_utilisateur(prenom, nom, mdp)


# Espace utilisateur

def ajouter_un_ordinateur (id_user , type_ordinateur_id) :
    """ Fonction qui permet d'ajouter un ordinateur """

    
    reference_pc = input ( " Entrez la référence de l'ordinateur que vous voulez ajouter : " )

    crud.ajouter_pc ()

def retirer_un_ordinateur () :
    """ Fonction qui permet de retirer un ordinateur """

    reference_pc = input ( " Entrez la référence de l'ordinateur que vous voulez retirer : ")

    crud.retirer_pc ()

