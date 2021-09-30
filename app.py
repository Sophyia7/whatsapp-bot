import pywhatkit
from datetime import datetime 

today = datetime.now()

shour = today.strftime("%H")
mobile_no = input('Enter Mobile Number of Receiver: ')
message = input('Enter Message you want to send : ')
hour = int(input('Enter hour : '))
minute = int(input('Enter minute : '))

pywhatkit.sendwhatmsg(mobile_no,message,hour,minute)