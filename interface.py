import tkinter as tk

class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mon Interface Tkinter")
        self.main()

    def main(self):
        exit_button = tk.Button("Exit", command=self.root.quit)
        exit_button.pack(side="bottom")
    
    def run(self):
        self.root.mainloop()