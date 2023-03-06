import sqlite3

#Création de la base de données database.db

conn = sqlite3.connect('database.db')
print("Opened database successfully")

#Création de la table user
cursor = conn.cursor()
# Création de la table user avec les champs id, username, password
cursor.execute('''DROP TABLE IF EXISTS userinfo''')
cursor.execute('''CREATE TABLE userinfo (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')