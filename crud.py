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



def cree_admin ( nom, prenom, mdp):
    
    connexion = sqlite3.connect ('bdd,db')
    curseur =  connexion.cursor()
    
    curseur.execute ("INSERT INTO utilisateur VALUES,(?, ?, ?, ?, ?)", (None , 1 , nom, prenom, mdp))

    connexion.commit()
    connexion.close()

<<<<<<< HEAD
    
    
    

def cree_liste_tickets_ouvert(id,date_creation,id_ref_pret,status,message):
    connexion = sqlite3.connect ('bdd,db')
    curseur =  connexion.cursor()
   
   
    curseur.execute('''
                
                    SELECT COUNT (*) date_creation FROM Ticket 

                    ''')
    
=======
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
    :parm reference_pc : référence de l'ordinateur
    :param id_user : identifiant de l'utilisateur
    :param type_ordinateur_id : idenfiant du type d'ordinateur
    """
    
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute ('''
                    INSERT INTO Carnet_pret VALUES (? , ? , ?)

                    ''', (reference_pc , id_user, type_ordinateur_id))
    

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

def creer_un_message (id_ref_pret:int, status:str, message:str) -> None:
    """
    Fonction qui permet de créer un rapport dans la table Ticket
    :param id_ref_pret : identifiant du ticket
    :param status : status du message
    :param message : message de l'utilisateur pour le ticket
    """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute ('''
                    INSERT INTO Ticket VALUES (?, ?, ?, ?, ?)
                    ''',(None, datetime.today().strftime('%Y-%m-%d'), id_ref_pret, status, message))

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
>>>>>>> e00d4e1adb12fed00f0d584e9a6410694144404f

    connexion.commit()
    connexion.close()



<<<<<<< HEAD
def cree_carnet_pret (reference_pc,user_id,type_ordinateur_id):
    connexion = sqlite3.connect ('bdd,db')
    curseur =  connexion.cursor()
   
    curseur.execute ("INSERT TO cree_carnet_pret VALUES,(?,?,?,?)",(reference_pc,user_id,type_ordinateur_id))


    connexion.commit()
    connexion.close()
    
    for ligne in curseur.fetchall()
    print (ligne)
    
=======
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
                    INNER JOIN carnet_pret
                        ON carnet_pret.reference = ticket.ref_pret
                        WHERE carnet_pret.utilisateur_id = ?
                    ''', (id_user,))

    resultat = curseur.fetchall()
    connexion.close()

    return resultat
>>>>>>> e00d4e1adb12fed00f0d584e9a6410694144404f
