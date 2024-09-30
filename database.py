import sqlite3 as sq

# Function use to init the database ; create the table
def create_table(filename:str)->bool:
    try:
        conn = sq.connect(filename)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                gender TEXT NOT NULL,
                birthday DATE NOT NULL,
                start_subscribe_date DATE NOT NULL,
                end_subscribe_date DATE,
                address TEXT NOT NULL,
                city TEXT NOT NULL,
                zipcode INTEGER NOT NULL,
                email TEXT  NOT NULL,
                phone TEXT  NOT NULL,
                job TEXT NOT NULL,
                relationship_situation TEXT NOT NULL,
                nb_kids INTEGER NOT NULL,
                membership_number TEXT NOT NULL,
                membership_role TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
        return True
    except:
        return False

# Function use to load data from the database
def load_data(filename:str)->list:
    conn = sq.connect(filename)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    data = cursor.fetchall()
    conn.close()
    return data

# Function use to save data into the database
def save_data(filename:str, data:list)->bool:
    try:
        conn = sq.connect(filename)
        cursor = conn.cursor()
        cursor.executemany("INSERT OR IGNORE INTO members VALUES (?, ?, ?)", data)
        conn.commit()
        conn.close()
        return True
    except:
        return False