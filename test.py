import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="", host="127.0.0.1", port="5432")

print("Opened database successfully")