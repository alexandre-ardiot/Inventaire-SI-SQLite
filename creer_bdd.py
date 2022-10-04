import sqlite3

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()


curseur.execute('''CREATE TABLE User
                (
                    id INTEGER PRIMARY KEY,
                    role INTEGER,
                    prenom TEXT,
                    nom TEXT,
                    mot_de_passe TEXT
                )
''')

curseur.execute('''CREATE TABLE chat_tickets
                (
                    date TEXT,
                    id_ticket INTEGER,
                    auteur TEXT,
                    message TEXT,
                    FOREIGN KEY (id_ticket)
                        REFERENCES Ticket(id)
                        ON DELETE CASCADE,
                    FOREIGN KEY (auteur)
                        REFERENCES User(id)
                        ON DELETE CASCADE
                )
''')

curseur.execute('''CREATE TABLE Ticket
                (
                    id INTEGER PRIMARY KEY,
                    date_creation TEXT,
                    id_ref_pret INTEGER,
                    status INTEGER,
                    message TEXT,
                    FOREIGN KEY (id_ref_pret)
                        REFERENCES Carnet_pret(reference_pc)
                        ON DELETE CASCADE
                )
''')

curseur.execute('''CREATE TABLE Carnet_pret
                (
                    reference_pc TEXT PRIMARY KEY,
                    user_id INTEGER,
                    type_ordinateur_id INTEGER,
                    FOREIGN KEY (user_id)
                        REFERENCES User(id)
                        ON DELETE CASCADE,
                    FOREIGN KEY (type_ordinateur_id)
                        REFERENCES Type_ordinateur(id)
                        ON DELETE CASCADE
                )
''')

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