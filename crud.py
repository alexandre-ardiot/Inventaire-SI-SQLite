from fileinput import close
import sqlite3
import hashlib

from datetime import datetime
from typing import Any
from xmlrpc.client import Boolean

def creation_utilisateur(email:str, prenom:str, nom:str, mdp:str) -> None:
    """Creer un utilisateur dans la table User
    :param email : e-mail de l'utilisateur
    :param prenom: Prénom de l'utilisateur
    :param nom: Nom de l'utilisateur
    :param mdp: Mot de passe de l'utilisateur
    """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    mdp += email
    mdp_chiffre = hashlib.sha256(mdp.encode()).hexdigest()
    curseur.execute("INSERT INTO User VALUES (?, ? , ?, ?, ?, ?)", (None, email , 0, prenom, nom, mdp_chiffre))

    connexion.commit()
    connexion.close()

def creer_type_pc (marque:str, processeur:str, carte_graphique:str, ram:str, disque:str) -> None:
    """ Fonction qui permet de créer un pc dans la table Type_ordinateur
    :param marque : Marque de l'ordinateur
    :param processeur : Processeur de lordinateur
    :param carte_graphique : Carte graphique de l'ordinateur
    :param ram : Ram de l'ordinateur
    :param disque : Disque de l'ordinateur
    """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute ("INSERT INTO Type_ordinateur VALUES (? , ? , ? , ? , ? , ?)", (None, marque, processeur, carte_graphique, ram, disque))

    connexion.commit()
    connexion.close()

def verifier_utilisateur(email:str, mdp:str) -> str:
    """ Fonction qui vérifie l'email et le mot de passe de l'utilsateur
    :param email: Email de l'utilisateur
    :param mdp: Mot de passe du compte de l'utilisateur
    """

    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    
    mdp += email
    mdp_chiffre = hashlib.sha256(mdp.encode()).hexdigest()
    
    curseur.execute('''
                    SELECT * FROM User
                        WHERE email = ? AND mot_de_passe = ?
                    ''', (email, mdp_chiffre))
    
    reponse = curseur.fetchone()
    connexion.close()

    return reponse

# Espace utilisateur

def ajouter_pc (reference_pc:str, id_user:int, type_ordinateur_id:int) -> None:
    """
    Fonction qui permet d'ajouter un ordinateur et ses informations dans la table Carnet_pret
    :param reference_pc : référence de l'ordinateur
    :param id_user : identifiant de l'utilisateur
    :param type_ordinateur_id : idenfiant du type d'ordinateur
    """
    
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute ('''
                    INSERT INTO Carnet_pret VALUES (?, ?, ?)
                    ''', (reference_pc, id_user, type_ordinateur_id))
    

    connexion.commit()
    connexion.close()

def retirer_pc (reference_pc:str) -> None: 
    """
    Fonction qui permet de retirer un ordinateur et ses informations dans la table Carnet_pret
    :parm reference_pc : référence de l'ordinateur
    """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute ( ''' 
                    DELETE FROM Carnet_pret
                    WHERE reference_pc = ?
                    ''',(reference_pc,))

    connexion.commit()
    connexion.close()

def pc_utilisateur(user_id:int) -> None: 
    """
    Fonction qui permet de les références des PC de l'utilisateur
    :param user_id: ID de l'utilisateur
    """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute(''' 
                    SELECT * FROM Carnet_pret
                    WHERE user_id = ?
                    ''',(user_id,))

    resultat = curseur.fetchall()
    connexion.close()

    return resultat

def creer_un_message (ref_pret:str, status:str, message:str) -> None:
    """
    Fonction qui permet de créer un rapport dans la table Ticket
    :param ref_pret : identifiant du ticket
    :param status : status du message
    :param message : message de l'utilisateur pour le ticket
    """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute ('''
                    INSERT INTO Ticket VALUES (?, ?, ?, ?, ?)
                    ''',(None, datetime.today().strftime('%Y-%m-%d'), ref_pret, status, message))

    connexion.commit()
    connexion.close()

# Message sous ticket

def creer_ticket_message (id_ticket:int, id_user:int, message:str) -> None:
    """
    Fonction qui permet à l'utilisateur et l'administrateur de discuter
    :param id_ticket : identifiant du ticket
    :param id_user : identifiant de l'utilisateur
    :param message : message entre l'utilisateur et l'administrateur
    """
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()


    curseur.execute ('''
                    INSERT INTO chat_tickets VALUES (?, ?, ?, ?, ?)
                    ''',(None , datetime.today().strftime('%Y-%m-%d') , id_ticket , id_user , message))

    connexion.commit()
    connexion.close()

def nombre_pc_prete () -> int:
    """ Fonction qui permet de connaitre le nombre d'ordinateur en prêt """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute ('''SELECT COUNT (*) FROM Carnet_pret''')

    resultat = curseur.fetchone()
    connexion.close()
    return resultat

def nombre_de_panne () -> int:
    """ Fonction qui permet de connaitre le nombre d'ordinateur en panne """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute ('''SELECT COUNT (*) FROM Ticket''')

    resultat = curseur.fetchone()
    connexion.close()
    return resultat

def obtenir_tickets_utilisateur(id_user:int) -> tuple:
    """Renvoi les tickets de l'utilisateur"""


    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()

    curseur.execute('''
                    SELECT * FROM ticket
                    INNER JOIN Carnet_pret
                        ON Carnet_pret.reference_pc = ticket.ref_pret
                        WHERE Carnet_pret.user_id = ?
                    ''', (id_user,))

    resultat = curseur.fetchall()
    connexion.close()

    return resultat

def obtenir_tickets_admin() -> tuple:
    """Renvoi tout les tickets"""


    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()

    curseur.execute('''
                    SELECT * FROM ticket
                    ''')

    resultat = curseur.fetchall()
    connexion.close()

    return resultat

def voir_ticket_en_cours(status) :
    """ Fonction qui permet de consulter le status des tickets en cours (1)"""

    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()

    curseur.execute(''' 
                    SELECT * FROM Ticket
                    WHERE status IN ( 1 )
                    ''')

    resultat = curseur.fetchall()
    connexion.close()

    return resultat

def voir_pret(user_id:int) -> tuple:
    """ Fonction qui permet de consulter les prêts en cours"""

    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()

    curseur.execute(''' 
                    SELECT * FROM Carnet_pret
                        WHERE user_id = ?
                    ''', (user_id,))

    resultat = curseur.fetchall()
    connexion.close()

    return resultat

def ajouter_info_pc(marque:str, processeur:str, carte_graphique:str, ram:int, disque:int) -> None:
    """Permet de remplir la table Type_ordinateur
    :param marque: Marque de l'ordinateur
    :param processeur: Processeur de l'ordinateur
    :param carte_graphique: Carte graphique de l'ordinateur
    :param ram: Quantitée de RAM de l'ordinateur
    :param disque: Espace disque de l'ordinateur
    """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute("INSERT INTO Type_ordinateur VALUES (?, ? , ?, ?, ?, ?)", (None, marque, processeur, carte_graphique, ram, disque))

    connexion.commit()
    connexion.close()

"""def chat_existe(id_ticket):
    #Vérifie"""

def minou_minou(ticket_id:int):
    """Affiche les messages du chat
    :param ticket_id: ID tu ticket de référence
    """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute('''
                    SELECT * FROM chat_tickets
                    INNER JOIN Ticket
                        ON chat_tickets.id_ticket = Ticket.id
                        WHERE chat_tickets.id_ticket = ?
                    ''', (ticket_id,))

    resultat = curseur.fetchall()
    connexion.close()

    return resultat

def message_chat(ticket_id:int, auteur:str, message:str):
    """Ajout d'un nouveau message dans un chat
    :param ticket ID: ID du ticket de référence
    :param auteur: Prénom de l'utilisateur
    :param message: Message de l'utilisateur
    """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute('''
                    INSERT INTO chat_tickets VALUES (?, ?, ?, ?, ?)
                    ''', (None, datetime.today().strftime('%Y-%m-%d'), ticket_id, auteur, message))

    connexion.commit()
    connexion.close()