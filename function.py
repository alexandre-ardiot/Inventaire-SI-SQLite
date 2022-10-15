import crud
import os

from time import sleep

#Création de compte et connexion

def creer_compte() -> None:
    """Demande le prénom, nom et mot de passe du compte a creer puis le crée"""

    email = input("Quel est votre email : ")
    prenom = input("Quel est votre prénom : ")
    nom = input("Quel est votre nom : ")
    mdp = input("Choisissez un mot de passe : ")

    crud.creation_utilisateur(email, prenom, nom, mdp)

def se_connecter() -> tuple:
    """ Fonction qui permet de s'identifier """

    email = input ( "Quelle est votre e_mail : ")
    mdp = input ( "Quel est votre mot de passe : ")

    user = crud.verifier_utilisateur(email, mdp )

    return user

#Espace Utilisateur

def afficher_ticket_utilisateur(id_user:int) -> None:
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

def creer_ticket(ref_pret:str) -> None :
    """Fonction qui permet de créer un rapport de bug
    :param ref_pret: Référence de l'ordinateur
    """

    message = input("Veuillez taper votre rapport de bug : ")

    crud.creer_un_ticket(ref_pret, 1, message)

def afficher_pret(user_id:int) -> tuple:
    """Permet d'afficher les prêts en cours de l'utilisateur
    :param user_id: ID de l'utilisateur
    """
    
    prets = crud.voir_pret(user_id)

    a = 0

    for pret in prets:
        print(a, " - ", pret[0])
        a += 1

    return prets

def ajouter_pc(user_id:int) -> None:
    """Permet d'ajouter un PC à la Carnet_pret
    :param user_id: ID de l'utilisateur en cours
    """

    reference_pc = input("Quelle est la référence du PC : ")
    type_ordinateur_id = int(input("Quelle est votre type d'ordinateur (0 - PC fixe, 1 - PC portable) : "))

    crud.ajouter_pc(reference_pc, user_id, type_ordinateur_id)

def ajouter_info_pc() -> None:
    """Permet de remplir la table Type_ordinateur"""

    marque = input("Quelle est la marque du PC ? : ")
    processeur = input("Quelle est le processeur du PC ? : ")
    carte_graphique = input("Quelle est la carte graphique du PC ? : ")
    ram = int(input("Quelle est la quantitée de RAM du PC ? : "))
    disque = int(input("Quelle est l'espace disque du PC ? : "))

    crud.ajouter_info_pc(marque, processeur, carte_graphique, ram, disque)

def retirer_pc(user_id:int) -> None:
    """Liste les références de PC de l'utilisateur puis supprime celle choisie par l'utilisateur
    :param user_id: ID de l'utilisateur
    """

    references = crud.pc_utilisateur(user_id)

    for ref in references:
        print(ref[0])

    choix = input("Quelle référence souhaitez-vous supprimer ? : ")

    crud.retirer_pc(choix)

#Espace Admin

def afficher_tickets_admin() -> None:
    """Renvoi tout les tickets"""

    liste_tickets = crud.obtenir_tickets_admin()

    os.system("clear")
    print("Tickets en cours :\n")

    for ticket in liste_tickets:
        print(ticket)
        print("---------")

    print("\n")

#Chat

def chat(ticket_id:int, user:str):
    """Affiche les messages du chat déjà existant et demande à l'utilisateur le message qu'il souhaite y rajouter
    :param ticket_id: ID du ticket lié au chat
    :param user; Prénom de l'utilisateur
    """

    messages = crud.ticket_afficher_chat(ticket_id)

    for message in messages:
        print(message[3], " : ", message[4])

    nouveau_message = input("Entrez du texte : ")
    crud.message_chat(ticket_id, user, nouveau_message)

#Divers

def clear() -> None:
    "Nettoie l'écran"

    os.system("clear")

def afficher_erreur() -> None:
    """Affiche qu'une erreur est survenue durant 2,5 secondes"""

    os.system("clear")
    print("Une erreur est survenue, veuillez reessayer")
    sleep(2.5)
    os.system("clear")