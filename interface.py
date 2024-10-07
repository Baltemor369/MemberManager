import tkinter as tk
import re
from tkinter import ttk
from const import *
from User import User
from database import Database

class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_NAME)
        
        self.root.state('zoomed')

        self.root.configure(**ROOT_STYLE)

        self.session_state = {}
        self.session_state[KEY_ALERT] = ("", None)

        self.tree = ttk.Treeview(self.root)

        user = User("John", "Doe", "M", "1990-01-01", "2023-01-01", "2024-01-01", "123 Main St", "City", "12345", "john.doe@example.com", "1234567890", "Engineer", "Single", 0, "123456", "Member")
        attributes = list(user.__dict__.keys())

        self.tree["columns"] = attributes
        # Définir les colonnes & entêtes
        self.tree.column("#0", width=0)
        self.tree.heading("#0", text="", anchor=tk.CENTER)
        for col in attributes:
            self.tree.column(col, anchor=tk.CENTER, width=80)
            self.tree.heading(col, text=col.replace("_"," "), anchor=tk.CENTER)

        self.main_window()

    def main_window(self):
        # clear screen
        self.clear_window(self.root)

        # create a exit button for close the window
        frame = tk.Frame(self.root)
        frame.pack()
        exit_button = tk.Button(self.root, text=TXT_EXIT, command=self.exit, width=10, anchor=tk.CENTER, **BUTTON_STYLE)
        exit_button.pack(pady=5, padx=5, anchor="ne")

        # Alert Frame to display a specific message
        alert_frame = tk.Frame(self.root, **ROOT_STYLE)
        alert_frame.pack(padx=10, pady=10)

        alert_label = tk.Label(alert_frame, text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1], **ROOT_STYLE)
        alert_label.pack(pady=5)

        # update tree data

        # data table
        self.tree.pack()

        # add button
        add_button = tk.Button(self.root, text=TXT_ADD, command=self.add_window, width=10, anchor=tk.CENTER, **BUTTON_STYLE)
        add_button.pack(pady=5, padx=5)
    
    def add_window(self):
        # clear screen
        self.clear_window(self.root)

        # create a exit button for close the window
        frame = tk.Frame(self.root)
        frame.pack()
        back_button = tk.Button(self.root, text=TXT_BACK, command=self.main_window, width=10, anchor=tk.CENTER, **BUTTON_STYLE)
        back_button.pack(pady=5, padx=5, anchor="ne")

        # Alert Frame to display a specific message
        alert_frame = tk.Frame(self.root, **ROOT_STYLE)
        alert_frame.pack(padx=10, pady=10)

        alert_label = tk.Label(alert_frame, text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1], **ROOT_STYLE)
        alert_label.pack(pady=5)

        # main Frame
        frame_body = tk.Frame(self.root, **ROOT_STYLE)
        frame_body.pack(padx=10, pady=10)

        # Personnal information
        frameTL = tk.LabelFrame(frame_body, text="Informations personnelle", **ROOT_STYLE)
        frameTL.pack(side="left", padx=15)

        tk.Label(frameTL, text="Prénom", **ROOT_STYLE).pack(pady=5)
        first_name_entry = tk.Entry(frameTL)
        first_name_entry.pack(pady=5)

        tk.Label(frameTL, text="Nom", **ROOT_STYLE).pack(pady=5)
        last_name_entry = tk.Entry(frameTL)
        last_name_entry.pack(pady=5)

        tk.Label(frameTL, text="Sexe", **ROOT_STYLE).pack(pady=5)
        gender_entry = tk.Entry(frameTL)
        gender_entry.pack(pady=5)

        tk.Label(frameTL, text="Date Anniversaire", **ROOT_STYLE).pack(pady=5)
        birthday_entry = tk.Entry(frameTL)
        birthday_entry.pack(pady=5)

        # Informations de Contact
        frameTR = tk.LabelFrame(frame_body, text="Informations de Contact", **ROOT_STYLE)
        frameTR.pack(side="left", padx=15)

        tk.Label(frameTR, text="Adresse Postale", **ROOT_STYLE).pack(pady=5)
        address_entry = tk.Entry(frameTR)
        address_entry.pack(pady=5)

        tk.Label(frameTR, text="Ville", **ROOT_STYLE).pack(pady=5)
        city_entry = tk.Entry(frameTR)
        city_entry.pack(pady=5)

        tk.Label(frameTR, text="Code Postal", **ROOT_STYLE).pack(pady=5)
        zipcode_entry = tk.Entry(frameTR)
        zipcode_entry.pack(pady=5)

        tk.Label(frameTR, text="Email", **ROOT_STYLE).pack(pady=5)
        email_entry = tk.Entry(frameTR)
        email_entry.pack(pady=5)

        tk.Label(frameTR, text="Téléphone", **ROOT_STYLE).pack(pady=5)
        phone_entry = tk.Entry(frameTR)
        phone_entry.pack(pady=5)

        # Situation
        frameBL = tk.LabelFrame(frame_body, text="Situation", **ROOT_STYLE)
        frameBL.pack(side="left", padx=15)

        tk.Label(frameBL, text="Métier", **ROOT_STYLE).pack(pady=5)
        job_entry = tk.Entry(frameBL)
        job_entry.pack(pady=5)

        tk.Label(frameBL, text="Situation familiale", **ROOT_STYLE).pack(pady=5)
        relationship_situation_entry = tk.Entry(frameBL)
        relationship_situation_entry.pack(pady=5)

        tk.Label(frameBL, text="Nombre d'enfant", **ROOT_STYLE).pack(pady=5)
        nb_kids_entry = tk.Entry(frameBL)
        nb_kids_entry.pack(pady=5)

        # Information dans l'association
        frameBR = tk.LabelFrame(frame_body, text="Information dans l'association", **ROOT_STYLE)
        frameBR.pack(side="left", padx=15)

        tk.Label(frameBR, text="N°adhérent", **ROOT_STYLE).pack(pady=5)
        membership_number_entry = tk.Entry(frameBR)
        membership_number_entry.pack(pady=5)

        tk.Label(frameBR, text="Rôle", **ROOT_STYLE).pack(pady=5)
        membership_role_entry = tk.Entry(frameBR)
        membership_role_entry.pack(pady=5)

        tk.Label(frameBR, text="Date d'inscription", **ROOT_STYLE).pack(pady=5)
        start_suscription_entry = tk.Entry(frameBR)
        start_suscription_entry.pack(pady=5)

        tk.Label(frameBR, text="Date de sortie", **ROOT_STYLE).pack(pady=5)
        end_suscription_entry = tk.Entry(frameBR)
        end_suscription_entry.pack(pady=5)

        # get inputs from Entry to init a User Object and send it to the self.add_client function
        tk.Button(self.root, text=TXT_ADD, command=lambda : self.add_client( User(
            first_name_entry.get(),
            last_name_entry.get(),
            gender_entry.get(),
            birthday_entry.get(),
            address_entry.get(),
            city_entry.get(),
            zipcode_entry.get(),
            email_entry.get(),
            phone_entry.get(),
            job_entry.get(),
            relationship_situation_entry.get(),
            nb_kids_entry.get(),
            membership_number_entry.get(),
            membership_role_entry.get(),
            start_suscription_entry.get(),
            end_suscription_entry.get()
            )
        )).pack(pady=5)

    def add_client(self, user:User):
        print(user.first_name)

        # verify inputs format
        # check person doesn't already exist
        # add the person to the database

        # All succeeded, return to the main menu
        self.session_state[KEY_ALERT] = ("Person successfully added", GREEN)
        self.main_window()
        
    
    def clear_window(self, window):
        for widget in window.winfo_children():
            widget.pack_forget()
    
    def run(self):
        self.root.mainloop()
    
    def exit(self):
        self.root.quit()