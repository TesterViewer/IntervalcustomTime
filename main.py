from win10toast import ToastNotifier
import datetime

toaster = ToastNotifier()
isTimeUp = True
isRunning = True
currTime = datetime.datetime.now()
ivalTime = datetime.datetime.now()
while isRunning == True:
  if isTimeUp == True:
    currTime = datetime.datetime.now()
    ivalTime = datetime.datetime.now()
    toaster.show_toast("Timer","Time Up!!!")
    isTimeUp = False
  elif isTimeUp == False:
    if ivalTime.minute - currTime.minute >= 5:
      isTimeUp = True
    else:
      ivalTime = datetime.datetime.now()
      isTimeUp = False

  