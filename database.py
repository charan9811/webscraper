import sqlite3

class database:
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        self.create_table()


    def create_table(self):

        self.cur.execute("""  CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY,
                URL TEXT,
                headline TEXT,
                author TEXT,
                date TEXT
            )
        """)


    def fill_data(self, _id, data):
        self.cur.execute("INSERT INTO articles VALUES(?, ?, ?, ?, ?)", (_id, data['URL'], data['headline'],
                                                                data['author'], data['date']))
        self.con.commit()

    def find_data(self, headline):
        res = self.cur.execute("SELECT headline FROM articles WHERE headline=?", (headline,))
        return res.fetchone() is None

    def send_data(self):
        result = self.cur.execute("SELECT * FROM articles")
        return result

    def close_connection(self):
        self.con.close()