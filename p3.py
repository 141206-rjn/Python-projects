import time
import sys


def digi_clock():
   while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print("\rDigital Clock: " + current_time, end = '')
        time.sleep(1)

def count_down(seconds):
    print("CountDown Started:")
    while seconds >0 :
        print("\rTime remaining: "+ str(seconds) + "seconds",end ='')
        time.sleep(1)
        seconds -=1 
    print("Time's up!")

if __name__ == '__main__':
    while True :
        choice =int(input("Choose an option 1 for clock or 2 for timer:"))   
        if choice == 1:
           digi_clock()
        elif choice == 2:
           time =int(print("Enter time in secoonds:"))
           count_down(time)
        else :
           print("Invalid choice")