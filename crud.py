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



def cree_admin ( nom, prenom, mdp):
    
    connexion = sqlite3.connect ('bdd,db')
    curseur =  connexion.cursor()
    
    curseur.execute ("INSERT INTO utilisateur VALUES,(?,?,?)",(nom, prenom, mdp))

    connexion.commit()
    connexion.close()

    
    
    

def cree_liste_tickets_ouvert(id,date_creation,id_ref_pret,status,message):
    connexion = sqlite3.connect ('bdd,db')
    curseur =  connexion.cursor()
   
   
    curseur.execute('''
                
                    SELECT COUNT (*) date_creation FROM Ticket 

                    ''')
    

    connexion.commit()
    connexion.close()



def cree_carnet_pret (reference_pc,user_id,type_ordinateur_id):
    connexion = sqlite3.connect ('bdd,db')
    curseur =  connexion.cursor()
   
    curseur.execute ("INSERT TO cree_carnet_pret VALUES,(?,?,?,?)",(reference_pc,user_id,type_ordinateur_id))


    connexion.commit()
    connexion.close()
    


def nb_pret_ordinateur(reference_pc,user_id,type_ordinateur_id):
    connexion = sqlite3.connect ('bdd,db')
    curseur =  connexion.cursor()

    curseur.execute ('''

                    SELECT COUNT(*) id_ref_pret 
                    FROM Ticket(id,date_creation,id_ref_pret,status,message)
                    INNER JOIN
                    ON
                    INNER JOIN
                    ON type_ordinateur

                    ''')

    for ligne in curseur.fetchall()
    print (ligne)
    
   



def nb_panne_ordinateur(reference_pc,user_id,type_ordinateur_id):
    connexion = sqlite3.connect ('bdd,db')
    curseur =  connexion.cursor()
    
    
    curseur.execute('''

                     SELECT COUNT(*) id 
                     FROM Type_ordinateur(id,marque,processeur,carte_graphique,ram,disque
                     INNER JOIN
                     ON
                     INNER JOIN
                     ON type_ordinateur

                   ''')

    for ligne in curseur.fetchall()
    print (ligne)
    