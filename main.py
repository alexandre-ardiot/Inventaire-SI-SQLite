import sqlite3
import crud
import fonction

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()


connexion.commit()
connexion.close()