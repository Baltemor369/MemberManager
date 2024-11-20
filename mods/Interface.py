import tkinter as tk
import os
import re
from tkinter import filedialog, messagebox
from tkinter import ttk

from .const import *
from mods.User import User
from mods.Database import Database
from mods.Tools import format_date, clear_input

class Interface:
    def __init__(self):
        self.db = Database(DB_PATH)
        self.root = tk.Tk()
        self.root.title(APP_NAME)

        icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
        self.root.iconbitmap(icon_path)
        
        self.root.state('zoomed')

        self.root.configure(**ROOT_STYLE)

        self.session_state = {}
        self.session_state[KEY_ALERT] = VAL_EMPTY_ALERT
        self.session_state[KEY_FORM] = VAL_EMPTY
        self.session_state[KEY_USER] = User()
        

        self.tree = ttk.Treeview(self.root)
        
        attributes = User().__attr__()

        self.tree["columns"] = attributes[1:]

        self.tree.column("#0", width=0, stretch=tk.NO)
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

        # create a title
        tk.Label(self.root, text=APP_NAME, **TITLE_STYLE).pack(pady=10)
        

        # Alert Frame to display a specific message
        alert_frame = tk.Frame(self.root, **ROOT_STYLE)
        alert_frame.pack(padx=10, pady=10)

        self.alert_label = tk.Label(alert_frame, text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1], **ALERT_STYLE)
        self.alert_label.pack(pady=5)

        # search frame
        search_frame = tk.Frame(self.root, **ROOT_STYLE)
        search_frame.pack(padx=10, pady=10)

        tk.Label(search_frame, text=TXT_SEARCH_LABEL, **SUBTITLE_STYLE).pack(pady=5, side="left")

        self.session_state[KEY_SEARCH] = tk.StringVar()
        self.session_state[KEY_SEARCH].trace_add("write", self.update_treeview)
        search_entry = tk.Entry(search_frame, width=30, textvariable=self.session_state[KEY_SEARCH])
        search_entry.pack(pady=5, padx=5, side="left")

        tk.Button(search_frame, text=TXT_ADVANCED_SEARCH, command=self.open_advanced_search, **BUTTON_STYLE_LONG).pack(pady=5, padx=5)
        tk.Button(search_frame, text=TXT_CLEAR, command=self.main_window, **BUTTON_STYLE_LONG).pack(pady=5, padx=5)

        # clear treeview data
        self.tree.delete(*self.tree.get_children())
            
        # update tree data
        for elt in self.db.load_data():
            if elt[-1] == VAL_ACTIVE:
                self.tree.insert("", tk.END, text=elt[0], values=elt[1:])
            else:
                self.tree.insert("", tk.END, text=elt[0], values=elt[1:], tag=(VAL_INACTIVE,))
        
        self.tree.tag_configure(VAL_INACTIVE, background="gray")
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
        
        # export button
        import_button = tk.Button(self.root, text=TXT_IMPORT, command=self.open_file_dialog, anchor=tk.CENTER, **BUTTON_STYLE)
        import_button.pack(pady=5, padx=5)
    
    def add_window(self):
        # clear screen
        self.clear_window(self.root)
        self.session_state[KEY_ALERT] = VAL_EMPTY_ALERT

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
        first_name_entry.focus_set()

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
        birth_location_entry = tk.Entry(frameTL)
        birth_location_entry.insert(0, self.session_state[KEY_USER].birthday_location)
        birth_location_entry.pack(pady=5)

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
        frame_phone = tk.Frame(frameTR, bg=SMOOTHGREEN)
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
        membership_function_entry = ttk.Combobox(frameBR, values=LIST_FUNCTION, width=12)
        if self.session_state[KEY_USER].member_function:
            membership_function_entry.current(LIST_FUNCTION.index(self.session_state[KEY_USER].member_function))
        else:
            membership_function_entry.current(0)
        membership_function_entry.pack(pady=5)

        tk.Label(frameBR, text=ATTR[DB_START_SUSCRIPTION], **LABEL_STYLE).pack(pady=5)
        start_subscription_entry = tk.Entry(frameBR)
        start_subscription_entry.insert(0, self.session_state[KEY_USER].start_subscription)
        start_subscription_entry.pack(pady=5)

        tk.Label(frameBR, text=ATTR[DB_END_SUSCRIPTION], **LABEL_STYLE).pack(pady=5)
        end_subscription_entry = tk.Entry(frameBR)
        end_subscription_entry.insert(0, self.session_state[KEY_USER].end_subscription)
        end_subscription_entry.pack(pady=5)

        tk.Label(frameBR, text=ATTR[DB_ACTIVITY], **LABEL_STYLE).pack(pady=5)
        activity_entry = ttk.Combobox(frameBR, values=LIST_ACTIF, width=12)
        if self.session_state[KEY_USER].activity:
            activity_entry.current(LIST_ACTIF.index(self.session_state[KEY_USER].activity))
        else:
            activity_entry.current(0)
        activity_entry.pack(pady=5)

        if self.session_state[KEY_FORM] in [VAL_EMPTY, VAL_ADD]:
            # get inputs from Entry to init a User Object and send it to the self.add_client function
            tk.Button(self.root, text=TXT_ADD, command=lambda : self.add_client( User(
                first_name=first_name_entry.get().capitalize(),
                last_name=last_name_entry.get().capitalize(),
                day_last_name=birth_last_name_entry.get().capitalize(),
                civility=civility_entry.get(),
                nationality=nationality_entry.get().capitalize(),
                birthday=format_date(birthday_entry.get()),
                birthday_location=birth_location_entry.get().capitalize(),
                address=address_entry.get(),
                city=city_entry.get().capitalize(),
                zipcode=zipcode_entry.get(),
                email=email_entry.get(),
                phone=phone_entry.get(),
                job=job_entry.get().capitalize(),
                relationship=relationship_situation_entry.get(),
                nb_kids=nb_kids_entry.get(),
                member_function=membership_function_entry.get(),
                start_subscription=format_date(start_subscription_entry.get()),
                end_subscription=format_date(end_subscription_entry.get()),
                activity=activity_entry.get(),
                member_id=self.db.generer_identifiant(),
                )
            ), **BUTTON_STYLE).pack(pady=5)
        elif self.session_state[KEY_FORM] == VAL_MODIFY:
            # get inputs from Entry to init a User Object and send it to the self.add_client function
            tk.Button(self.root, text=TXT_MODIFY, command=lambda : self.modify_client( User(
                first_name=first_name_entry.get().capitalize(),
                last_name=last_name_entry.get().capitalize(),
                day_last_name=birth_last_name_entry.get().capitalize(),
                civility=civility_entry.get(),
                nationality=nationality_entry.get().capitalize(),
                birthday=format_date(birthday_entry.get()),
                birthday_location=birth_location_entry.get().capitalize(),
                address=address_entry.get(),
                city=city_entry.get().capitalize(),
                zipcode=zipcode_entry.get(),
                email=email_entry.get(),
                phone=phone_entry.get(),
                job=job_entry.get().capitalize(),
                relationship=relationship_situation_entry.get(),
                nb_kids=nb_kids_entry.get(),
                member_function=membership_function_entry.get(),
                start_subscription=format_date(start_subscription_entry.get()),
                end_subscription=format_date(end_subscription_entry.get()),
                activity=activity_entry.get(),
                member_id=self.session_state[KEY_USER].member_id,
                ID=self.session_state[KEY_USER].ID
                )
            ), **BUTTON_STYLE).pack(pady=5)

    # Get & Verify inputs, if all rights, it's added to the database
    def add_client(self, user:User):
        if not user:
            self.session_state[KEY_ALERT] = (MSG_USER_NOT_FIND, RED)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        
        # verify inputs
        if not self.verify_inputs(user):
            return
        
        # add the person to the database
        if not self.db.save_data(user):
            self.session_state[KEY_ALERT] = (MSG_SAVING_DATA, RED)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        
        # clear user
        user = None
        self.session_state[KEY_USER]=User()
        
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
        id = str(item["text"])
        # delete user from the database
        if not self.db.delete_user(id):
            self.session_state[KEY_ALERT] = (MSG_USER_NOT_FIND, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        
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
        values = self.tree.item(selected_item, "values")
        columns = self.tree['columns']
        data_dict = {columns[i]: values[i] for i in range(len(columns))}
        
        tmp_id = self.tree.item(selected_item, "text")
        
        # session state update 
        self.session_state[KEY_USER] = User(**data_dict, ID=tmp_id)
        
        # form display
        self.session_state[KEY_FORM] = VAL_MODIFY
        self.add_window()

    def modify_client(self, user:User):
        # if user is empty
        if not user:
            self.session_state[KEY_ALERT] = (MSG_USER_NOT_FIND, RED)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return
        
        if not self.verify_inputs(user, True):
            return

        # update user in the database
        if not self.db.update_user(user):
            self.session_state[KEY_ALERT] = (MSG_UPDATE_DATA, RED)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])    
            return
        # clear user
        user = None
        self.session_state[KEY_USER] = User()
        # All succeeded, return to the main menu
        self.session_state[KEY_ALERT] = (MSG_MODIFY_SUCCESS, GREEN)
        self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
        self.main_window()
    
    def open_advanced_search(self):
        # clear user
        self.session_state[KEY_USER] = User()

        self.advanced_search_window = tk.Toplevel(self.root, **ROOT_STYLE)
        self.advanced_search_window.title("Recherche avancée")

        # main Frame
        frame_body = tk.Frame(self.advanced_search_window, **ROOT_STYLE)
        frame_body.pack(padx=10, pady=10)

        # Personnal information
        frameTL = tk.LabelFrame(frame_body, text=TXT_PERSONAL_INFO, **LABEL_STYLE)
        frameTL.pack(side="left", padx=15)

        tk.Label(frameTL, text=ATTR[DB_FIRST_NAME], **LABEL_STYLE).pack(pady=5)
        first_name_entry = tk.Entry(frameTL)
        first_name_entry.insert(0, self.session_state[KEY_USER].first_name)
        first_name_entry.pack(pady=5)
        first_name_entry.focus_set()

        tk.Label(frameTL, text=ATTR[DB_LAST_NAME], **LABEL_STYLE).pack(pady=5)
        last_name_entry = tk.Entry(frameTL)
        last_name_entry.insert(0, self.session_state[KEY_USER].last_name)
        last_name_entry.pack(pady=5)
        
        tk.Label(frameTL, text=ATTR[DB_BIRTHDAY_LAST_NAME], **LABEL_STYLE).pack(pady=5)
        birth_last_name_entry = tk.Entry(frameTL)
        birth_last_name_entry.insert(0, self.session_state[KEY_USER].day_last_name)
        birth_last_name_entry.pack(pady=5)

        tk.Label(frameTL, text=ATTR[DB_CIVILITY], **LABEL_STYLE).pack(pady=5)
        civility_entry = ttk.Combobox(frameTL, values=[""] + LIST_CIVILITY, width=8)
        if self.session_state[KEY_USER].civility:
            civility_entry.current(LIST_CIVILITY.index(self.session_state[KEY_USER].civility))
        else:
            civility_entry.current(0)
        civility_entry.pack(pady=5)

        tk.Label(frameTL, text=ATTR[DB_NATIONALITY], **LABEL_STYLE).pack(pady=5)
        nationality_entry = ttk.Combobox(frameTL, values=[""] + LIST_NATION, width=8)
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
        birth_location_entry = tk.Entry(frameTL)
        birth_location_entry.insert(0, self.session_state[KEY_USER].birthday_location)
        birth_location_entry.pack(pady=5)

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
        relationship_situation_entry = ttk.Combobox(frameBL, values=[""] + LIST_RELATIONSHIP, width=10)
        if self.session_state[KEY_USER].relationship:
            relationship_situation_entry.current(LIST_RELATIONSHIP.index(self.session_state[KEY_USER].relationship))
        else:
            relationship_situation_entry.current(0)
        relationship_situation_entry.pack(pady=5)

        tk.Label(frameBL, text=ATTR[DB_NB_KIDS], **LABEL_STYLE).pack(pady=5)
        nb_kids_entry = ttk.Combobox(frameBL, values=[""] + list(range(0,21)), width=5)
        if self.session_state[KEY_USER].nb_kids:
            nb_kids_entry.current(self.session_state[KEY_USER].nb_kids)
        else:
            nb_kids_entry.current(0)
        nb_kids_entry.pack(pady=5)

        # Information dans l'association
        frameBR = tk.LabelFrame(frame_body, text=TXT_ASSOCIATION_INFO, **LABEL_STYLE)
        frameBR.pack(side="left", padx=15)

        tk.Label(frameBR, text=ATTR[DB_MEMBERSHIP_FONCTION], **LABEL_STYLE).pack(pady=5)
        membership_function_entry = ttk.Combobox(frameBR, values=[""] + LIST_FUNCTION, width=12)
        if self.session_state[KEY_USER].member_function:
            membership_function_entry.current(LIST_FUNCTION.index(self.session_state[KEY_USER].member_function))
        else:
            membership_function_entry.current(0)
        membership_function_entry.pack(pady=5)

        tk.Label(frameBR, text=ATTR[DB_START_SUSCRIPTION], **LABEL_STYLE).pack(pady=5)
        start_subscription_entry = tk.Entry(frameBR)
        start_subscription_entry.insert(0, self.session_state[KEY_USER].start_subscription)
        start_subscription_entry.pack(pady=5)

        tk.Label(frameBR, text=ATTR[DB_END_SUSCRIPTION], **LABEL_STYLE).pack(pady=5)
        end_subscription_entry = tk.Entry(frameBR)
        end_subscription_entry.insert(0, self.session_state[KEY_USER].end_subscription)
        end_subscription_entry.pack(pady=5)

        tk.Label(frameBR, text=ATTR[DB_ACTIVITY], **LABEL_STYLE).pack(pady=5)
        activity_entry = ttk.Combobox(frameBR, values=[""] + LIST_ACTIF, width=12)
        if self.session_state[KEY_USER].activity:
            activity_entry.current(LIST_ACTIF.index(self.session_state[KEY_USER].activity))
        else:
            activity_entry.current(0)
        activity_entry.pack(pady=5)
        
        search_button = tk.Button(self.advanced_search_window, text=TXT_SEARCH, command=lambda : self.advanced_research(User(
                first_name=first_name_entry.get().capitalize(),
                last_name=last_name_entry.get().capitalize(),
                day_last_name=birth_last_name_entry.get().capitalize(),
                civility=civility_entry.get(),
                nationality=nationality_entry.get().capitalize(),
                birthday=format_date(birthday_entry.get()),
                birthday_location=birth_location_entry.get().capitalize(),
                address=address_entry.get(),
                city=city_entry.get().capitalize(),
                zipcode=zipcode_entry.get(),
                email=email_entry.get(),
                phone=phone_entry.get(),
                job=job_entry.get().capitalize(),
                relationship=relationship_situation_entry.get(),
                nb_kids=nb_kids_entry.get(),
                member_function=membership_function_entry.get(),
                start_subscription=format_date(start_subscription_entry.get()),
                end_subscription=format_date(end_subscription_entry.get()),
                activity=activity_entry.get(),
                )), **BUTTON_STYLE)
        search_button.pack(pady=20)
    
    def advanced_research(self, user:User):
        # destroy window
        # self.advanced_search_window.destroy()

        # clear treeview
        self.tree.delete(*self.tree.get_children())
        
        user_values = user.__list__()

        # search elts
        for item in self.db.load_data():
            find = True
            for i in range(1,len(user_values)):
                if user_values[i]:
                    if user_values[i] not in str(item[i]):
                        find = False
            if find:
                self.tree.insert("", tk.END, text=item[0], values=item[1:])

    def verify_inputs(self, user:User, modifying:bool=False):
        ## verify inputs format
        # clearing inputs
        user.first_name = clear_input(user.first_name)
        user.last_name = clear_input(user.last_name)
        user.day_last_name = clear_input(user.day_last_name)
        user.civility = clear_input(user.civility)
        user.nationality = clear_input(user.nationality)
        user.address = clear_input(user.address)
        user.city = clear_input(user.city)
        user.zipcode = clear_input(user.zipcode)
        user.email = clear_input(user.email)
        user.phone = clear_input(user.phone)
        user.job = clear_input(user.job)
        user.relationship = clear_input(user.relationship)
        user.nb_kids = clear_input(user.nb_kids)
        user.member_function = clear_input(user.member_function)
        user.activity = clear_input(user.activity)

        max = 1
        
        # REQUIRED
        # check firstname and lastname and birth last name REGEX_NAME
        if not (re.match(REGEX_NAME, user.first_name) and re.match(REGEX_NAME, user.last_name) and (user.day_last_name=="" or re.match(REGEX_NAME, user.day_last_name))):
            self.session_state[KEY_ALERT] = (MSG_INVALID_NAME, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # check civility
        if user.civility not in LIST_CIVILITY:
            self.session_state[KEY_ALERT] = (MSG_INVALID_CIVILITY, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # check nationality
        if user.nationality not in LIST_NATION:
            self.session_state[KEY_ALERT] = (MSG_INVALID_NATION, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # REQUIRED
        # check birthday format : DD-MM-YYYY
        if user.birthday is None:
            self.session_state[KEY_ALERT] = (MSG_INVALID_BIRTHDAY, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
       
        # REQUIRED
        # check birth location
        if user.birthday_location is None:
            self.session_state[KEY_ALERT] = (MSG_INVALID_LOCATION_BIRTHDAY, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False

        # REQUIRED
        # check date start
        if user.start_subscription is None:
            self.session_state[KEY_ALERT] = (MSG_INVALID_SUSCRIPTION, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # check date end subscribe
        
        # check address
        
        # check city 
        
        # check zipcode 
        
        # check email format : regex
        if not(re.match(REGEX_EMAIL, user.email) or user.email == ""):
            self.session_state[KEY_ALERT] = (MSG_INVALID_EMAIL, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # check phone number
        
        # check job
        
        # check relationship situation from the list
        if not user.relationship in LIST_RELATIONSHIP:
            self.session_state[KEY_ALERT] = (MSG_INVALID_RELATIONSHIP, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # check number of kids : is a digit
        if not (user.nb_kids.isdigit() and int(user.nb_kids) >= 0):
            self.session_state[KEY_ALERT] = (MSG_INVALID_KIDS, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        # check membership number 
        
        # check membership function from in the list
        if not user.member_function in LIST_FUNCTION:
            self.session_state[KEY_ALERT] = (MSG_INVALID_ROLE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False

        result = self.db.get_items(member_function=ROLE_PRESIDENT)
        if len(result) > max:
            self.session_state[KEY_ALERT] = (MSG_MAX_ROLE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        result = self.db.get_items(member_function=ROLE_VICE_PRESIDENT)
        if len(result) > max:
            self.session_state[KEY_ALERT] = (MSG_MAX_ROLE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        result = self.db.get_items(member_function=ROLE_SECRETARY)
        if len(result) > max:
            self.session_state[KEY_ALERT] = (MSG_MAX_ROLE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        result = self.db.get_items(member_function=ROLE_SECRETARY_ASSISTANT)
        if len(result) > max:
            self.session_state[KEY_ALERT] = (MSG_MAX_ROLE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        result = self.db.get_items(member_function=ROLE_TREASURER)
        if len(result) > max:
            self.session_state[KEY_ALERT] = (MSG_MAX_ROLE, ORANGE)
            self.alert_label.configure(text=self.session_state[KEY_ALERT][0], fg=self.session_state[KEY_ALERT][1])
            return False
        
        result = self.db.get_items(member_function=ROLE_TREASURER_ASSISTANT)
        if len(result) > max:
            self.session_state[KEY_ALERT] = (MSG_MAX_ROLE, ORANGE)
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
    
    def open_file_dialog(self): 
        csv_filename = filedialog.askopenfilename(title="Choisir un fichier CSV", filetypes=[("CSV files", "*.csv")]) 
        if csv_filename: 
            try: 
                if self.db.import_csv(csv_filename):
                    messagebox.showinfo("Succès", "Fichier CSV importé avec succès !") 
                    self.main_window()
            except Exception as e: 
                messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")
    
    # Fonction de filtrage
    def update_treeview(self, *args):
        search_term = self.session_state[KEY_SEARCH].get()
        self.tree.delete(*self.tree.get_children())
        
        for item in self.db.load_data():
            if search_term.lower() in item[-3].lower():
                self.tree.insert("", tk.END, text=item[0], values=item[1:])

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
            try:
                widget.pack_forget()
            except:
                pass
    
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