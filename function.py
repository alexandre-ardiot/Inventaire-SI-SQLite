import sqlite3
import crud

def creer_compte() -> None:
    """Demande le prénom, nom et mot de passe du compte a creer puis le crée"""

    prenom = input("Quel est votre prénom : ")
    nom = input("Quel est votre nom : ")
    mdp = input("Choisissez un mot de passe : ")

    crud.creation_utilisateur(prenom, nom, mdp)


# Espace utilisateur

def ajouter_pc() -> None :
    """Fonction qui permet d'ajouter un ordinateur"""

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    
    ordinateur_a_ajouter = input ( "Quel ordinateur voulez-vous ajouter : " )
    
