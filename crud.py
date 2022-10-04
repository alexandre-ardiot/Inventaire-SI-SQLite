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