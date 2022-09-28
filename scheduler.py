from datetime import datetime
import os
import time


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    x = now.weekday()

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if current_time == '15:20' and x < 5:
        os.system('python main.py')
    time.sleep(60)