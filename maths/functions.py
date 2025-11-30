import sys


def sf(text):
    n:int=0
    while True:
        try:
            n=int(input(text))
            break
        except ValueError:
            print("\033[A",end="")
            print("\033[K",end="\r")
    return n
        
def sec_to_time(sec:int):
    s=sec%60
    sec=int(sec/60)
    m=sec%60
    sec=int(sec/60)
    h=sec

    return f"{h}:{m}:{s}"
def clr(lines):
    for i in range(lines):
        print("\033[A",end="")
        print("\033[K",end="\r")

def quit(sig,frame):
    print("\nThanks for playing!")
    sys.exit(0)