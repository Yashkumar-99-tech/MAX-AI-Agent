import sqlite3

class MemoryDB:

    def __init__(self):

        self.connection = sqlite3.connect(
            "memory/memory.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS memories(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,

            content TEXT

        )

        """)

        self.connection.commit()

    def save_memory(self, title, content):

        self.cursor.execute(

            "INSERT INTO memories(title,content) VALUES(?,?)",

            (title, content)

        )

        self.connection.commit()

    def get_memory(self, title):

        self.cursor.execute(

            "SELECT content FROM memories WHERE title=? ORDER BY id DESC LIMIT 1",

            (title,)

        )

        data = self.cursor.fetchone()

        if data:

            return data[0]

        return None

    def delete_memory(self, title):

        self.cursor.execute(

            "DELETE FROM memories WHERE title=?",

            (title,)

        )

        self.connection.commit()

    def get_all(self):

        self.cursor.execute(

            "SELECT title,content FROM memories"

        )

        return self.cursor.fetchall()