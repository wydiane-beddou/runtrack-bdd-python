import mysql.connector

# Créer une connexion à la base de données
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="WeshGrow!",
    database="laplateforme"
)

# Créer un curseur pour exécuter des requêtes SQL
cursor = cnx.cursor()


# Exécuter la requête SQL pour récupérer les noms et capacités de la table "salles"
requete = "SELECT nom, capacite FROM salles"
cursor.execute(requete)

# récupérer les résultats sous forme de liste de tuples
resultats = cursor.fetchall()

# afficher les résultats
print(resultats)

# close the cursor and connection to the database
cursor.close()
cnx.close()
