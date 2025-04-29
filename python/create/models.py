import sqlite3


def create_user_table():
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   email VARCHAR(250) NOT NULL,
                   last_login DATE,
                   is_supperuser BOOLEAN DEFAULT FALSE,
                   roule VARCHAR(150),
                   is_active BOOLEAN DEFAULT TRUE,
                   is_staff BOOLEAN DEFAULT FALSE,
                   created_at TIMESTAMP,
                   updated_at TIMESTAMP
                   )
    ''')
    conn.commit()
    conn.close()


# owner 1:N
def create_course_table():
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name VARCHAR(250) NOT NULL,
                   body TEXT,
                   owner_id INTEGER NOT NULL,
                   is_active BOOLEAN DEFAULT TRUE,
                   created_at TIMESTAMP,
                   updated_at TIMESTAMP,
                   FOREIGN KEY(owner_id) REFERENCES users(id)
                   )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_user_table()
    create_course_table()