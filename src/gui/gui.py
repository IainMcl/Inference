import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class Gui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(background="#2b2d2f")
        self.master = master
        self.pack()
        self.base()
        self.create_widgets()

    def base(self):
        # image dimensions 500 x 200
        self.logo = ImageTk.PhotoImage(Image.open("./images/phs_logo.png").resize((300, 120)))
        panel = tk.Label(self, image=self.logo)
        panel.grid(column=4, row=0)
        # self.logo = tk.create_image(100, 40, anchor=NE, image=img)

    def create_widgets(self):
        load = tk.Button(self)
        load["text"] = "Browse"
        load["command"] = self.load_data
        load.grid(column=3, row=4)

    def load_data(self):
        print("Loading data")
        dfile = filedialog.askopenfilename()
