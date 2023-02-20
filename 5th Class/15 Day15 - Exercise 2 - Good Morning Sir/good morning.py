import time
currentTime = int(time.strftime('%H'))   

a = "Zidi"

if currentTime < 12 :
     print('Good morning', a)
elif currentTime > 12 :
     print('Not morning', a)
if currentTime > 12 :
     print('Good afternoon', a)
if currentTime > 6 :
     print('Good evening', a)