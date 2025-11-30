from math import ceil
import signal
from functions import *
from random import randint,choice
import time

signal.signal(signal.SIGINT,quit) #To handle ctrl-c and give a proper message

score=0
"""
0->10: 1D+-*/2D:1 pts
10->30: 2D+-*/2D: 2pts
30->60: 2D+-*/3D: 3pts
60->100: 3D+-*/3D: 4pts
"""

print("Welcome to Maths Quiz!")
time.sleep(1)

clr(1)
operators=["+","-","*"]
q=1
t1=int(time.time())
while (True):
    print("Score:",score)
    if (score<10):
        a=randint(0,9)
        b=randint(10,99)
    elif score<30:
        a=randint(10,99)
        b=randint(10,99)
    elif score<60:
        a=randint(100,999)
        b=randint(10,99)
    else:
        a=randint(100,999)
        b=randint(100,999)

    o=choice(operators)
    print(f"Question {q}:",a,o,b)
    r=eval(f"{a}{o}{b}")
    i=sf("Enter your answer: ")
    if (i==r):
        print("Correct!")
        score=score+ceil(q/10)
        time.sleep(1)
    else:
        print(f"You suck. Its {r}, lol.")
        t2=int(time.time())
        print(f"AND you took {sec_to_time(t2-t1)} for this sorry performance")
        break
    q=q+1
    clr(4)