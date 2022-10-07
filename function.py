from email import message
import sqlite3
import crud

def creer_compte() -> None:
    """Demande le prénom, nom et mot de passe du compte a creer puis le crée"""

    prenom = input("Quel est votre prénom : ")
    nom = input("Quel est votre nom : ")
    mdp = input("Choisissez un mot de passe : ")

    crud.creation_utilisateur(prenom, nom, mdp)

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