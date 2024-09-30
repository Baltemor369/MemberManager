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

        tk.Label(self.root, text="Add Window").pack()
    
    def clear_window(self, window):
        for widget in window.winfo_children():
            widget.pack_forget()
    
    def run(self):
        self.root.mainloop()
    
    def exit(self):
        self.root.quit()