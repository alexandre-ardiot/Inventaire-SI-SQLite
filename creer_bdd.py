import sqlite3

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()

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



curseur.execute (''' CREATE TABLE Carnet_de_pret
(
    reference_pc TEXT PRIMARY KEY,
    FOREIN KEY (id_utilisateur)
        utilisateur(id),
    FOREIN KEY (type_ordinateur_id)
        type_ordinateur (id)
)
''')



curseur.execute (''' CREATE TABLE ticket
(
    id TEXT PRIMARY KEY,
    date_creation TEXT,
    status TEXT,
    message TEXT,
    FOREIN KEY (id_reference_pc)
        ticket(reference_pc)
)
''')
connexion.commit()
connexion.close()