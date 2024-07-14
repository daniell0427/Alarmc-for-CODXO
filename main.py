from customtkinter import *
from database import *
from functions import *
from pages.alarmPage import *

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class App(CTk):
    def __init__(self):
        super().__init__()

        #specs
        self.geometry("500x550", )
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.title("Alarmx")
        self.iconbitmap("resources/alarm.ico")
        self.resizable(False, False)

        #show frame
        self.my_frame = AlarmPage(master=self)
        self.my_frame.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)


#run app
app = App()
app.mainloop()

