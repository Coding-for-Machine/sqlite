import sqlite3

def connect():
    return sqlite3.connect("test.db")

def create_user():
    conn = connect()
    cursor = conn.cursor()
    user_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(150) NOT NULL,
        password VARCHAR(150) NOT NULL,
        is_admin BOOLEAN DEFAULT FALSE
    )
    '''
    cursor.execute(user_table)
    conn.commit()
    conn.close()

def create_category():
    conn = connect()
    cursor = conn.cursor()
    category_table = '''
    CREATE TABLE IF NOT EXISTS category(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL
    )
    '''
    cursor.execute(category_table)
    conn.commit()
    conn.close()

def create_course():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS course(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(150) NOT NULL,
        body TEXT,
        is_active BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP,
        updated_at TIMESTAMP     
    )
    ''')
    conn.commit()
    conn.close()

def user_course_enrole():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_course_enrole(
        user_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY(user_id, course_id),
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(course_id) REFERENCES course(id)
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_course()
    user_course_enrole()
    create_category()
    create_user()
