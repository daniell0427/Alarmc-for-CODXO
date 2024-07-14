from customtkinter import *
from tkinter import Canvas, Scrollbar
from tkinter import ttk
from database import *
from functions import *

class AlarmPage(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Constants
        self.master = master
        self.uuid = get_uuid()
        self.default_font = CTkFont(family="Serif", size=16)
        self.header_font = CTkFont(family="Serif", size=24)


        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Define scrollbar style
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Vertical.TScrollbar", 
                gripcount=0,
                background="grey20", 
                darkcolor="grey10", 
                lightcolor="grey30",
                troughcolor="grey10", 
                bordercolor="grey10", 
                arrowcolor="white",
                activebackground="grey")

        # Create a canvas for scrolling
        self.canvas = Canvas(self, bd=0, highlightthickness=0)
        self.canvas.grid(row=1, column=0, sticky='nsew')
        
        # Apply the styled scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview, style="Vertical.TScrollbar")
        self.scrollbar.grid(row=1, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas
        self.scrollable_frame = CTkFrame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')

        # Header
        alarmText = CTkLabel(self, text="Alarm", font=self.header_font, width=200, anchor=W)
        alarmText.grid(column=0, row=0, sticky=W, padx=10, pady=5)
        addButton = CTkButton(self, text="+", font=self.header_font, command=self.showAddPage, width=30, height=20,
                              fg_color="transparent", hover_color="#61BAE6", corner_radius=10)
        addButton.grid(column=1, row=0, sticky=E, padx=10, pady=5)

        self.create_widgets()

    def showAddPage(self):
        from pages.addPage import AddPage
        self.my_frame = AddPage(master=self.master)
        self.my_frame.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

    def toggle_alarm(self, alarm_id, current_state):
        new_state = 0 if current_state else 1
        cursor.execute("UPDATE alarms SET active = ? WHERE rowid = ?", (new_state, alarm_id))
        conn.commit()
        self.refresh_alarms()

    def delete_alarm(self, alarm_id):
        cursor.execute("DELETE FROM alarms WHERE rowid = ?", (alarm_id,))
        conn.commit()
        self.refresh_alarms()

    def refresh_alarms(self):
        self.alarms = get_alarms(self.uuid)
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.create_widgets()

    def create_widgets(self):
        self.alarms = get_alarms(self.uuid)

        # Horizontal line
        horizontal_line = CTkFrame(self.scrollable_frame, height=4, width=470, fg_color="black")
        horizontal_line.grid(row=0, column=0, columnspan=2, padx=10, pady=(0, 10))

        # Display alarms
        if self.alarms:
            for idx, alarm in enumerate(self.alarms, start=1):
                alarm_id, hour, minute, repeat, active = alarm[5], alarm[1], alarm[2], alarm[3], alarm[4]
                time_str = f"{hour:02d}:{minute:02d}"

                alarm_frame = CTkFrame(self.scrollable_frame)
                alarm_frame.grid(row=idx, column=0, padx=(10, 50), pady=10, sticky="ew", columnspan=2)
                button_color = "green" if active else "red"
                hover_color = "lightgreen" if active else "pink"

                # Time label
                time_label = CTkLabel(alarm_frame, text=time_str, font=self.header_font)
                time_label.grid(row=0, column=0, padx=15, pady=20, sticky=W)

                # Days buttons
                days = ["S", "M", "T", "W", "T", "F", "S"]
                for idy, day in enumerate(days):
                    if str(idy) in repeat:
                        day = CTkLabel(alarm_frame, text=day, width=30, height=30, bg_color="grey")
                    else:
                        day = CTkLabel(alarm_frame, text=day, width=30, height=30)
                    day.grid(row=0, column=idy + 1, padx=2)

                # Toggle and delete buttons
                toggle_button = CTkButton(alarm_frame, width=30, height=30, fg_color=button_color,
                                        hover_color=hover_color, text="", command=lambda a_id=alarm_id, a_state=active: self.toggle_alarm(a_id, a_state))
                delete_button = CTkButton(alarm_frame, width=20, height=20, fg_color="transparent", hover_color="grey", text="x",
                                        command=lambda a_id=alarm_id: self.delete_alarm(a_id))

                toggle_button.grid(row=0, column=len(days) + 1, padx=15, pady=15, sticky=E)
                delete_button.grid(row=0, column=len(days) + 2, padx=5, pady=5, sticky=NE)
                alarm_frame.grid_columnconfigure(len(days) + 1, weight=1)

                play_alarm(time_str, repeat)

        else:
            addLabel = CTkLabel(self.scrollable_frame, text="You don't have any alarms yet \n Add a new alarm!", justify=LEFT, font=self.default_font, text_color="#9A9A9A")
            addLabel.grid(row=1, column=0, padx=10, columnspan=2, pady=200)

        self.scrollable_frame.grid_columnconfigure(0, weight=1)