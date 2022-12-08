
import psycopg2

class Database:
    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                database=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port
            )
            self.conn.autocommit = True
            self.cur = self.conn.cursor()
            return self.cur
        except psycopg2.Error as e:
            print("Error while connecting to PostgreSQL", e)

    def close(self):
        self.cur.close()
        self.conn.close()