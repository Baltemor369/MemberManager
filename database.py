import sqlite3 as sq
import csv
from const import *
from User import *

class Database:
    def __init__(self, filename:str)->bool:
        self.filename = filename
        try:
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {TABLE} (
                    {DB_ID} INTEGER PRIMARY KEY AUTOINCREMENT,
                    {DB_FIRST_NAME} TEXT NOT NULL,
                    {DB_LAST_NAME} TEXT NOT NULL,
                    {DB_BIRTHDAY_LAST_NAME} TEXT NOT NULL,
                    {DB_CIVILITY} TEXT NOT NULL,
                    {DB_NATIONALITY} TEXT NOT NULL,
                    {DB_BIRTHDAY} DATE NOT NULL,
                    {DB_BIRTHDAY_LOCATION} TEXT NOT NULL,
                    {DB_START_SUSCRIPTION} DATE NOT NULL,
                    {DB_END_SUSCRIPTION} DATE NOT NULL,
                    {DB_ADDRESS} TEXT NOT NULL,
                    {DB_CITY} TEXT NOT NULL,
                    {DB_ZIPCODE} INTEGER NOT NULL,
                    {DB_EMAIL} TEXT NOT NULL,
                    {DB_PHONE} TEXT NOT NULL,
                    {DB_JOB} TEXT NOT NULL,
                    {DB_RELATIONSHIP_SITUATION} TEXT NOT NULL,
                    {DB_NB_KIDS} INTEGER NOT NULL,
                    {DB_MEMBERSHIP_NUMBER} TEXT NOT NULL UNIQUE,
                    {DB_MEMBERSHIP_FONCTION} TEXT NOT NULL,
                    {DB_ACTIVITY} BOOLEAN
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
                INSERT OR IGNORE INTO {TABLE} ({User.__attr__()})
                VALUES ({"?," * (len(User.__attr__()-1))}?)
            """, data)
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

    def insert_user(self, user:User):
        try:
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute(f"""
                INSERT INTO {TABLE} ({User.__attr__()})
                VALUES ({"?," * (len(User.__attr__()-1))})
            """, ({user.__list__()})
            )
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
            cursor.execute(f"DELETE FROM {TABLE} WHERE {DB_ID} = ?", (user_id,))
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
                SET 
                WHERE {DB_ID} =?
            """, )
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