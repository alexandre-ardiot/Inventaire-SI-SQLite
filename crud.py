import sqlite3

def creation_utilisateur(prenom:str, nom:str, mdp:str) -> None:
    """Creer un utilisateur dans la table User
    :param prenom: Prénom de l'utilisateur
    :param nom: Nom de l'utilisateur
    :param mdp: Mot de passe de l'utilisateur
    """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute("INSERT INTO User VALUES (?, ?, ?, ?, ?)", (None, 0, prenom, nom, mdp))

    connexion.commit()
    connexion.close()

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
                    WHERE reference_pc = 0
                    ''')

    connexion.commit()
    connexion.close()

def creer_rapport_bug ( date , id_ticket , id_user , message) :
    """
    Fonction qui permet de créer un rapport de bug
    """

    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()

    curseur.execute ('''
                    INSERTE INTO chat_tickets VALUES (?, ?, ?, ?)
                    ''',(date , id_ticket , id_user , message))

    connexion.commit()
    connexion.close()