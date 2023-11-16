# Importation des modules nécessaires
import psycopg2 # pour se connecter à la base de données postgresql
import pandas as pd # pour manipuler les données
import numpy as np # pour générer des nombres aléatoires
import faker # pour générer des données fictives
import random # pour générer aléatoirement des données
import time # pour manipuler des dates

# Création d'un objet faker avec la langue française
fake = faker.Faker('fr_FR')

# Connexion à la base de données
conn = psycopg2.connect(database="postgres", user="postgres", password="Z1632522yde", host="localhost", port="5432")

# Création d'un curseur pour exécuter des requêtes SQL
cur = conn.cursor()

# Création de listes vides pour stocker les données aléatoires
clients = []
articles = []
collectes = []
csps = []

# Génération de 1000 clients aléatoires
for i in range(1000):
  # Génération d'un identifiant client unique
  id_client = i + 1
  # Génération d'un nom aléatoire
  nom = fake.last_name()
  # Génération d'un prénom aléatoire
  prenom = fake.first_name()
  # Génération d'un mail aléatoire
  mail = fake.email()
  # Génération d'un nombre d'enfants aléatoire entre 0 et 5
  nombre_enfant = np.random.randint(0, 6)
  # Génération d'une ville aléatoire
  ville = fake.city()
  # Génération d'un identifiant collecte aléatoire entre 1 et 1000
  id_collecte = np.random.randint(1, 1001)
  # Ajout du client à la liste des clients
  clients.append((id_client, nom, prenom, mail, nombre_enfant, ville, id_collecte))

# Génération de 1000 articles aléatoires
for i in range(1000):
  # Génération d'un identifiant article unique
  id_article = i + 1
  # Génération d'une description aléatoire
  description = fake.sentence()
  # Génération d'un prix unitaire aléatoire entre 1 et 100 euros
  prix_unitaire = np.random.uniform(1, 100)
  # Génération d'une catégorie achat aléatoire entre 1 et 10
  categorie_achat = np.random.randint(1, 11)
  # Ajout de l'article à la liste des articles
  articles.append((id_article, description, prix_unitaire, categorie_achat))

# Génération de 1000 passages caisse aléatoires
for i in range(1000):
  # Génération d'un identifiant collecte unique
  id_collecte = i + 1
  # Génération d'un prix catégorie aléatoire entre 1 et 10 euros
  prix_categorie = np.random.uniform(1, 10)
  # Génération d'une date de passage caisse aléatoire entre le 1er janvier 2022 et le 31 décembre 2023
  def str_time_prop(start, end, time_format, prop):

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

  def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d %I:%M %p', prop)
      
  date_passage_caisse = random_date("2022-1-1 1:30 PM", "2023-12-31 4:50 AM", random.random())
  # Génération d'un montant achat aléatoire entre 1 et 1000 euros
  montant_achat = np.random.uniform(1, 1000)
  # Génération d'un identifiant client aléatoire entre 1 et 1000
  id_client = np.random.randint(1, 1001)
  # Génération d'un identifiant article aléatoire entre 1 et 1000
  id_article = np.random.randint(1, 1001)
  # Ajout du passage caisse à la liste des passages caisse
  collectes.append((id_collecte, prix_categorie, date_passage_caisse, montant_achat, id_client, id_article))

# Génération de 1000 csp aléatoires
for i in range(1000):
  # Génération d'une classe socio-professionnelle aléatoire parmi une liste de 10 possibilités
  csp = np.random.choice(['Agriculteurs exploitants', 'Artisans, commerçants, chefs d\'entreprise', 'Cadres et professions intellectuelles supérieures', 'Professions intermédiaires', 'Employés', 'Ouvriers', 'Retraités', 'Sans activité professionnelle', 'Etudiants', 'Autres'])
  # Génération d'un identifiant client aléatoire entre 1 et 1000
  id_client = np.random.randint(1, 1001)
  # Ajout de la csp à la liste des csp
  csps.append((csp, id_client))

# Conversion des listes en dataframes pandas
df_clients = pd.DataFrame(clients, columns=['identifiant_client', 'nom', 'prenom', 'mail', 'nombre_enfant', 'ville', 'identifiant_collecte'])
df_articles = pd.DataFrame(articles, columns=['identifiant_article', 'description', 'prix_unitaire', 'categorie_achat'])
df_collectes = pd.DataFrame(collectes, columns=['identifiant_collecte', 'prix_categorie', 'date_passage_caisse', 'montant_achat', 'identifiant_client', 'identifiant_article'])
df_csps = pd.DataFrame(csps, columns=['classe_socio_professionnelle', 'identifiant_client'])

# Insertion des données dans les tables de la base de données
df_clients.to_csv('client', sep='\t', encoding='utf-8')
df_articles.to_csv('article', sep='\t', encoding='utf-8')
df_collectes.to_csv('collecte', sep='\t', encoding='utf-8')
df_csps.to_csv('csp', sep='\t', encoding='utf-8')

# Fermeture du curseur et de la connexion
cur.close()
conn.close()