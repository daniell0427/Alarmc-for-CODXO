import uuid
import os
import threading
from datetime import datetime
import winsound

#generate uuid
def generate_uuid():
    return str(uuid.uuid4())

#get uuid
def get_uuid():
    file_path = 'cache/uuid.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()
    else:
        user_identifier = generate_uuid()
        with open(file_path, 'w') as file:
            file.write(user_identifier)
        return user_identifier
    

def play_alarm(alarm_time, repeat):
    sound = "resources/alarm.wav"
    day = str((datetime.now().weekday() + 1) % 7)
    def check_time():
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time and day in repeat:
            winsound.PlaySound(sound, winsound.SND_ASYNC)
            threading.Timer(30, stop_alarm).start()
        else:
            threading.Timer(1, check_time).start()

    def stop_alarm():
        winsound.PlaySound(None, winsound.SND_ASYNC)

    check_time()