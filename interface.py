import tkinter as tk
import re
import datetime 
from tkinter import ttk
from const import *
from User import User
from database import Database

class Interface:
    def __init__(self):
        self.db = Database(FILENAME)
        self.root = tk.Tk()
        self.root.title(APP_NAME)
        
        self.root.state('zoomed')

        self.root.configure(**ROOT_STYLE)

        self.session_state = {}
        self.session_state[KEY_ALERT] = ("", None)
        self.session_state[KEY_FORM] = ""
        self.session_state[ID]=""
        self.session_state[FIRST_NAME]=""
        self.session_state[LAST_NAME]=""
        self.session_state[GENDER]=""
        self.session_state[BIRTHDAY]=""
        self.session_state[START_SUSCRIPTION]=""
        self.session_state[END_SUSCRIPTION]=""
        self.session_state[ADDRESS]=""
        self.session_state[CITY]=""
        self.session_state[ZIPCODE]=""
        self.session_state[EMAIL]=""
        self.session_state[PHONE]=""
        self.session_state[JOB]=""
        self.session_state[RELATIONSHIP_SITUATION]=""
        self.session_state[NB_KIDS]=""
        self.session_state[MEMBERSHIP_NUMBER]=""
        self.session_state[MEMBERSHIP_ROLE]=""

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
        exit_button = tk.Button(self.root, text=TXT_EXIT, command=self.exit, anchor=tk.CENTER, **BUTTON_STYLE)
        exit_button.pack(pady=5, padx=5, anchor="ne")

        # Alert Frame to display a specific message
        alert_frame = tk.Frame(self.root, **ROOT_STYLE)
        alert_frame.pack(padx=10, pady=10)

        self.alert_label = tk.Label(alert_frame, text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1], **ALERT_STYLE)
        self.alert_label.pack(pady=5)

        # clear treeview data
        self.tree.delete(*self.tree.get_children())

        # update tree data
        for elt in self.db.load_data():
            self.tree.insert("", tk.END, values=elt)

        # data table
        self.tree.pack()

        # add button
        add_button = tk.Button(self.root, text=TXT_ADD, command=self.add_window, anchor=tk.CENTER, **BUTTON_STYLE)
        add_button.pack(pady=5, padx=5)
        
        # del button
        del_button = tk.Button(self.root, text=TXT_DEL, command=self.del_client, anchor=tk.CENTER, **BUTTON_STYLE)
        del_button.pack(pady=5, padx=5)
        
        # modify button
        modify_button = tk.Button(self.root, text=TXT_MODIFY, command=self.modify_window, anchor=tk.CENTER, **BUTTON_STYLE)
        modify_button.pack(pady=5, padx=5)
    
    def add_window(self):
        # clear screen
        self.clear_window(self.root)

        # create a exit button for close the window
        frame = tk.Frame(self.root)
        frame.pack()
        back_button = tk.Button(self.root, text=TXT_BACK, command=self.back, anchor=tk.CENTER, **BUTTON_STYLE)
        back_button.pack(pady=5, padx=5, anchor="ne")

        # Alert Frame to display a specific message
        alert_frame = tk.Frame(self.root, **ROOT_STYLE)
        alert_frame.pack(padx=10, pady=10)

        self.alert_label.configure(text="")
        self.alert_label.pack(pady=5)

        # main Frame
        frame_body = tk.Frame(self.root, **ROOT_STYLE)
        frame_body.pack(padx=10, pady=10)

        # Personnal information
        frameTL = tk.LabelFrame(frame_body, text="Informations personnelle", **ROOT_STYLE)
        frameTL.pack(side="left", padx=15)

        tk.Label(frameTL, text="Prénom", **LABEL_STYLE).pack(pady=5)
        first_name_entry = tk.Entry(frameTL)
        first_name_entry.insert(0, self.session_state[FIRST_NAME])
        first_name_entry.pack(pady=5)

        tk.Label(frameTL, text="Nom", **LABEL_STYLE).pack(pady=5)
        last_name_entry = tk.Entry(frameTL)
        last_name_entry.insert(0, self.session_state[LAST_NAME])
        last_name_entry.pack(pady=5)

        tk.Label(frameTL, text="Genre", **LABEL_STYLE).pack(pady=5)
        gender_entry = ttk.Combobox(frameTL, values=LIST_GENDER, width=8)
        if self.session_state[GENDER]:
            gender_entry.current(LIST_GENDER.index(self.session_state[GENDER]))
        else:
            gender_entry.current(0)
        gender_entry.pack(pady=5)

        tk.Label(frameTL, text="Date Anniversaire", **LABEL_STYLE).pack(pady=5)
        birthday_entry = tk.Entry(frameTL)
        birthday_entry.insert(0, self.session_state[BIRTHDAY])
        birthday_entry.pack(pady=5)

        # Informations de Contact
        frameTR = tk.LabelFrame(frame_body, text="Informations de Contact", **ROOT_STYLE)
        frameTR.pack(side="left", padx=15)

        tk.Label(frameTR, text="Adresse Postale", **LABEL_STYLE).pack(pady=5)
        address_entry = tk.Entry(frameTR)
        address_entry.insert(0, self.session_state[ADDRESS])
        address_entry.pack(pady=5)

        tk.Label(frameTR, text="Ville", **LABEL_STYLE).pack(pady=5)
        city_entry = tk.Entry(frameTR)
        city_entry.insert(0, self.session_state[CITY])
        city_entry.pack(pady=5)

        tk.Label(frameTR, text="Code Postal", **LABEL_STYLE).pack(pady=5)
        zipcode_entry = tk.Entry(frameTR)
        zipcode_entry.insert(0, self.session_state[ZIPCODE])
        zipcode_entry.pack(pady=5)

        tk.Label(frameTR, text="Email", **LABEL_STYLE).pack(pady=5)
        email_entry = tk.Entry(frameTR)
        email_entry.insert(0, self.session_state[EMAIL])
        email_entry.pack(pady=5)

        tk.Label(frameTR, text="Téléphone", **LABEL_STYLE).pack(pady=5)
        phone_entry = tk.Entry(frameTR)
        phone_entry.pack(pady=5)

        # Situation
        frameBL = tk.LabelFrame(frame_body, text="Situation", **ROOT_STYLE)
        frameBL.pack(side="left", padx=15)

        tk.Label(frameBL, text="Métier", **LABEL_STYLE).pack(pady=5)
        job_entry = tk.Entry(frameBL)
        job_entry.insert(0, self.session_state[JOB])
        job_entry.pack(pady=5)

        tk.Label(frameBL, text="Situation familiale", **LABEL_STYLE).pack(pady=5)
        relationship_situation_entry = ttk.Combobox(frameBL, values=LIST_RELATIONSHIP, width=10)
        if self.session_state[GENDER]:
            relationship_situation_entry.current(LIST_RELATIONSHIP.index(self.session_state[GENDER]))
        else:
            relationship_situation_entry.current(0)
        relationship_situation_entry.pack(pady=5)

        tk.Label(frameBL, text="Nombre d'enfant", **LABEL_STYLE).pack(pady=5)
        nb_kids_entry = ttk.Combobox(frameBL, values=list(range(0,21)), width=5)
        if self.session_state[GENDER]:
            nb_kids_entry.current(self.session_state[NB_KIDS])
        else:
            nb_kids_entry.current(0)
        nb_kids_entry.pack(pady=5)

        # Information dans l'association
        frameBR = tk.LabelFrame(frame_body, text="Information dans l'association", **ROOT_STYLE)
        frameBR.pack(side="left", padx=15)

        tk.Label(frameBR, text="N°adhérent", **LABEL_STYLE).pack(pady=5)
        membership_number_entry = tk.Entry(frameBR)
        membership_number_entry.insert(0, self.session_state[MEMBERSHIP_NUMBER])
        membership_number_entry.pack(pady=5)

        tk.Label(frameBR, text="Rôle", **LABEL_STYLE).pack(pady=5)
        membership_role_entry = ttk.Combobox(frameBR, values=LIST_ROLE, width=12)
        if self.session_state[GENDER]:
            membership_role_entry.current(LIST_ROLE.index(self.session_state[MEMBERSHIP_ROLE]))
        else:
            membership_role_entry.current(0)
        membership_role_entry.pack(pady=5)

        tk.Label(frameBR, text="Date d'inscription", **LABEL_STYLE).pack(pady=5)
        start_suscription_entry = tk.Entry(frameBR)
        start_suscription_entry.insert(0, self.session_state[START_SUSCRIPTION])
        start_suscription_entry.pack(pady=5)

        tk.Label(frameBR, text="Date de sortie", **LABEL_STYLE).pack(pady=5)
        end_suscription_entry = tk.Entry(frameBR)
        end_suscription_entry.insert(0, self.session_state[END_SUSCRIPTION])
        end_suscription_entry.pack(pady=5)

        if self.session_state[KEY_FORM] in [VAL_EMPTY, VAL_ADD]:
            # get inputs from Entry to init a User Object and send it to the self.add_client function
            tk.Button(self.root, text=TXT_ADD, command=lambda : self.add_client( User(
                first_name=first_name_entry.get(),
                last_name=last_name_entry.get(),
                gender=gender_entry.get(),
                birthday=birthday_entry.get(),
                address=address_entry.get(),
                city=city_entry.get(),
                zipcode=zipcode_entry.get(),
                email=email_entry.get(),
                phone=phone_entry.get(),
                job=job_entry.get(),
                relationship_situation=relationship_situation_entry.get(),
                nb_kids=nb_kids_entry.get(),
                membership_number=membership_number_entry.get(),
                membership_role=membership_role_entry.get(),
                start_suscription=start_suscription_entry.get(),
                end_suscription=end_suscription_entry.get()
                )
            ), **BUTTON_STYLE).pack(pady=5)
        elif self.session_state[KEY_FORM] == VAL_MODIFY:
            # get inputs from Entry to init a User Object and send it to the self.add_client function
            tk.Button(self.root, text=TXT_ADD, command=lambda : self.modify_client( User(
                first_name=first_name_entry.get(),
                last_name=last_name_entry.get(),
                gender=gender_entry.get(),
                birthday=birthday_entry.get(),
                address=address_entry.get(),
                city=city_entry.get(),
                zipcode=zipcode_entry.get(),
                email=email_entry.get(),
                phone=phone_entry.get(),
                job=job_entry.get(),
                relationship_situation=relationship_situation_entry.get(),
                nb_kids=nb_kids_entry.get(),
                membership_number=membership_number_entry.get(),
                membership_role=membership_role_entry.get(),
                start_suscription=start_suscription_entry.get(),
                end_suscription=end_suscription_entry.get()
                )
            ), **BUTTON_STYLE).pack(pady=5)

    # Get & Verify inputs, if all rights, it's added to the database
    def add_client(self, user:User):
        if user is None:
            return

        # manage inputs error
        if not self.verify_inputs(user):
            return
        
        # add the person to the database
        self.db.save_data(user.__list__())

        user = None
        # All succeeded, return to the main menu
        self.session_state[KEY_ALERT] = (MSG_ADD_SUCCESS, GREEN)
        self.main_window()
    
    def del_client(self):
        # clear alert message
        self.alert_label.configure(text="")

        # if nothing is selected, display error message
        if not self.tree.selection():
            self.session_state[KEY_ALERT] = (MSG_NO_SELECTION, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        
        # get the element selected
        selected_item = self.tree.selection()[0]
        item = self.tree.item(selected_item)
        # get its id
        id = str(item["values"][0])
        # delete user from the database
        self.db.delete_user(id)
        # delete user from the treeview
        self.tree.delete(selected_item)

        self.session_state[KEY_ALERT] = (MSG_DEL_SUCCESS, GREEN)
        self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
    
    def modify_window(self):
        # clear alert message
        self.alert_label.configure(text="")

        # if nothing is selected, display error message
        if not self.tree.selection():
            self.session_state[KEY_ALERT] = (MSG_NO_SELECTION, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        
        # get the element selected
        selected_item = self.tree.selection()[0]
        # get values from the element
        item = self.tree.item(selected_item)["values"]
        item = item[1:]
        # session state update 
        user = User(*item)
        self.session_state[FIRST_NAME]=user.first_name
        self.session_state[LAST_NAME]=user.last_name
        self.session_state[GENDER]=user.gender
        self.session_state[BIRTHDAY]=user.birthday
        self.session_state[START_SUSCRIPTION]=user.start_suscription
        self.session_state[END_SUSCRIPTION]=user.end_suscription
        self.session_state[ADDRESS]=user.address
        self.session_state[CITY]=user.city
        self.session_state[ZIPCODE]=user.zipcode
        self.session_state[EMAIL]=user.email
        self.session_state[PHONE]=user.phone
        self.session_state[JOB]=user.job
        self.session_state[RELATIONSHIP_SITUATION]=user.relationship_situation
        self.session_state[NB_KIDS]=user.nb_kids
        self.session_state[MEMBERSHIP_NUMBER]=user.membership_number
        self.session_state[MEMBERSHIP_ROLE]=user.membership_role
        # form display

    def modify_client(self, user:User):
        # clear alert message
        self.alert_label.configure(text="")
        
        # if user is empty
        if not user:
            self.session_state[KEY_ALERT] = (MSG_USER_NOT_FIND, RED)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        
        if self.verify_inputs(user):
            self.session_state[KEY_ALERT] = (MSG_MODIFY_SUCCESS, GREEN)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
        
        self.db.update_user(user)

    def verify_inputs(self, user:User):
        ## verify inputs format
        # check firstname and lastname is only with letters
        if not user.first_name.isalpha() or not user.last_name.isalpha():
            self.session_state[KEY_ALERT] = (MSG_INVALID_NAME, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        #check gender : H/F
        if user.gender not in LIST_GENDER:
            self.session_state[KEY_ALERT] = (MSG_INVALID_GENDER, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        # check birthday format : DD-MM-YYYY
        try:
            datetime.datetime.strptime(user.birthday, "%d/%m/%Y")
        except:
            self.session_state[KEY_ALERT] = (MSG_INVALID_BIRTHDAY, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        # check date start & end subscribe
        try:
            datetime.datetime.strptime(user.start_suscription, "%d/%m/%Y")
        except :
            self.session_state[KEY_ALERT] = (MSG_INVALID_SUSCRIPTION, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        try:
            datetime.datetime.strptime(user.end_suscription, "%d/%m/%Y")
        except :
            self.session_state[KEY_ALERT] = (MSG_INVALID_SUSCRIPTION, RED)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        # check address not empty
        if not user.address:
            self.session_state[KEY_ALERT] = (MSG_INVALID_ADDRESS, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        # check city : not empty
        if not user.city:
            self.session_state[KEY_ALERT] = (MSG_INVALID_CITY, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        # check zipcode : 5 digits
        if len(user.zipcode)!= 5 or not user.zipcode.isdigit():
            self.session_state[KEY_ALERT] = (MSG_INVALID_ZIPCODE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        # check email format : regex
        if not re.match(REGEX_EMAIL, user.email):
            self.session_state[KEY_ALERT] = (MSG_INVALID_EMAIL, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        # check phone number format : 10 digits
        if len(user.phone)!= 10 or not user.phone.isdigit():
            self.session_state[KEY_ALERT] = (MSG_INVALID_PHONE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        # check job : not empty
        if not user.job:
            self.session_state[KEY_ALERT] = (MSG_INVALID_JOB, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        # check relationship situation : not empty
        if not user.relationship_situation:
            self.session_state[KEY_ALERT] = (MSG_INVALID_RELATIONSHIP, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
        # check number of kids : not empty
        if not user.nb_kids:
            self.session_state[KEY_ALERT] = (MSG_INVALID_KIDS, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        # check membership number : not empty
        if not user.membership_number:
            self.session_state[KEY_ALERT] = (MSG_INVALID_MEMBERSHIP, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        # check membership role : not empty
        if not user.membership_role:
            self.session_state[KEY_ALERT] = (MSG_INVALID_ROLE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        return True
        
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