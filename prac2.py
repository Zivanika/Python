import time
ti1=int(time.strftime("%H"))
if(5<ti1<12):
    print("Good Morning Ma'am")
elif(12<=ti1<=16):
    print("Good Afternoon Ma'am")
elif(16<=ti1<=20):
    print("Good Evening Ma'am")
else:
    print("Good Night Ma'am")