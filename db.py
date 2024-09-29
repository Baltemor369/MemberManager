import sqlite3 as sq


def create_table(filename:str):
    conn = sq.connect(filename)
    cursor = conn.cursor()
    # create table with : first name, last name, sexe, birthday, start subscribe date, end subscribe date, address, email, phone, job, relationship situation
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            sexe TEXT NOT NULL,
            birthday TEXT NOT NULL,
            start_subscribe_date TEXT NOT NULL,
            end_subscribe_date TEXT,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            zipcode NUMBER NOT NULL,
            email TEXT  NOT NULL,
            phone TEXT  NOT NULL,
            job TEXT NOT NULL,
            relationship_situation TEXT
        )
    """)
    conn.commit()
    conn.close()

def load_data(filename:str)->list:
    conn = sq.connect(filename)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    data = cursor.fetchall()
    conn.close()
    return data

def save_data(filename:str, data:list):
    conn = sq.connect(filename)
    cursor = conn.cursor()
    cursor.executemany("INSERT OR IGNORE INTO members VALUES (?, ?, ?)", data)
    conn.commit()
    conn.close()