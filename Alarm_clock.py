from datetime import datetime
import winsound 

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm...")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")
    if current_hour == alarm_hour:
        if current_minute == alarm_minute:
            if current_second == alarm_second:
                if current_period == alarm_period:
                    print("wake up !!!")
                    winsound.Beep(500, 10000)
                    break

