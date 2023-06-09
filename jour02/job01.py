import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("PASSWORD")
# Connexion à la base de données
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = password,
    database = "laplateforme"
)

# Exécution de la requête
cursor = db.cursor()
cursor.execute("SELECT * FROM etudiants")

# Récupération des résultats
resultats = cursor.fetchall()

# Affichage des résultats en console
for row in resultats:
    print(row)

# Fermeture de la connexion à la base de données
db.close()
