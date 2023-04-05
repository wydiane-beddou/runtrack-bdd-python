import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("PASSWORD")
# Connexion à la base de données
cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = password,
    database = "laplateforme"
)


# Créer un curseur
cursor = cnx.cursor()

# Récupérer tous les employés et leur service respectif
query = "SELECT e.nom, e.prenom, s.nom FROM employes e JOIN services s ON e.id_service = s.id"
cursor.execute(query)

# Récupérer les résultats et les afficher en console
for (nom, prenom, service) in cursor:
    print(nom, prenom, service)

# Fermer le curseur et la connexion à la base de données
cursor.close()
cnx.close()

# CLASSE

class Employes:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password='WeshGrow!',
            database = 'laplateforme'
        )
        self.cursor = self.cnx.cursor()

    def get_all(self):
        query = "SELECT * FROM employes"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_by_id(self, id):
        query = "SELECT * FROM employes WHERE id = %s"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()

    def insert(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (nom, prenom, salaire, id_service))
        self.cnx.commit()
        return self.cursor.lastrowid

    def update(self, id, nom, prenom, salaire, id_service):
        query = "UPDATE employes SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        self.cursor.execute(query, (nom, prenom, salaire, id_service, id))
        self.cnx.commit()

    def delete(self, id):
        query = "DELETE FROM employes WHERE id = %s"
        self.cursor.execute(query, (id,))
        self.cnx.commit()

    def __del__(self):
        self.cursor.close()
        self.cnx.close()



with Employes() as employes:
    try:
        # Récupérer tous les employés
        all_employes = employes.get_all()
        print(all_employes)

        # Récupérer un employé par ID
        employes_by_id = employes.get_by_id(1)
        print(employes_by_id)

        # Insérer un nouvel employé
        new_employes_id = employes.insert("Hot", "Dog", 4000, 1)
        
        print(new_employes_id)

        # Mettre à jour un employé existant
        employes.update(4, "Dupont", "Jean", 3000, 2)
        
        # Supprimer un employé
        employes.delete(5)
    except Exception as e:
        print(f"Error occurred: {e}")