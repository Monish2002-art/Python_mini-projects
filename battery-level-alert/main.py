#This is a project for monitoring battery level of laptop ,while some important/big files and we  are unable to be
#with the latop so i created a mini project on monitoring battery level of laptop while we are away with some another important work

#I have used psutil library and twilio for monitoring and sending notification
#Twilio is as primarily used for automating customer interactions, building notification systems, 
# securing user accounts with 2FA, and powering contact center


import psutil
from twilio.rest import Client
from cred import acc_sid, auth_token #twilio credentials

battery = psutil.sensors_battery()

percent = battery.percent

client = Client(acc_sid,auth_token)

if percent < 90:
    message = client.messages.create(
        body = f"Your laptop's battery percentage is {percent}%, You need to charge now",
        from_="+19094793922",
        to ="+919597362259"
    )
    print(f"message sent at {percent}%")

else:
    print(f"message sent at {percent}%, chill you battery has life for now!!")
