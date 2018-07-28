import mysql.connector

connection=mysql.connector.connect(host='localhost')
cur=connection.cursor()
cur.execute('create database testone')
connection.commit()
cur.close()
