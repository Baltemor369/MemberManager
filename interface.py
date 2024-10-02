import tkinter as tk
from tkinter import ttk
from const import *

class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_NAME)
        # self.root.attributes("-fullscreen", True)
        self.root.state('zoomed')

        self.root.configure(**ROOT_STYLE)

        self.session_state = {}

        self.tree = ttk.Treeview(self.root)

        self.tree["columns"] = (FIRST_NAME, LAST_NAME, GENDER, BIRTHDAY, START_SUBSCRIBE, END_SUBSCRIBE, ADDRESS, CITY, ZIPCODE, EMAIL, PHONE, JOB, RELATIONSHIP_SITUATION, NB_KIDS,MEMBERSHIP_NUMBER, MEMBERSHIP_ROLE)
        # Définir les colonnes
        self.tree.column("#0", width=0)
        for col in self.tree["columns"]:
            self.tree.column(col, anchor=tk.CENTER, width=80)

        # Définir les en-têtes
        self.tree.heading("#0", text="", anchor=tk.CENTER)
        self.tree.heading(FIRST_NAME, text=STR_FIRST_NAME, anchor=tk.CENTER)
        self.tree.heading(LAST_NAME, text=STR_LAST_NAME, anchor=tk.CENTER)
        self.tree.heading(GENDER, text=STR_GENDER, anchor=tk.CENTER)
        self.tree.heading(BIRTHDAY, text=STR_BIRTHDAY, anchor=tk.CENTER)
        self.tree.heading(START_SUBSCRIBE, text=STR_START_SUBSCRIBE, anchor=tk.CENTER)
        self.tree.heading(END_SUBSCRIBE, text=STR_END_SUBSCRIBE, anchor=tk.CENTER)
        self.tree.heading(ADDRESS, text=STR_ADDRESS, anchor=tk.CENTER)
        self.tree.heading(CITY, text=STR_CITY, anchor=tk.CENTER)
        self.tree.heading(ZIPCODE, text=STR_ZIPCODE, anchor=tk.CENTER)
        self.tree.heading(EMAIL, text=STR_EMAIL, anchor=tk.CENTER)
        self.tree.heading(PHONE, text=STR_PHONE, anchor=tk.CENTER)
        self.tree.heading(JOB, text=STR_JOB, anchor=tk.CENTER)
        self.tree.heading(RELATIONSHIP_SITUATION, text=STR_RELATIONSHIP_SITUATION, anchor=tk.CENTER)
        self.tree.heading(NB_KIDS, text=STR_NB_KIDS, anchor=tk.CENTER)
        self.tree.heading(MEMBERSHIP_NUMBER, text=STR_MEMBERSHIP_NUMBER, anchor=tk.CENTER)
        self.tree.heading(MEMBERSHIP_ROLE, text=STR_MEMBERSHIP_ROLE, anchor=tk.CENTER)

        self.main_window()

    def main_window(self):
        # clear screen
        self.clear_window(self.root)

        # create a exit button for close the window
        frame = tk.Frame(self.root)
        frame.pack()
        exit_button = tk.Button(self.root, text=TXT_EXIT, command=self.exit, width=10, anchor=tk.CENTER, **BUTTON_STYLE)
        exit_button.pack(pady=5, padx=5, anchor="ne")

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

        # main Frame
        frame_body = tk.Frame(self.root, **ROOT_STYLE)
        frame_body.pack(padx=10, pady=10)

        # Personnal information
        frameTL = tk.LabelFrame(frame_body, text="Informations personnelle", **ROOT_STYLE)
        frameTL.pack(side="left", padx=15)

        tk.Label(frameTL, text="Prénom", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_FIRST_NAME] = tk.Entry(frameTL)
        self.session_state[STR_FIRST_NAME].pack(pady=5)
        
        tk.Label(frameTL, text="Nom", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_LAST_NAME] = tk.Entry(frameTL)
        self.session_state[STR_LAST_NAME].pack(pady=5)
        
        tk.Label(frameTL, text="Sexe", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_GENDER] = tk.Entry(frameTL)
        self.session_state[STR_GENDER].pack(pady=5)
        
        tk.Label(frameTL, text="Date Anniversaire", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_BIRTHDAY] = tk.Entry(frameTL)
        self.session_state[STR_BIRTHDAY].pack(pady=5)

        # Contact
        frameTR = tk.LabelFrame(frame_body, text="Informations de Contact", **ROOT_STYLE)
        frameTR.pack(side="left", padx=15)

        tk.Label(frameTR, text="Adresse Postale", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_ADDRESS] = tk.Entry(frameTR)
        self.session_state[STR_ADDRESS].pack(pady=5)
        
        tk.Label(frameTR, text="Ville", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_CITY] = tk.Entry(frameTR)
        self.session_state[STR_CITY].pack(pady=5)
        
        tk.Label(frameTR, text="Code Postal", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_ZIPCODE] = tk.Entry(frameTR)
        self.session_state[STR_ZIPCODE].pack(pady=5)
        
        tk.Label(frameTR, text="Email", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_EMAIL] = tk.Entry(frameTR)
        self.session_state[STR_EMAIL].pack(pady=5)
        
        tk.Label(frameTR, text="Téléphone", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_PHONE] = tk.Entry(frameTR)
        self.session_state[STR_PHONE].pack(pady=5)
        
        # Situation
        frameBL = tk.LabelFrame(frame_body, text="Situation", **ROOT_STYLE)
        frameBL.pack(side="left", padx=15)

        tk.Label(frameBL, text="Métier", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_JOB] = tk.Entry(frameBL)
        self.session_state[STR_JOB].pack(pady=5)
        
        tk.Label(frameBL, text="Situation familiale", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_RELATIONSHIP_SITUATION] = tk.Entry(frameBL)
        self.session_state[STR_RELATIONSHIP_SITUATION].pack(pady=5)
        
        tk.Label(frameBL, text="Nombre d'enfant", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_NB_KIDS] = tk.Entry(frameBL)
        self.session_state[STR_NB_KIDS].pack(pady=5)

        # Information about Association
        frameBR = tk.LabelFrame(frame_body, text="Information dans l'association", **ROOT_STYLE)
        frameBR.pack(side="left", padx=15)

        tk.Label(frameBR, text="N°adhérent", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_MEMBERSHIP_NUMBER] = tk.Entry(frameBR)
        self.session_state[STR_MEMBERSHIP_NUMBER].pack(pady=5)
        
        tk.Label(frameBR, text="Rôle", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_MEMBERSHIP_ROLE] = tk.Entry(frameBR)
        self.session_state[STR_MEMBERSHIP_ROLE].pack(pady=5)
                
        tk.Label(frameBR, text="Date d'inscription", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_START_SUBSCRIBE] = tk.Entry(frameBR)
        self.session_state[STR_START_SUBSCRIBE].pack(pady=5)
        
        tk.Label(frameBR, text="Date de sortie", **ROOT_STYLE).pack(pady=5)
        self.session_state[STR_END_SUBSCRIBE] = tk.Entry(frameBR)
        self.session_state[STR_END_SUBSCRIBE].pack(pady=5)
        
        
    
    def clear_window(self, window):
        for widget in window.winfo_children():
            widget.pack_forget()
    
    def run(self):
        self.root.mainloop()
    
    def exit(self):
        self.root.quit()