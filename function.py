import sqlite3
from time import sleep
import crud

import os
from email import message


def creer_compte() -> None:
    """Demande le prénom, nom et mot de passe du compte a creer puis le crée"""

    email = input("Quel est votre email : ")
    prenom = input("Quel est votre prénom : ")
    nom = input("Quel est votre nom : ")
    mdp = input("Choisissez un mot de passe : ")

    crud.creation_utilisateur(email, prenom, nom, mdp)

def creer_type_pc() -> None:
    """ Fonction qui permet d'ajouter des ordinateur dans la base de donnée type_ordinateur"""
    
    marque = input(" Entrez la marque de l'ordinateur : ")
    processeur = input (" Entrez le processeur de l'ordinateur : " )
    carte_graphique = input (" Entrez la carte graphique de l'ordinateur : " )
    ram = input (" Entrez la ram de l'ordinateur : " )
    disque = input (" Entrez le disque de l'ordinateur : " )

    crud.creer_type_pc(marque, processeur, carte_graphique, ram, disque)

def se_connecter() -> str:
    """ Fonction qui permet de s'identifier """

    email = input ( "Quelle est votre e_mail : ")
    mdp = input ( "Quel est votre mot de passe : ")

    crud.verifier_utilisateur(email, mdp )


# Espace utilisateur

def ajouter_un_ordinateur(id_user) :
    """ Fonction qui permet d'ajouter un ordinateur """

    reference_pc = input ("Entrez la référence de l'ordinateur que vous voulez ajouter : ")
    type_ordinateur_id = input ("Quel est votre type d'ordinateur : ")

    crud.ajouter_pc(reference_pc, id_user , type_ordinateur_id)


def retirer_un_ordinateur () :
    """ Fonction qui permet de retirer un ordinateur """

    reference_pc = input ("Entrez la référence de l'ordinateur que vous voulez retirez : ")

    crud.retirer_pc(reference_pc)


def creer_ticket() :
    """Fonction qui permet de créer un rapport de bug"""

    message = input("Veuillez taper votre rapport de bug : ")

    crud.creer_un_message(message)

# Message sous ticket

def echanger_message (id_user) :
    """ Fonction qui permet à l'utilisateur et l'administrateur d'échanger des messages """

    message = input ("Veuillez écrire votre message : ")

    crud.creer_ticket_message(None, id_user, message)

def afficher_accueil_utilisateur(id_user):
    """Renvoi les tickets de l'utilisateur, avec un délai de 1,5 seconde entre chaque ticket"""
    
    liste_tickets = crud.obtenir_tickets_utilisateur(id_user)

    for ticket in liste_tickets:
        os.system("clear")
        print("Vos tickets :")
        print(ticket)
        print("---------")
        sleep(1.5)