import sqlite3
import hashlib
from datetime import datetime

def creation_utilisateur(email:str, prenom:str, nom:str, mdp:str) -> None:
    """Creer un utilisateur dans la table User
    :param prenom: Prénom de l'utilisateur
    :param nom: Nom de l'utilisateur
    :param mdp: Mot de passe de l'utilisateur
    :param email : e-mail de l'utilisateur
    """
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    mdp += email
    mdp_chiffre = hashlib.sha256(mdp.encode()).hexdigest()
    curseur.execute("INSERT INTO User VALUES (?, ? , ?, ?, ?, ?)", (None, email , 0, prenom, nom, mdp_chiffre))

    connexion.commit()
    connexion.close()

def creer_type_pc ( marque, processeur, carte_graphique, ram, disque ):
    """ Fonction qui permet de créer un pc dans la table Type_ordinateur
    :parm marque : Marque de l'ordinateur
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


def vérifier_utilisateur(email, mdp):
    """ Fonction qui vérifie l'email et le mot de passe de l'utilsateur
    :param email: Email de l'utilisateur
    :param mdp: Mot de passe du compte de l'utilisateur
    """

    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    
    mdp += email
    mdp_chiffre = hashlib.sha256(mdp.encode()).hexdigest()
    
    curseur.execute('''
                    SELECT * FROM utilisateur
                        WHERE email = ? AND mdp = ?
                    ''', (email, mdp_chiffre))
    
    reponse = curseur.fetchone()
    connexion.close()
    return reponse

# Espace utilisateur

def ajouter_pc (reference_pc , id_user, type_ordinateur_id ) :
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

def retirer_pc (reference_pc) : 
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

def creer_un_message ( id_ticket , id_user , message) :
    """
    Fonction qui permet de créer un rapport de bug dans la table Ticket
    :param date : date de la création du rapport de bug
    :param id_ticket : identifiant du ticket
    :param id_user : identifiant de l'utilisateur
    :param message : message de l'utilisateur pour le bug
    """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute ('''
                    INSERTE INTO Tickets VALUES (?, ?, ?, ?)
                    ''',(datetime.today().strftime('%Y-%m-%d') , id_ticket , id_user , message))

    connexion.commit()
    connexion.close()

# Message sous ticket

def creer_ticket_message (id_chat_ticket , id_ticket , id_user , message):
    """
    Fonction qui permet à l'utilisateur et l'administrateur de discuter
    :param date : date du ticket
    :param id_chat_ticket : identifiant du ticket de chat
    :param id_ticket : identifiant du ticket
    :param id_user : identifiant de l'utilisateur
    :param message : message entre l'utilisateur et l'administrateur
    """
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()


    curseur.execute ('''
                    INSERTE INTO chat_tickets VALUES (?, ?, ?, ?)
                    ''',(id_chat_ticket , datetime.today().strftime('%Y-%m-%d') , id_ticket , id_user , message))

    connexion.commit()
    connexion.close()



def nombre_pc_preter ():
    """ Fonction qui permet de connaitre le nombre d'ordinateur en prêt """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute (''' SELECT COUNT (*) FROM Carnet_pret ''')

    resultat = curseur.fetchone()
    connexion.close()
    return resultat

def nombre_de_panne () :
    """ Fonction qui permet de connaitre le nombre d'ordinateur en panne """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute ( ''' SELECT COUNT (*) FROM Ticket''')

    resultat = curseur.fetchone()
    connexion.close()
    return resultat