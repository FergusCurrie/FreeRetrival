import sqlite3

class SqliteConnector():
    def __init__(self) -> None:
        self.conn = sqlite3.connect('free_retrival.db')
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def query(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.fetchall()
