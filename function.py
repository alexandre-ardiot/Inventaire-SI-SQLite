import sqlite3
import crud
import os

from time import sleep
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

    user = crud.verifier_utilisateur(email, mdp )

    return user

# Espace utilisateur

def ajouter_un_ordinateur(id_user) :
    """Fonction qui permet d'ajouter un ordinateur
    :param id_user: Identifiant de l'utilisateur
    """

    reference_pc = input ("Entrez la référence de l'ordinateur que vous voulez ajouter : ")
    type_ordinateur_id = input ("Quel est votre type d'ordinateur : ")

    crud.ajouter_pc(reference_pc, id_user , type_ordinateur_id)

def retirer_un_ordinateur () :
    """ Fonction qui permet de retirer un ordinateur """

    reference_pc = input ("Entrez la référence de l'ordinateur que vous voulez retirez : ")

    crud.retirer_pc(reference_pc)

def creer_ticket(ref_pret:str) -> None :
    """Fonction qui permet de créer un rapport de bug
    :param ref_pret: Référence de l'ordinateur
    """

    message = input("Veuillez taper votre rapport de bug : ")

    crud.creer_un_message(ref_pret, 1, message)

# Message sous ticket

def echanger_message (id_user) :
    """Fonction qui permet à l'utilisateur et l'administrateur d'échanger des messages
    :param id_user: Identifiant de l'utilisateur
    """

    message = input ("Veuillez écrire votre message : ")

    crud.creer_ticket_message(None, id_user, message)

def afficher_accueil_utilisateur(id_user):
    """Renvoi les tickets de l'utilisateur
    :param id_user: Identifiant de l'utilisateur
    """

    liste_tickets = crud.obtenir_tickets_utilisateur(id_user)

    os.system("clear")
    print("Vos tickets :\n")

    for ticket in liste_tickets:
        print(ticket)
        print("---------")

    print("\n")

def afficher_tickets_admin():
    """Renvoi tout les tickets"""

    liste_tickets = crud.obtenir_tickets_admin()

    os.system("clear")
    print("Tickets en cours :\n")

    for ticket in liste_tickets:
        print(ticket)
        print("---------")

    print("\n")

def afficher_erreur():
    os.system("clear")
    print("Une erreur est survenue, veuillez reessayer")
    sleep(2.5)
    os.system("clear")

def afficher_pret(user_id:int):
    "Permet d'afficher les prêts en cours de l'utilisateur"
    
    prets = crud.voir_pret(user_id)

    a = 0

    for pret in prets:
        print(a, " - ", pret[0])
        a += 1

    return prets

def clear() -> None:
    "Nettoie l'écran"
    os.system("clear")

def ajouter_pc(user_id:int) -> None:
    """Permet d'ajouter un PC à la Carnet_pret
    :param user_id: ID de l'utilisateur en cours
    """

    reference_pc = input("Quelle est la référence du PC : ")
    type_ordinateur_id = int(input("Quelle est votre type d'ordinateur (0 - PC fixe, 1 - PC portable) : "))

    crud.ajouter_pc(reference_pc, user_id, type_ordinateur_id)

def retirer_pc(user_id:int) -> None:
    """Liste les références de PC de l'utilisateur puis supprime celle choisie par l'utilisateur
    :param user_id: ID de l'utilisateur
    """

    references = crud.pc_utilisateur(user_id)

    for ref in references:
        print(ref[0])

    choix = input("Quelle référence souhaitez-vous supprimer ? : ")

    crud.retirer_pc(choix)

def ajouter_info_pc() -> None:
    """Permet de remplir la table Type_ordinateur"""

    marque = input("Quelle est la marque du PC ? : ")
    processeur = input("Quelle est le processeur du PC ? : ")
    carte_graphique = input("Quelle est la carte graphique du PC ? : ")
    ram = int(input("Quelle est la quantitée de RAM du PC ? : "))
    disque = int(input("Quelle est l'espace disque du PC ? : "))

    crud.ajouter_info_pc(marque, processeur, carte_graphique, ram, disque)

def chat(ticket_id:int, user:str):
    """Affiche les messages du chat déjà existant et demande à l'utilisateur le message qu'il souhaite y rajouter
    :param ticket_id: ID du ticket lié au chat
    :param user; Prénom de l'utilisateur
    """

    messages = crud.minou_minou(ticket_id)

    for message in messages:
        print(message[3], " : ", message[4])

    nouveau_message = input("Entrez du texte : ")
    crud.message_chat(ticket_id, user, nouveau_message)