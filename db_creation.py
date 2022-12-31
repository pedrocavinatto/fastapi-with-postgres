from database import Database
import os

#Env variables
db_name = os.environ['POSTGRES_DB']
db_user = os.environ['POSTGRES_USER']
db_password = os.environ['POSTGRES_PASSWORD']
db_host = os.environ['POSTGRES_HOST']
db_port = os.environ['POSTGRES_PORT']

try:
    db = Database(db_name, db_user, db_password, db_host, db_port);
    cursor = db.connect()
    cursor.execute("CREATE TABLE users (id SERIAL NOT NULL, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, age INTEGER);")
    db.close()
except Exception as e:
    print(e.args)
