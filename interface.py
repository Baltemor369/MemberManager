import tkinter as tk
import re
import datetime 
from tkinter import ttk
from const import *
from User import User
from database import Database

class Interface:
    def __init__(self):
        self.db = Database("members.db")
        self.root = tk.Tk()
        self.root.title(APP_NAME)
        
        self.root.state('zoomed')

        self.root.configure(**ROOT_STYLE)

        self.session_state = {}
        self.session_state[KEY_ALERT] = ("", None)

        self.tree = ttk.Treeview(self.root)

        user = User("John", "Doe", "M", "1990-01-01", "2023-01-01", "2024-01-01", "123 Main St", "City", "12345", "john.doe@example.com", "1234567890", "Engineer", "Single", 0, "0001", "Member")
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

        alert_label = tk.Label(alert_frame, text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1], **ALERT_STYLE)
        alert_label.pack(pady=5)

        # update tree data
        for elt in self.db.load_data():
            self.tree.insert("", tk.END, values=elt)

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
        back_button = tk.Button(self.root, text=TXT_BACK, command=self.back, width=10, anchor=tk.CENTER, **BUTTON_STYLE)
        back_button.pack(pady=5, padx=5, anchor="ne")

        # Alert Frame to display a specific message
        alert_frame = tk.Frame(self.root, **ROOT_STYLE)
        alert_frame.pack(padx=10, pady=10)

        self.alert_label = tk.Label(alert_frame, text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1], **ALERT_STYLE)
        self.alert_label.pack(pady=5)

        # main Frame
        frame_body = tk.Frame(self.root, **ROOT_STYLE)
        frame_body.pack(padx=10, pady=10)

        # Personnal information
        frameTL = tk.LabelFrame(frame_body, text="Informations personnelle", **ROOT_STYLE)
        frameTL.pack(side="left", padx=15)

        tk.Label(frameTL, text="Prénom", **LABEL_STYLE).pack(pady=5)
        first_name_entry = tk.Entry(frameTL)
        first_name_entry.pack(pady=5)

        tk.Label(frameTL, text="Nom", **LABEL_STYLE).pack(pady=5)
        last_name_entry = tk.Entry(frameTL)
        last_name_entry.pack(pady=5)

        tk.Label(frameTL, text="Genre", **LABEL_STYLE).pack(pady=5)
        gender_entry = ttk.Combobox(frameTL, values=LIST_GENDER, width=8)
        gender_entry.current(0)
        gender_entry.pack(pady=5)

        tk.Label(frameTL, text="Date Anniversaire", **ROOT_STYLE).pack(pady=5)
        birthday_entry = tk.Entry(frameTL)
        birthday_entry.pack(pady=5)

        # Informations de Contact
        frameTR = tk.LabelFrame(frame_body, text="Informations de Contact", **ROOT_STYLE)
        frameTR.pack(side="left", padx=15)

        tk.Label(frameTR, text="Adresse Postale", **LABEL_STYLE).pack(pady=5)
        address_entry = tk.Entry(frameTR)
        address_entry.pack(pady=5)

        tk.Label(frameTR, text="Ville", **LABEL_STYLE).pack(pady=5)
        city_entry = tk.Entry(frameTR)
        city_entry.pack(pady=5)

        tk.Label(frameTR, text="Code Postal", **LABEL_STYLE).pack(pady=5)
        zipcode_entry = tk.Entry(frameTR)
        zipcode_entry.pack(pady=5)

        tk.Label(frameTR, text="Email", **LABEL_STYLE).pack(pady=5)
        email_entry = tk.Entry(frameTR)
        email_entry.pack(pady=5)

        tk.Label(frameTR, text="Téléphone", **LABEL_STYLE).pack(pady=5)
        phone_entry = tk.Entry(frameTR)
        phone_entry.pack(pady=5)

        # Situation
        frameBL = tk.LabelFrame(frame_body, text="Situation", **ROOT_STYLE)
        frameBL.pack(side="left", padx=15)

        tk.Label(frameBL, text="Métier", **LABEL_STYLE).pack(pady=5)
        job_entry = tk.Entry(frameBL)
        job_entry.pack(pady=5)

        tk.Label(frameBL, text="Situation familiale", **LABEL_STYLE).pack(pady=5)
        relationship_situation_entry = ttk.Combobox(frameBL, values=LIST_RELATIONSHIP, width=10)
        relationship_situation_entry.current(0)
        relationship_situation_entry.pack(pady=5)

        tk.Label(frameBL, text="Nombre d'enfant", **LABEL_STYLE).pack(pady=5)
        nb_kids_entry = ttk.Combobox(frameBL, values=list(range(0,21)), width=5)
        nb_kids_entry.current(0)
        nb_kids_entry.pack(pady=5)

        # Information dans l'association
        frameBR = tk.LabelFrame(frame_body, text="Information dans l'association", **ROOT_STYLE)
        frameBR.pack(side="left", padx=15)

        tk.Label(frameBR, text="N°adhérent", **LABEL_STYLE).pack(pady=5)
        membership_number_entry = tk.Entry(frameBR)
        membership_number_entry.pack(pady=5)

        tk.Label(frameBR, text="Rôle", **LABEL_STYLE).pack(pady=5)
        membership_role_entry = ttk.Combobox(frameBR, values=LIST_ROLE, width=12)
        membership_role_entry.current(0)
        membership_role_entry.pack(pady=5)

        tk.Label(frameBR, text="Date d'inscription", **LABEL_STYLE).pack(pady=5)
        start_suscription_entry = tk.Entry(frameBR)
        start_suscription_entry.pack(pady=5)

        tk.Label(frameBR, text="Date de sortie", **LABEL_STYLE).pack(pady=5)
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

    # Get & Verify inputs, if all rights, it's added to the database
    def add_client(self, user:User):
        ## verify inputs format
        # check firstname and lastname is only with letters
        if not user.first_name.isalpha() or not user.last_name.isalpha():
            self.session_state[KEY_ALERT] = (MSG_INVALID_NAME, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        #check gender : H/F
        if user.gender not in LIST_GENDER:
            self.session_state[KEY_ALERT] = (MSG_INVALID_GENDER, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        # check birthday format : DD-MM-YYYY
        try:
            datetime.datetime.strptime(user.birthday, "%d-%m-%Y")
        except:
            self.session_state[KEY_ALERT] = (MSG_INVALID_BIRTHDAY, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        # check date start & end subscribe
        try:
            datetime.datetime.strptime(user.start_suscription, "%d-%m-%Y")
            datetime.datetime.strptime(user.end_suscription, "%d-%m-%Y")
        except :
            self.session_state[KEY_ALERT] = (MSG_INVALID_SUSCRIPTION, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        # check address not empty
        if not user.address:
            self.session_state[KEY_ALERT] = (MSG_INVALID_ADDRESS, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        # check city : not empty
        if not user.city:
            self.session_state[KEY_ALERT] = (MSG_INVALID_CITY, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        # check zipcode : 5 digits
        if len(user.zipcode)!= 5 or not user.zipcode.isdigit():
            self.session_state[KEY_ALERT] = (MSG_INVALID_ZIPCODE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        # check email format : valid email
        if not re.match(REGEX_EMAIL, user.email):
            self.session_state[KEY_ALERT] = (MSG_INVALID_EMAIL, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        # check phone number format : 10 digits
        if len(user.phone)!= 10 or not user.phone.isdigit():
            self.session_state[KEY_ALERT] = (MSG_INVALID_PHONE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        # check job : not empty
        if not user.job:
            self.session_state[KEY_ALERT] = (MSG_INVALID_JOB, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        # check relationship situation : not empty
        if not user.relationship_situation:
            self.session_state[KEY_ALERT] = (MSG_INVALID_RELATIONSHIP, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
        # check number of kids : not empty
        if not user.nb_kids:
            self.session_state[KEY_ALERT] = (MSG_INVALID_KIDS, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        # check membership number : not empty
        if not user.membership_number:
            self.session_state[KEY_ALERT] = (MSG_INVALID_MEMBERSHIP, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        # check membership role : not empty
        if not user.membership_role:
            self.session_state[KEY_ALERT] = (MSG_INVALID_ROLE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        
        # add the person to the database
        self.db.save_data(user.__list__())

        # All succeeded, return to the main menu
        self.session_state[KEY_ALERT] = (MSG_ADD_SUCCESS, GREEN)
        self.main_window()
        
    # undisplay widgets in window (not destroy)
    def clear_window(self, window):
        for widget in window.winfo_children():
            widget.pack_forget()
    
    # start the main application loop
    def run(self):
        self.root.mainloop()
    
    def back(self):
        self.session_state[KEY_ALERT]=("","#000000")
        self.main_window()
    # exit the app and all other process need to be stop separately
    def exit(self):
        self.root.quit()