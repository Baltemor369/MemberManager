import sqlite3 as sq
import csv
from const import *

class Database:
    def __init__(self, filename:str)->bool:
        self.filename = filename
        try:
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {TABLE} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    gender TEXT NOT NULL,
                    birthday DATE NOT NULL,
                    start_subscribe_date DATE NOT NULL,
                    end_subscribe_date DATE NOT NULL,
                    address TEXT NOT NULL,
                    city TEXT NOT NULL,
                    zipcode INTEGER NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT NOT NULL UNIQUE,
                    job TEXT NOT NULL,
                    relationship_situation TEXT NOT NULL,
                    nb_kids INTEGER NOT NULL,
                    membership_number TEXT NOT NULL UNIQUE,
                    membership_role TEXT NOT NULL
                )
            """)
            conn.commit()
        except sq.Error as e:
            print(f"An error occurred: {e}")
        finally:
            if conn:
                conn.close()

    # Function use to load data from the database
    def load_data(self)->list:
        conn = sq.connect(self.filename)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE}")
        data = cursor.fetchall()
        conn.close()
        return data

    # Function use to save data into the database
    def save_data(self, data:list)->bool:
        try:
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute(f"""
                INSERT OR IGNORE INTO {TABLE} (first_name, last_name, gender, birthday, start_subscribe_date, end_subscribe_date, address, city, zipcode, email, phone, job, relationship_situation, nb_kids, membership_number, membership_role)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, data[:-1])
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False

    # Function use to select items in the database
    def get_items(self, conditions:str)->list:
        conn = sq.connect(self.filename)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE} WHERE {conditions}")
        data = cursor.fetchall()
        conn.close()
        return data

    def insert_user(self, user):
        try:
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute(f"""
                INSERT INTO {TABLE} (first_name, last_name, gender, birthday, start_subscribe_date, end_subscribe_date, address, city, zipcode, email, phone, job, relationship_situation, nb_kids, membership_number, membership_role)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (user.first_name, user.last_name, user.gender, user.birthday, user.start_suscription, user.end_suscription, user.address, user.city, user.zipcode, user.email, user.phone, user.job, user.relationship_situation, user.nb_kids, user.membership_number, user.membership_role))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Erreur lors de l'insertion de l'utilisateur : {e}")
            return False

    def delete_user(self, user_id:str)->bool:
        try:
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {TABLE} WHERE id = ?", (user_id,))
            conn.commit()
            if conn:
                conn.close()
            return True
        except sq.Error as error:
            print("Erreur lors de la suppression de l'utilisateur :", error)
            if conn:
                conn.close()
            return False
    
    def update_user(self, user):
        try:
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute(f"""
                UPDATE {TABLE}
                SET first_name =?, last_name =?, gender =?, birthday =?, start_subscribe_date =?, end_subscribe_date =?, address =?, city =?, zipcode =?, email =?, phone =?, job =?, relationship_situation =?, nb_kids =?, membership_number =?, membership_role =?
                WHERE id =?
            """, (user.first_name, user.last_name, user.gender, user.birthday, user.start_suscription, user.end_suscription, user.address, user.city, user.zipcode, user.email, user.phone, user.job, user.relationship_situation, user.nb_kids, user.membership_number, user.membership_role, user.id))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Erreur lors de la mise à jour de l'utilisateur : {e}")
            if conn:
                conn.close()
            return False
    
    def generer_identifiant(self)->str:
        conn = sq.connect(self.filename)
        cursor = conn.cursor()
        cursor.execute(f'SELECT {DB_MEMBERSHIP_NUMBER} FROM {TABLE}')
        ids = cursor.fetchall()
        conn.close()

        if not ids:
            return '0001'
        else:
            ids = [int(id[0]) for id in ids]
            new_id = max(ids) + 1
            return f'{new_id:04d}'
    
    def export_csv(self):
        conn = sq.connect(self.filename)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE}")
        data = cursor.fetchall()
        # get column's names
        column_names = [description[0] for description in cursor.description]

        # CSV Creation
        with open('members.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            
            # Write column names
            csvwriter.writerow(column_names)
            
            # Write down data
            csvwriter.writerows(data)
        conn.close()