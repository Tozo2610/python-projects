from time import sleep
import functions as f
import random as r
import signal

signal.signal(signal.SIGINT,f.quit) #To handle ctrl-c and give a proper message

print("Welcome to The Digital Handcricket by Jishnu Das")
print("##################################")
print("\t\tTOSS")
print("##################################")

while True:
    choice=input("What would like to choose? Head or Tails? [H/T]: ")
    if choice.upper()=="H":
        choice=0 #0=heads
    elif choice.upper()=="T":
        choice=1 #1=tails
    else:
        f.clr(1) #clear the input line
        continue

    toss=r.randint(0,1) #Coin toss
    if choice==toss:
        print("You won the toss!")
        while (True):
            batorball=input("What would you like to do? Bat or Bowl? [1 for Batting, 2 for Bowling]: ")
            if batorball.isdigit():
                batorball=int(batorball)
                if batorball!=1 and batorball!=2: 
                    f.clr(1) #clear input line and retry
                    continue
                else:
                    break #got correct input, continue to next part of program
            else:
                f.clr(1) #clear the input line and retry
                continue
        if batorball==1:
            print("You have chosen to bat first")
        else:
            print("You have chosen to bowl first")
    else:
        print("You lost the toss.")
        batorball=r.randint(1,2) #opponent chooses
        if batorball==1: #since 1 means player bats, opponent bowls
            print("Your opponent chose to bowl first")
        else: #since 2 means player bowls, opponent bats
            print("Your opponent chose to bat first")

    while (True):
        try:
            wickets_allowed=int(input("Enter number of wickets: "))
            if wickets_allowed<1:
                raise ValueError #I choose ValueError here because it makes sense in this case.
                                 #It is used in another place as well
            else:
                break #got correct input, continue to next part of program
        except ValueError:
            f.clr(1) #clear the input line and retry
            continue

    print("##################################")
    for i in range(3,0,-1): #countdown
        print(f"\tMatch starts in {i}",end="\r")
        sleep(1)
    
    # I use this string "\033[K" and "\033[A" very often both in this file and the functions file
    # "\033[K" clears the entire line where the cursor is
    # "\033[A" moves the cursor up one line. This is not used here but is used in functions.py

    print("\033[K", end="\r")
    print("\tMatch started!")
    print("##################################")

    runs_player=0
    runs_opponent=0
    wf_player=0 #wickets fallen for player
    wf_opponent=0 #wickets fallen for opponent
    m=0 #player's move
    ball=1 #ball number
    if batorball==1: #that is, player bats
        currently_batting=0 #0 stands for player
    else: #that is, player bowls
        currently_batting=1 #1 stands for opponent
    moves=[] #for storing in games.csv
    target=0

    # Now, the actual game starts. 
    # Player bats or bowls and opponent responds.
    # The numbers after some lines correspond to...
    # ...the lines that need to removed after every ball is played

    while (True):
        if currently_batting==0:
            print(f"Your score: {runs_player}-{wf_player}",end="")    #1
        else:
            print(f"Your opponent's score: {runs_opponent}-{wf_opponent}",end="  ")    #1
        
        if target!=0: #Batting just got over, other player now bats
            print(f"[Target is {target}]")
            ball=1 #reset
        else:
            print() #since, end="\r" was used

        while (True):
            try:
                m=int(input("Enter your move [1-6]: ")) #2
                if m<1 or m>6: #move must be between 1 and 6
                    raise ValueError
                else: #correct input
                    break
            except ValueError:
                f.clr(1) #clear the input line and retry
                continue

        moves.append(m) #for storing in games.csv
        t=r.randint(1,4) #random time to wait (0.6s to 2.4s) as if opponent is human
        for i in range(t): #the loading-type animation of dots is really good
            print("\033[KOpponent is thinking.",end="\r")
            sleep(0.2)
            print("\033[KOpponent is thinking..",end="\r")
            sleep(0.2)
            print("\033[KOpponent is thinking...",end="\r")
            sleep(0.2)

        om=int(f.read_most_probable("most_probable.csv",ball)) #TODO:This is not complete yet. Have to create different codes for batting and bowling

        print(f"\033[KOpponent gave: {om}") #3

        if currently_batting==0 and om==m: #if player is batting and both gave the same move
            print("You lost a wicket!") #4
            wf_player=wf_player+1 #add to wickets lost
            if wf_player==wickets_allowed: #all out
                target=runs_player+1
                print(f"All out!\nYour score is {runs_player}-{wf_player}.\nOpponent must score",target,"to win.")
                sleep(5) #enough time for player to read
                f.clr(7) #clear all these lines
                currently_batting=1 #shift batting to opponent
                continue
        elif currently_batting==1 and om==m: #if opponent is batting and both gave the same move
            print("You took your opponent's wicket!")
            wf_opponent=wf_opponent+1
            if wf_opponent==wickets_allowed:
                target=runs_opponent+1
                print(f"All out!\nOpponent's score is {runs_opponent}-{wf_opponent}.\nYou must score",target,"to win.")
                sleep(5)
                f.clr(7)
                currently_batting=0 #shift batting to player
                continue
        elif currently_batting==0: #if player is batting and both gave diiferent moves
            print(f"You scored {m} runs!")
            runs_player=runs_player+m #add to runs scored
        else: #last case: opponent is batting and different moves
            print(f"Your opponent scored {om} runs!")
            runs_opponent=runs_opponent+om

        ball=ball+1 #We are finally at the end of this ball
        sleep(2) #Allow player to read
        f.clr(4) #clear everything and get ready for the next ball
    break