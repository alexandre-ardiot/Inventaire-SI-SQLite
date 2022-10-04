import sqlite3

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()

curseur.execute('''CREATE TABLE Type_ordinateur
                (
                    id INTEGER PRIMARY KEY,
                    marque TEXT,
                    processeur TEXT,
                    carte_graphique TEXT,
                    ram TEXT,
                    disque TEXT
                )
''')

connexion.commit()
connexion.close()