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

# Exécuter la requête SQL
query = "SELECT SUM(capacite) AS capacite_totale FROM salles;"
cursor.execute(query)

# Récuperer le résultat
result = cursor.fetchone()[0]

# Afficher le résultat
print("La capacité de toutes les salles est de :", result)

# Fermer le curseur et la connexion
cursor.close()
cnx.close()