import datetime
import time
import webbrowser

alarm_time = input("Set alarm time (HH:MM): ")

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print("🔔 Wake up!")
        webbrowser.open("https://www.youtube.com/watch?v=2vjPBrBU-TM")  # Alarm sound
        break
    time.sleep(30)
