from app.database.connect import connect
import sqlite3

# user models
def users_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(150) UNIQUE NOT NULL,
                    password VARCHAR(100) NOT NULL,
                    id_admin BOOLEAN DEFAULT TRUE
                    )''')
    conn.commit()
    conn.close()

def user_create(username, password):
    if username and password:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password))
        conn.commit()
        conn.close()
    
if __name__ in "__main__":
    users_table()
    user_create("Asadbek", "Asadbek")