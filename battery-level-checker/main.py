
#----------------------------------------------
#psutil is a module to for system monitoring
#----------------------------------------------


import psutil

battery = psutil.sensors_battery()

if battery is None:
    print("battery info not available")
else:
    print(f"battery percentage:{battery.percent:6f}%")


#this is to check low percentage
battery = psutil.sensors_battery()

percent = battery.percent

if percent < 20:
    print(f"battery is low {percent}")
else:
    print("battery is good")
