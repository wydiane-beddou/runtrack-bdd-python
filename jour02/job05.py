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
query = "SELECT SUM(superficie) AS superficie_totale FROM etage;"
cursor.execute(query)

# Récuperer le résultat
result = cursor.fetchone()[0]

# Afficher le résultat
print("La superficie de la Plateforme est de ", result, "m²")

# Fermer le curseur et la connexion
cursor.close()
cnx.close()