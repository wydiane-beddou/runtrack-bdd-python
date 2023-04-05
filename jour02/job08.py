import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Zoo:
    def __init__(self):
        password = os.getenv("PASSWORD")
        self.cnx = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = password,
        database = "laplateforme"
)
        self.cursor = self.cnx.cursor()

    def get_all_animals(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_all_cages(self):
        query = "SELECT * FROM cage"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_animal(self, nom, race, date_naissance, pays_origine, id_cage):
        query = "INSERT INTO animal (nom, race, date_naissance, pays_origine, id_cage) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (nom, race, date_naissance, pays_origine, id_cage))
        self.cnx.commit()
        return self.cursor.lastrowid

    def remove_animal(self, id_animal):
        query = "DELETE FROM animal WHERE id_animal = %s"
        self.cursor.execute(query, (id_animal,))
        self.cnx.commit()

    def update_animal(self, id_animal, nom, race, date_naissance, pays_origine, id_cage):
        query = "UPDATE animal SET nom = %s, race = %s, date_naissance = %s, pays_origine = %s, id_cage = %s WHERE id_animal = %s"
        self.cursor.execute(query, (nom, race, date_naissance, pays_origine, id_cage, id_animal))
        self.cnx.commit()

    def add_cage(self, superficie, capacite_max):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        self.cursor.execute(query, (superficie, capacite_max))
        self.cnx.commit()
        return self.cursor.lastrowid

    def remove_cage(self, id_cage):
        query = "DELETE FROM cage WHERE id_cage = %s"
        self.cursor.execute(query, (id_cage,))
        self.cnx.commit()

    def update_cage(self, id_cage, superficie, capacite_max):
        query = "UPDATE cage SET superficie = %s, capacite_max = %s WHERE id_cage = %s"
        self.cursor.execute(query, (superficie, capacite_max, id_cage))
        self.cnx.commit()

    def get_animals_in_cage(self, id_cage):
        query = "SELECT * FROM animal WHERE id_cage = %s"
        self.cursor.execute(query, (id_cage,))
        return self.cursor.fetchall()

    def get_total_cage_area(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def __del__(self):
        self.cursor.close()
        self.cnx.close()

zoo = Zoo()

while True:
    print("Que souhaitez-vous faire ?")
    print("1 - Ajouter un animal")
    print("2 - Supprimer un animal")
    print("3 - Modifier un animal")
    print("4 - Ajouter une cage")
    print("5 - Supprimer une cage")
    print("6 - Modifier une cage")
    print("7 - Afficher tous les animaux")
    print("8 - Afficher les animaux dans une cage")
    print("9 - Afficher la superficie totale des cages")
    choix = input("Votre choix : ")

    if choix == '1':
        nom = input("Nom de l'animal : ")
        race = input("Race de l'animal : ")
        date_naissance = input("Date de naissance de l'animal (AAAA-MM-JJ) : ")
        pays_origine = input("Pays d'origine de l'animal : ")
        id_cage = input("ID de la cage de l'animal : ")
        zoo.add_animal(nom, race, date_naissance, pays_origine, id_cage)
        print("Animal ajouté avec succès !")

    elif choix == '2':
        id_animal = input("ID de l'animal à supprimer : ")
        zoo.remove_animal(id_animal)
        print("Animal supprimé avec succès !")

    elif choix == '3':
        id_animal = input("ID de l'animal à modifier : ")
        nom = input("Nouveau nom de l'animal : ")
        race = input("Nouvelle race de l'animal : ")
        date_naissance = input("Nouvelle date de naissance de l'animal (AAAA-MM-JJ) : ")
        pays_origine = input("Nouveau pays d'origine de l'animal : ")
        id_cage = input("Nouvel ID de la cage de l'animal : ")
        zoo.update_animal(id_animal, nom, race, date_naissance, pays_origine, id_cage)
        print("Animal modifié avec succès !")

    elif choix == '4':
        superficie = input("Superficie de la nouvelle cage : ")
        capacite_max = input("Capacité maximum de la nouvelle cage : ")
        zoo.add_cage(superficie, capacite_max)
        print("Cage ajoutée avec succès !")

    elif choix == '5':
        id_cage = input("ID de la cage à supprimer : ")
        zoo.remove_cage(id_cage)
        print("Cage supprimée avec succès !")

    elif choix == '6':
        id_cage = input("ID de la cage à modifier : ")
        superficie = input("Nouvelle superficie de la cage : ")
        capacite_max = input("Nouvelle capacité maximum de la cage : ")
        zoo.update_cage(id_cage, superficie, capacite_max)
        print("Cage modifiée avec succès !")

    elif choix == '7':
        print("Liste de tous les animaux :")
        animals = zoo.get_all_animals()
        for animal in animals:
            print(animal)

    elif choix == '8':
        id_cage = input("ID de la cage à afficher : ")
        print("Liste des animaux dans la cage {} :".format(id_cage))
        animals = zoo.get_animals_in_cage(id_cage)
        for animal in animals:
            print(animal)

    elif choix == '9':
        total_cage_area = zoo.get_total_cage_area()
        print("La superficie totale des cages est de {} m²".format(total_cage_area))

    else:
        print("Choix invalide.")
