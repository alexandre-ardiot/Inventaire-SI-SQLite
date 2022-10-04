import sqlite3
connexion = sqlite3.connect("base_de_donnee.db")
curseur= connexion.cursor()

curseur.execute (''' CREATE TABLE Carnet_de_pret
(
    reference_pc TEXT PRIMARY KEY,
    FOREIN KEY (id_utilisateur)
        utilisateur(id),
    FOREIN KEY (type_ordinateur_id)
        type_ordinateur (id)
)
''')
connexion.commit()


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