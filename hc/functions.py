import pathlib
import random
import sys

def read_most_probable(file:str,move_no:int): #used in game to determine move
    #boilerplate code to access file safely
    dir=str(pathlib.Path(__file__).parent.resolve())+"/" 
    try:
        f=open(dir+file)
    except:
        print("A critical error occured. Please try again")
        sys.exit(1)

    #each line corresponds to the most probable move for that ball
    lines=f.readlines()
    if move_no<len(lines): #if the move number has any move associated with it, return it
        return lines[move_no-1] #line number n(say) corresponds to index n-1
    else: #else, random move
        return random.randint(1,6)

def write_game(file:str,game:list[str]): #store the game in games.csv
    #boilerplate code to access file safely
    dir=str(pathlib.Path(__file__).parent.resolve())+"/"
    try:
        f=open(dir+file,"a")
    except:
        print("A critical error occured. Please try again")
        sys.exit(1)

    #main.py gives an array of moves, but csv needs comma seperated values
    #so we make a string where we take each element and add it and a comma
    #except the last move
    text=""
    for x in game:
        text=text+x
        if game.index(x)!=len(game):
            text=text+","

    f.write(text)
    return

def calc_probability(games_file:str,prob_file:str,most_prob_file:str,extra_info_file:str):
    #boilerplate code to access files safely
    #also, we get the text already in the probabilites.csv and most_probable.csv files
    #because python deletes the file when opened with "w"
    dir=str(pathlib.Path(__file__).parent.resolve())+"/"
    try:
        gf=open(dir+games_file)

        pf=open(dir+prob_file,'r')
        prob_text=pf.read()
        pf.close()
        pf=open(dir+prob_file,"w")

        mpf=open(dir+most_prob_file,'r')
        most_prob_text=mpf.read()
        mpf.close()
        mpf=open(dir+most_prob_file,"w")

        ef=open(dir+extra_info_file)
    except:
        print("A critical error occured. Please try again")
        sys.exit(1)

    max_freq=[0,0]
    game_no=int(ef.read())
    game=gf.readlines()[game_no-1]
    game=game.split(",")
    prob_text=prob_text.splitlines()
    most_prob_text=most_prob_text.splitlines()
    print(most_prob_text)
    if len(game)<=len(prob_text):
        effective_length=len(game)
        c=0
    else:
        effective_length=len(prob_text)
        c=1

    for i in range(effective_length):
        t=prob_text[i].split(",")
        for j in range(6):
            ts=t[j].split(":")
            f=int(ts[1])
            if ts[0]==game[i]:
                t[j]=str(game[i])+":"+str(f+1)
                if f+1>max_freq[0]:
                    max_freq=[f,ts[0]]
            else:
                if f>max_freq[0]:
                    max_freq=[f,ts[0]]
        t_txt=""
        for x in t:
            t_txt=t_txt+x
            if t.index(x)!=len(t)-1:
                t_txt=t_txt+","
        prob_text[i]=t_txt
        most_prob_text[i]=str(max_freq[1])
        max_freq=[0,0]

    if c==1:
        for i in range(effective_length,len(game),1):
            t_txt=""
            for j in range(1,7,1):
                if j==int(game[i]):
                    t=str(j)+":1"
                else:
                    t=str(j)+":0"
                t_txt=t_txt+t
                if j!=6:
                    t_txt=t_txt+","
            
            prob_text.append(t_txt)
            most_prob_text.append(str(game[i]))
                
    prob_text_to_write=""
    most_prob_text_to_write=""
    for i in range(len(prob_text)):
        prob_text_to_write=prob_text_to_write+prob_text[i]
        most_prob_text_to_write=most_prob_text_to_write+most_prob_text[i]
        if i!=len(prob_text)-1:
            prob_text_to_write=prob_text_to_write+"\n"
            most_prob_text_to_write=most_prob_text_to_write+"\n"
    
    pf.write(prob_text_to_write)
    mpf.write(most_prob_text_to_write)
    return

def clr(lines):
    for i in range(lines):
        print("\033[A",end="")
        print("\033[K",end="\r")

def quit(sig,frame):
    print("\nThanks for playing!")
    sys.exit(0)