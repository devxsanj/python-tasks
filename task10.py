import time 
from datetime import datetime

def digitalClock():
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        print("current time:", now , end="\r")
        time.sleep(1)


digitalClock()