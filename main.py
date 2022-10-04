import sqlite3
import crud
import function

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()


connexion.commit()
connexion.close()