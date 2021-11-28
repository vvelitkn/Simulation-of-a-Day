import time
import os
import sys
from threading import Thread
from msvcrt import getch
wakeup = False 
thread_running = True
os.system('cls')
print("Here we simulate a week of your dreams but in a real life process.")
time.sleep(5)
tree = """
 _______
| *   * |
|_ * * _|
  |   |
__|   |__
"""
os.system('cls')
def freshair():
    os.system("cls")
    i =0
    print(" "*i,"( ͡❛  ͟ʖ ͡❛)",end="")

    while True:
        choice = ord(getch())
        if choice == 224: #Special keys (arrows, f keys, ins, del, etc.)
            choice = ord(getch())
            if choice == 75:
                if i>0: i =i-1
                print ('\x1b[2K\r', end="")
                print(" "*i,"( ͡❛  ͟ʖ ͡❛)",end="")
            elif choice == 77:
                if i<100: i =i+1
                print ('\x1b[2K\r', end="")
                print(" "*i,"( ͡❛  ͟ʖ ͡❛)",end="")
            elif choice == 80:
                print ('\x1b[2K\r', end="")
                print("\n")
                print(" "*i,"( ͡❛  ͟ʖ ͡❛)",end="")
            elif choice == 72:
                print ('\x1b[2K\r', end="")
                sys.stdout.write("\033[F")
                print ('\x1b[2K\r', end="")
                print(" "*i,"( ͡❛  ͟ʖ ͡❛)",end="")
        
def game():
    os.system('cls')
    print()
def gameorair():
    print("Now what do you want to do: going outside or playing game")
    print("Select with arrow keys")
    while True:
        choice = ord(getch())
        if choice == 224: #Special keys (arrows, f keys, ins, del, etc.)
            choice = ord(getch())
            if choice == 75:
                print("Fresh air is better!!")
                freshair()
                return 0
            elif choice == 77:
                print("Let's play some")
                game()
                return 0
            else: 
                print("Please use only right or left arrow buttons")
        else: 
            print("Please use only right or left arrow buttons")


def kitchen():
    os.system("cls")
    print("Welcome to kitchen, what do you want to eat/drink?\n")
    print("Use left or right arrow button")
    breakfeasts = ["cereal", "traditional breakfast", "coffee&croissant"]
    for _ in breakfeasts:
        print(_, end="\t")
    print()
    i =0
    print("Your choice is: waiting",end="")
    while True:
        choice = ord(getch())
        if choice == 224: #Special keys (arrows, f keys, ins, del, etc.)
            choice = ord(getch())
            if choice == 75:
                if i<2: i =i+1
                print ('\x1b[2K\r', end="")
                print("Your choice is:", breakfeasts[i],end="")
            elif choice == 77:
                if i>0: i =i-1
                print ('\x1b[2K\r', end="")
                print("Your choice is:", breakfeasts[i],end="")
            key = ord(getch())
            if key == 13:
                print ('\x1b[2K\r', end="")
                print("Afied")
                os.system("cls")
                gameorair()
                return 0
                    

def bathroom():
    print("Welcome to bathroom, what do you wanna do?")
def clearall():
    os.system("cls")
def my_forever_while():
    global thread_running

    start_time = time.time()
    time.sleep(1)
    # run this while there is no input
    print("\n\n\n")
    print("\nYou:", end="\n")
    zzz = "zzz..."
    while (wakeup != True):
        for _ in zzz:
                print(_, end="")
                time.sleep(.2)
                if(wakeup ==True):
                    return 0
        print ('\x1b[2K\r', end="")
        time.sleep(.5)

        if(wakeup ==True):
            return False
def take_input():
    print("Press enter to wake up",end="")
    inputofuser = input()
    return 0
def kitchenbathroomchoice():
    while True:
        choice = ord(getch())
        if choice == 224: #Special keys (arrows, f keys, ins, del, etc.)
            choice = ord(getch())
            if choice == 75:
                print("Bathroom")
                bathroom()
                return 0
            elif choice == 77:
                print("Kitchen")
                kitchen()
                return 0
            else: 
                print("Please use only right or left arrow buttons")
        else: 
            print("Please use only right or left arrow buttons")

if __name__ == '__main__':
    t1 = Thread(target=my_forever_while)
    t2 = Thread(target=take_input)

    t1.start()
    t2.start()
    t2.join()  # interpreter will wait until your process get completed or terminated
    thread_running = False
    wakeup = True
    os.system("cls")
    print("You wake up!!", end='\r')
    time.sleep(2)
    print("Bathroom <---- You ----> Kitchen\n")
    print("Use left or right arrow button")
    kitchenbathroomchoice()
    



