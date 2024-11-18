import sqlite3 as sq
import csv
from .const import *
from mods.User import *

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
                    {DB_END_SUSCRIPTION} DATE,
                    {DB_ADDRESS} TEXT NOT NULL,
                    {DB_CITY} TEXT NOT NULL,
                    {DB_ZIPCODE} INTEGER NOT NULL,
                    {DB_EMAIL} TEXT NOT NULL,
                    {DB_PHONE} TEXT NOT NULL,
                    {DB_JOB} TEXT NOT NULL,
                    {DB_RELATIONSHIP_SITUATION} TEXT NOT NULL,
                    {DB_NB_KIDS} INTEGER NOT NULL,
                    {DB_MEMBERSHIP_ID} TEXT NOT NULL UNIQUE,
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
        try:
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {TABLE}")
            data = cursor.fetchall()
            conn.close()
            return data
        except Exception as e:
            print(e)
            return []

    # Function use to save data into the database
    def save_data(self, user:User)->bool:
        try:
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute(f"""
                INSERT INTO {TABLE} ({User().__attr__()})
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (user.__list__()[1:]))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Unexpected Error : {e}")
            return False

    # Function use to select items in the database
    def get_items(self, **kwargs) -> list:
        cond = " AND ".join([f"{key} = ?" for key in kwargs.keys()])
        values = tuple(kwargs.values())
        
        try:
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {TABLE} WHERE {cond}", values)
            data = cursor.fetchall()
            conn.close()
            return data
        except Exception as e:
            print(e)
            return []


    def insert_user(self, user:User):
        try:
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute(f"""
                INSERT INTO {TABLE} ({User().__attr__()})
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
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
    
    def update_user(self, user:User):
        try:
            data = user.__list__()[1:]
            data.append(user.__list__()[0])
            conn = sq.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute(f"""
                UPDATE {TABLE}
                SET {DB_FIRST_NAME} = ?, {DB_LAST_NAME} = ?, {DB_BIRTHDAY_LAST_NAME} = ?, {DB_CIVILITY} = ?, {DB_NATIONALITY} = ?, {DB_BIRTHDAY} = ?, {DB_BIRTHDAY_LOCATION} = ?, {DB_START_SUSCRIPTION} = ?, {DB_END_SUSCRIPTION} = ?, {DB_ADDRESS} = ?, {DB_CITY} = ?, {DB_ZIPCODE} = ?, {DB_EMAIL} = ?, {DB_PHONE} = ?, {DB_JOB} = ?, {DB_RELATIONSHIP_SITUATION} = ?, {DB_NB_KIDS} = ?, {DB_MEMBERSHIP_ID} = ?, {DB_MEMBERSHIP_FONCTION} = ?, {DB_ACTIVITY} = ?
                WHERE {DB_ID} = ?
            """, data)
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
        cursor.execute(f'SELECT {DB_MEMBERSHIP_ID} FROM {TABLE}')
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
        conn.execute('PRAGMA encoding="UTF-8"')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE} WHERE {DB_ACTIVITY}='{VAL_ACTIVE}'")
        data = cursor.fetchall()
        # get column's names
        column_names = [val for key,val in ATTR.items()]

        # CSV Creation
        with open('members.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            # Write column names
            csvwriter.writerow(column_names)
            
            # Write down data
            csvwriter.writerows(data)
        conn.close()

    def import_csv(self, csv_filename):
        # connect to database
        conn = sq.connect(self.filename)
        cursor = conn.cursor()

        # read the CSV file
        with open(csv_filename, 'r', encoding='utf-8-sig') as csvfile:

            csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            column_names = next(csvreader)
            placeholders = ', '.join('?' * len(column_names))
            insert_query = f'INSERT INTO {TABLE} ({User().__attr__()}) VALUES ({placeholders})'
            for row in csvreader:
                cursor.execute(insert_query, row)
            return False

        # Sauvegarder les changements et fermer la connexion
        conn.commit()
        conn.close()
        return True