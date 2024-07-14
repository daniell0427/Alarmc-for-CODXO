from customtkinter import *
from database import *
from functions import *

class AddPage(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Constants
        uuid = get_uuid()
        alarms = get_alarms(uuid)
        default_font = CTkFont(family="Serif", size=16)
        header_font = CTkFont(family="Serif", size=24)

        def goBack():
            from pages.alarmPage import AlarmPage
            self.my_frame = AlarmPage(master=master)
            self.my_frame.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        def update_time_label():
            hour = int(hour_slider.get())
            minute = int(minute_slider.get())
            time_label.configure(text=f"Selected Time: {hour:02d}:{minute:02d}")

        def update_hour_label(value):
            hour = int(value)
            if hour >= 0 and hour <= 9:
                hour_label.configure(text=f"Selected Hour: 0{hour}")
            else:
                hour_label.configure(text=f"Selected Hour: {hour}")
            update_time_label()

        def update_minute_label(value):
            minute = int(value)
            if minute >= 0 and minute <= 9:
                minute_label.configure(text=f"Selected Minute: 0{minute}")
            else:
                minute_label.configure(text=f"Selected Minute: {minute}")
            update_time_label()

        def get_on_val():
            self.on_day_vars = [i for i in range(7) if self.day_vars[i].get() == "on"]

        def submit_alarm():
            get_on_val()
            repeat = ''.join(str(i) for i in self.on_day_vars)
            add_alarm_to_database(int(hour_slider.get()), int(minute_slider.get()), uuid, repeat, 1)
            goBack()

        # Hour slider
        hour_label = CTkLabel(self, text="Selected Hour: 0", font=default_font)
        hour_label.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="w")

        hour_slider = CTkSlider(self, from_=0, to=23, number_of_steps=24, command=update_hour_label)
        hour_slider.set(0)
        hour_slider.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)  

        # Minute slider
        minute_label = CTkLabel(self, text="Selected Minute: 0", font=default_font)
        minute_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        minute_slider = CTkSlider(self, from_=0, to=59, number_of_steps=60, command=update_minute_label)
        minute_slider.set(0)
        minute_slider.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)  
        # Time display label
        time_label = CTkLabel(self, text="Selected Time: 00:00", font=default_font)
        time_label.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky="ew")

        # Repeat days options
        days_frame = CTkFrame(self)
        days_frame.grid(row=5, column=0, padx=10, pady=(30, 10), sticky="ew", columnspan=2)

        repeat_days_label = CTkLabel(days_frame, text="Repeat:", font=default_font)
        repeat_days_label.grid(row=0, column=0, padx=5, pady=5, ipady=10, sticky=W)

        days = ["S", "M", "T", "W", "T", "F", "S"]
        self.on_day_vars = []
        self.day_vars = {}
        for idx, day in enumerate(days):
            var = StringVar(value="off")
            cb = CTkCheckBox(days_frame, text=day, variable=var, onvalue="on", offvalue="off", width=0, height=0)
            cb.grid(row=1, column=idx, pady=5, ipady=10, padx=13)
            self.day_vars[idx] = var

        # Back button to AlarmPage
        back = CTkButton(self, text="Back", font=header_font, width=100, command=goBack, fg_color="transparent")
        back.grid(row=6, column=0, padx=70, pady=50, sticky=W)

        # Submit button
        submit = CTkButton(self, text="Submit", font=header_font, width=100, command=submit_alarm, 
                           fg_color="transparent")
        submit.grid(row=6, column=1, padx=70, pady=50, sticky=E)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1) 
