from win10toast import ToastNotifier
import datetime

toaster = ToastNotifier()
isTimeUp = True
isRunning = True
timeUp = 5
currTime = datetime.datetime.now()
ivalTime = datetime.datetime.now()
while isRunning == True:
    if isTimeUp == True:
      if ivalTime.minute > currTime.minute:
        currTime = datetime.datetime.now()
        ivalTime = datetime.datetime.now()
      else:
        currTime = datetime.datetime.now()
      toaster.show_toast("TIMER OF LIFE","TAKING 5 MINUTES!!!")
      isTimeUp = False
    elif isTimeUp == False:
      if (((60 - currTime.minute) + ivalTime.minute) == timeUp) | (ivalTime.minute - currTime.minute >= timeUp):
        isTimeUp = True
      else:
        if ivalTime.minute > 59:
          ivalTime.minute = 0
        ivalTime = datetime.datetime.now()
        isTimeUp = False

