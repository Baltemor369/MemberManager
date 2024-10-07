import sqlite3 as sq
from const import *

class Database:
    def __init__(self, filename:str)->bool:
        self.filename = filename
        try:
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS {TABLE} (
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
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    job TEXT NOT NULL,
                    relationship_situation TEXT NOT NULL,
                    nb_kids INTEGER NOT NULL,
                    membership_number TEXT NOT NULL,
                    membership_role TEXT NOT NULL
                )
            """)
            conn.commit()
            return True
        except sq.Error as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            if conn:
                conn.close()

    # Function use to load data from the database
    def load_data(self)->list:
        conn = sq.connect(self.filename)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM {TABLE}")
        data = cursor.fetchall()
        conn.close()
        return data

    # Function use to save data into the database
    def save_data(self, filename:str, data:list)->bool:
        try:
            conn = sq.connect(filename)
            cursor = conn.cursor()
            cursor.executemany("INSERT OR IGNORE INTO {TABLE} VALUES (?, ?, ?)", data)
            conn.commit()
            conn.close()
            return True
        except:
            return False

    # Function use to select items in the database
    def get_items(self, filename:str, conditions:str)->list:
        conn = sq.connect(filename)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE} WHERE {conditions}")
        data = cursor.fetchall()
        conn.close()
        return data

    def insert_user(self, conn, user):
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO {TABLE} (first_name, last_name, gender, birthday, start_subscribe_date, end_subscribe_date, address, city, zipcode, email, phone, job, relationship_situation, nb_kids, membership_number, membership_role)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (user.first_name, user.last_name, user.gender, user.birthday, user.start_suscription, user.end_suscription, user.address, user.city, user.zipcode, user.email, user.phone, user.job, user.relationship_situation, user.nb_kids, user.membership_number, user.membership_role))
        conn.commit()

    def delete_user(self, conn, user_id):
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM {TABLE} WHERE id = ?", (user_id,))
            conn.commit()
            return True
        except sq.Error as error:
            print("Erreur lors de la suppression de l'utilisateur :", error)
            return False