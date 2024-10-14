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
        self.session_state[KEY_ALERT] = VAL_EMPTY_ALERT
        self.session_state[KEY_FORM] = VAL_EMPTY
        self.session_state[KEY_USER]=User()
        

        self.tree = ttk.Treeview(self.root)
        
        attributes = User().__attr__()

        self.tree["columns"] = attributes[1:]
        # Définir les colonnes & entêtes
        self.tree.column("#0", width=0)
        self.tree.heading("#0", text="", anchor=tk.CENTER)
        for col in attributes[1:]:
            self.tree.column(col, anchor=tk.CENTER, width=80)
            self.tree.heading(col, text=ATTR[col], command=lambda c=col: self.sortby(c, 0), anchor=tk.CENTER)

        self.main_window()

    def main_window(self):
        # clear screen
        self.clear_window(self.root)

        # set default value for add form
        self.session_state[KEY_FORM] = VAL_ADD

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

        # search frame
        search_frame = tk.Frame(self.root, **ROOT_STYLE)
        search_frame.pack(padx=10, pady=10)

        tk.Label(search_frame, text=TXT_SEARCH, **TITLE_STYLE).pack(pady=5, side="left")

        self.session_state[KEY_SEARCH] = tk.StringVar()
        self.session_state[KEY_SEARCH].trace_add("write", self.update_treeview)
        search_entry = ttk.Entry(search_frame, width=21, textvariable=self.session_state[KEY_SEARCH])
        search_entry.pack(pady=5, padx=5, side="left")


        # clear treeview data
        self.tree.delete(*self.tree.get_children())
        
        # retrieve original data
        self.session_state[KEY_DATA]=self.db.load_data()
        
        # update tree data
        for elt in self.db.load_data():
            self.tree.insert("", tk.END, values=elt)

        # display table
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

        # export button
        modify_button = tk.Button(self.root, text=TXT_EXPORT, command=self.exporter, anchor=tk.CENTER, **BUTTON_STYLE)
        modify_button.pack(pady=5, padx=5)
    
    def add_window(self):
        # clear screen
        self.clear_window(self.root)
        self.session_state[KEY_ALERT] = ("", None)

        # create a exit button for close the window
        frame = tk.Frame(self.root)
        frame.pack()
        back_button = tk.Button(self.root, text=TXT_BACK, command=self.back, anchor=tk.CENTER, **BUTTON_STYLE)
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
        frameTL = tk.LabelFrame(frame_body, text=TXT_PERSONAL_INFO, **LABEL_STYLE)
        frameTL.pack(side="left", padx=15)

        tk.Label(frameTL, text=ATTR[DB_FIRST_NAME], **LABEL_STYLE).pack(pady=5)
        first_name_entry = tk.Entry(frameTL)
        first_name_entry.insert(0, self.session_state[KEY_USER].first_name)
        first_name_entry.pack(pady=5)

        tk.Label(frameTL, text=ATTR[DB_LAST_NAME], **LABEL_STYLE).pack(pady=5)
        last_name_entry = tk.Entry(frameTL)
        last_name_entry.insert(0, self.session_state[KEY_USER].last_name)
        last_name_entry.pack(pady=5)
        
        tk.Label(frameTL, text=ATTR[DB_BIRTHDAY_LAST_NAME], **LABEL_STYLE).pack(pady=5)
        birth_last_name_entry = tk.Entry(frameTL)
        birth_last_name_entry.insert(0, self.session_state[KEY_USER].day_last_name)
        birth_last_name_entry.pack(pady=5)

        tk.Label(frameTL, text=ATTR[DB_CIVILITY], **LABEL_STYLE).pack(pady=5)
        civility_entry = ttk.Combobox(frameTL, values=LIST_CIVILITY, width=8)
        if self.session_state[KEY_USER].civility:
            civility_entry.current(LIST_CIVILITY.index(self.session_state[KEY_USER].civility))
        else:
            civility_entry.current(0)
        civility_entry.pack(pady=5)

        tk.Label(frameTL, text=ATTR[DB_NATIONALITY], **LABEL_STYLE).pack(pady=5)
        nationality_entry = ttk.Combobox(frameTL, values=LIST_NATION, width=8)
        if self.session_state[KEY_USER].nationality:
            nationality_entry.current(LIST_NATION.index(self.session_state[KEY_USER].nationality))
        else:
            nationality_entry.current(0)
        nationality_entry.pack(pady=5)

        tk.Label(frameTL, text=ATTR[DB_BIRTHDAY], **LABEL_STYLE).pack(pady=5)
        birthday_entry = tk.Entry(frameTL)
        birthday_entry.insert(0, self.session_state[KEY_USER].birthday)
        birthday_entry.pack(pady=5)
        
        tk.Label(frameTL, text=ATTR[DB_BIRTHDAY_LOCATION], **LABEL_STYLE).pack(pady=5)
        birthday_entry = tk.Entry(frameTL)
        birthday_entry.insert(0, self.session_state[KEY_USER].birthday_location)
        birthday_entry.pack(pady=5)

        # Informations de Contact
        frameTR = tk.LabelFrame(frame_body, text=TXT_CONTACT_INFO, **LABEL_STYLE)
        frameTR.pack(side="left", padx=15)

        tk.Label(frameTR, text=ATTR[DB_ADDRESS], **LABEL_STYLE).pack(pady=5)
        address_entry = tk.Entry(frameTR)
        address_entry.insert(0, self.session_state[KEY_USER].address)
        address_entry.pack(pady=5)

        tk.Label(frameTR, text=ATTR[DB_CITY], **LABEL_STYLE).pack(pady=5)
        city_entry = tk.Entry(frameTR)
        city_entry.insert(0, self.session_state[KEY_USER].city)
        city_entry.pack(pady=5)

        tk.Label(frameTR, text=ATTR[DB_ZIPCODE], **LABEL_STYLE).pack(pady=5)
        zipcode_entry = tk.Entry(frameTR)
        zipcode_entry.insert(0, self.session_state[KEY_USER].zipcode)
        zipcode_entry.pack(pady=5)

        tk.Label(frameTR, text=ATTR[DB_EMAIL], **LABEL_STYLE).pack(pady=5)
        email_entry = tk.Entry(frameTR)
        email_entry.insert(0, self.session_state[KEY_USER].email)
        email_entry.pack(pady=5)

        tk.Label(frameTR, text=ATTR[DB_PHONE], **LABEL_STYLE).pack(pady=5)
        frame_phone = tk.Frame(frameTR, **ROOT_STYLE)
        frame_phone.pack()

        phone_entry = tk.Entry(frame_phone)
        phone_entry.insert(0, self.session_state[KEY_USER].phone)
        phone_entry.pack(pady=5, side="left")

        # Situation
        frameBL = tk.LabelFrame(frame_body, text=TXT_SITUATION_INFO, **LABEL_STYLE)
        frameBL.pack(side="left", padx=15)

        tk.Label(frameBL, text=ATTR[DB_JOB], **LABEL_STYLE).pack(pady=5)
        job_entry = tk.Entry(frameBL)
        job_entry.insert(0, self.session_state[KEY_USER].job)
        job_entry.pack(pady=5)

        tk.Label(frameBL, text=ATTR[DB_RELATIONSHIP_SITUATION], **LABEL_STYLE).pack(pady=5)
        relationship_situation_entry = ttk.Combobox(frameBL, values=LIST_RELATIONSHIP, width=10)
        if self.session_state[KEY_USER].relationship:
            relationship_situation_entry.current(LIST_RELATIONSHIP.index(self.session_state[KEY_USER].relationship))
        else:
            relationship_situation_entry.current(0)
        relationship_situation_entry.pack(pady=5)

        tk.Label(frameBL, text=ATTR[DB_NB_KIDS], **LABEL_STYLE).pack(pady=5)
        nb_kids_entry = ttk.Combobox(frameBL, values=list(range(0,21)), width=5)
        if self.session_state[KEY_USER].nb_kids:
            nb_kids_entry.current(self.session_state[KEY_USER].nb_kids)
        else:
            nb_kids_entry.current(0)
        nb_kids_entry.pack(pady=5)

        # Information dans l'association
        frameBR = tk.LabelFrame(frame_body, text=TXT_ASSOCIATION_INFO, **LABEL_STYLE)
        frameBR.pack(side="left", padx=15)

        tk.Label(frameBR, text=ATTR[DB_MEMBERSHIP_FONCTION], **LABEL_STYLE).pack(pady=5)
        membership_role_entry = ttk.Combobox(frameBR, values=LIST_FUNCTION, width=12)
        if self.session_state[KEY_USER].member_fonction:
            membership_role_entry.current(LIST_FUNCTION.index(self.session_state[KEY_USER].member_fonction))
        else:
            membership_role_entry.current(0)
        membership_role_entry.pack(pady=5)

        tk.Label(frameBR, text=ATTR[DB_START_SUSCRIPTION], **LABEL_STYLE).pack(pady=5)
        start_suscription_entry = tk.Entry(frameBR)
        start_suscription_entry.insert(0, self.session_state[KEY_USER].start_suscription)
        start_suscription_entry.pack(pady=5)

        tk.Label(frameBR, text=ATTR[DB_END_SUSCRIPTION], **LABEL_STYLE).pack(pady=5)
        end_suscription_entry = tk.Entry(frameBR)
        end_suscription_entry.insert(0, self.session_state[KEY_USER].end_suscription)
        end_suscription_entry.pack(pady=5)

        if self.session_state[KEY_FORM] in [VAL_EMPTY, VAL_ADD]:
            # get inputs from Entry to init a User Object and send it to the self.add_client function
            tk.Button(self.root, text=TXT_ADD, command=lambda : self.add_client( User(
                first_name=first_name_entry.get(),
                last_name=last_name_entry.get(),
                birth_last_name_entry=birth_last_name_entry.get(),
                civility=civility_entry.get(),
                birthday=birthday_entry.get(),
                birthday_location=birthday_entry.get(),
                address=address_entry.get(),
                city=city_entry.get(),
                zipcode=zipcode_entry.get(),
                email=email_entry.get(),
                phone=phone_entry.get(),
                job=job_entry.get(),
                relationship_situation=relationship_situation_entry.get(),
                nb_kids=nb_kids_entry.get(),
                membership_number=self.db.generer_identifiant(),
                membership_role=membership_role_entry.get(),
                start_suscription=start_suscription_entry.get(),
                end_suscription=end_suscription_entry.get()
                )
            ), **BUTTON_STYLE).pack(pady=5)
        elif self.session_state[KEY_FORM] == VAL_MODIFY:
            # get inputs from Entry to init a User Object and send it to the self.add_client function
            tk.Button(self.root, text=TXT_MODIFY, command=lambda : self.modify_client( User(
                first_name=first_name_entry.get(),
                last_name=last_name_entry.get(),
                gender=civility_entry.get(),
                birthday=birthday_entry.get(),
                address=address_entry.get(),
                city=city_entry.get(),
                zipcode=zipcode_entry.get(),
                email=email_entry.get(),
                phone=phone_entry.get(),
                job=job_entry.get(),
                relationship_situation=relationship_situation_entry.get(),
                nb_kids=nb_kids_entry.get(),
                membership_number=self.session_state[KEY_USER].member_id,
                membership_role=membership_role_entry.get(),
                start_suscription=start_suscription_entry.get(),
                end_suscription=end_suscription_entry.get(),
                id=self.session_state[KEY_USER].id
                )
            ), **BUTTON_STYLE).pack(pady=5)

    # Get & Verify inputs, if all rights, it's added to the database
    def add_client(self, user:User):
        if not user:
            self.session_state[KEY_ALERT] = (MSG_USER_NOT_FIND, GREEN)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        
        # manage inputs error
        if not self.verify_inputs(user):
            return
        
        # add the person to the database
        if not self.db.save_data(user.__list__()):
            self.session_state[KEY_ALERT] = (MSG_SAVING_DATA, RED)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        # clear user
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
        # if nothing is selected, display error message
        if not self.tree.selection():
            self.session_state[KEY_ALERT] = (MSG_NO_SELECTION, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        
        # get the element selected
        selected_item = self.tree.selection()[0]
        # get values from the element
        item = self.tree.item(selected_item, "values")
        print(item)
        tmp_id = item[0]
        item = item[1:]
        # session state update 
        self.session_state[KEY_USER] = User(*item, id=tmp_id)
        # form display
        self.session_state[KEY_FORM] = VAL_MODIFY
        self.add_window()

    def modify_client(self, user:User):
        # if user is empty
        if not user:
            self.session_state[KEY_ALERT] = (MSG_USER_NOT_FIND, RED)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        
        if not self.verify_inputs(user):
            return

        # update user in the database
        self.db.update_user(user)
        # clear user
        user = None
        self.session_state[KEY_USER] = User()
        # All succeeded, return to the main menu
        self.session_state[KEY_ALERT] = (MSG_MODIFY_SUCCESS, GREEN)
        self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
        self.main_window()

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
            self.session_state[KEY_ALERT] = (MSG_INVALID_SUSCRIPTION, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # check address not empty
        # if not user.address:
        #     self.session_state[KEY_ALERT] = (MSG_INVALID_ADDRESS, ORANGE)
        #     self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
        #     return False
        
        # check city : not empty
        # if not user.city:
        #     self.session_state[KEY_ALERT] = (MSG_INVALID_CITY, ORANGE)
        #     self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
        #     return False
        
        # check zipcode : 5 digits
        # if len(user.zipcode)!= 5 or not user.zipcode.isdigit():
        #     self.session_state[KEY_ALERT] = (MSG_INVALID_ZIPCODE, ORANGE)
        #     self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
        #     return False
        
        # check email format : regex
        if not(re.match(REGEX_EMAIL, user.email) or user.email == ""):
            self.session_state[KEY_ALERT] = (MSG_INVALID_EMAIL, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # check phone number format : 10 digits
        if not ((len(user.phone) == 10) or user.phone == ""):
            self.session_state[KEY_ALERT] = (MSG_INVALID_PHONE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # check job : not empty
        if not user.job:
            self.session_state[KEY_ALERT] = (MSG_INVALID_JOB, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # check relationship situation : in the list
        if not user.relationship_situation in LIST_RELATIONSHIP:
            self.session_state[KEY_ALERT] = (MSG_INVALID_RELATIONSHIP, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
        
        # check number of kids : is a digit
        if not (user.nb_kids.isdigit() and int(user.nb_kids) >= 0):
            self.session_state[KEY_ALERT] = (MSG_INVALID_KIDS, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # check membership number : not empty
        if not user.membership_number:
            self.session_state[KEY_ALERT] = (MSG_INVALID_MEMBERSHIP, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # check membership role : in the list
        if not user.membership_role in LIST_FUNCTION:
            self.session_state[KEY_ALERT] = (MSG_INVALID_ROLE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        return True
    
    # Fonction de tri
    def sortby(self, col, descending):
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children("")]
        data.sort(reverse=descending)
        
        # Repositionner les éléments dans l'ordre trié
        for ix, item in enumerate(data):
            self.tree.move(item[1], '', ix)

        # Ajuster le sens du tri
        self.tree.heading(col, command=lambda col=col: self.sortby(col, int(not descending)))
    
    # Fonction de filtrage
    def update_treeview(self, *args):
        search_term = self.session_state[KEY_SEARCH].get().lower()
        self.tree.delete(*self.tree.get_children())
        
        for item in self.session_state[KEY_DATA]:
            if search_term in item[-2].lower():
                self.tree.insert("", "end", values=item)

    def exporter(self):
        try:
            self.db.export_csv()
            self.session_state[KEY_ALERT] = (MSG_CSV_SUCCESS, GREEN)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        except Exception as e:
            print(e)
            self.session_state[KEY_ALERT] = (MSG_CSV_ERROR, RED)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return

    # undisplay widgets in window (not destroy)
    def clear_window(self, window):
        for widget in window.winfo_children():
            widget.pack_forget()
    
    # start the main application loop
    def run(self):
        self.root.mainloop()
    
    def back(self):
        self.session_state[KEY_ALERT]=("",None)
        self.session_state[KEY_USER]=User()
        self.main_window()
    # exit the app and all other process need to be stop separately
    def exit(self):
        self.root.quit()