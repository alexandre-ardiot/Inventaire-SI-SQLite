from email import message
import sqlite3
import crud

def creer_compte() -> None:
    """Demande le prénom, nom et mot de passe du compte a creer puis le crée"""

    prenom = input("Quel est votre prénom : ")
    nom = input("Quel est votre nom : ")
    mdp = input("Choisissez un mot de passe : ")

    crud.creation_utilisateur(prenom, nom, mdp)

def creer_type_pc ():
    """ Fonction qui permet d'ajouter des ordinateur dans la base de donnée type_ordinateur"""
    
    marque = input(" Entrez la marque de l'ordinateur : ")
    processeur = input (" Entrez le processeur de l'ordinateur : " )
    carte_graphique = input (" Entrez la carte graphique de l'ordinateur : " )
    ram = input (" Entrez la ram de l'ordinateur : " )
    disque = input (" Entrez le disque de l'ordinateur : " )

    crud.creer_type_pc ( marque, processeur, carte_graphique, ram, disque)

def se_connecter () :
    """ Fonction qui permet de s'identifier """

    email = input ( " Quelle est votre e_mail : ")
    mdp = input ( " Quel est votre mot de passe : ")

    crud.vérifier_utilisateur (email , mdp )


# Espace utilisateur

def ajouter_un_ordinateur (id_user , type_ordinateur_id) :
    """ Fonction qui permet d'ajouter un ordinateur """

    reference_pc = input ( " Entrez la référence de l'ordinateur que vous voulez ajouter : " )

    crud.ajouter_pc (id_user , type_ordinateur_id)


def retirer_un_ordinateur () :
    """ Fonction qui permet de retirer un ordinateur """

    reference_pc = input ( " Entrez la référence de l'ordinateur que vous voulez retirer : ")

    crud.retirer_pc (reference_pc)


def creer_rapport_bug () :
    """ Fonction qui permet de créer un rapport de bug """

    message = input ( " Veuillez taper votre rapport de bug : ")

    crud.creer_rapport_bug (message)

# Message sous ticket

def echanger_message () :
    """ Fonction qui permet à l'utilisateur et l'administrateur d'échanger des messages """

    message = input ( " Veuillez écrire votre message : ")

    crud.creer_ticket_message()