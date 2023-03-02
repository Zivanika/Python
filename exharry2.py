import time
# timestamp=time.strfttime('%H:%M:%S')
# print(timestamp)
t1=int(time.strftime("%H"))
if(5<t1<12):
    print("Good Morning!")
elif(12<=t1<=15):
    print("Good Afternoon!")
elif(15<=t1<=20):
    print("Good Evening!")
else:
    print("Good Night!")
  

