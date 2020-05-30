import psycopg2

con = psycopg2.connect(database="MusicStore", user="postgres", password="postgres", host="127.0.0.1", port="5432")

cursor = con.cursor()
cursor.execute("SELECT * FROM Band")
rows = cursor.fetchall()

for row in rows:
  print(row)
