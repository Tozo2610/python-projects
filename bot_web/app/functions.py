import os
import pathlib

def career_csv_to_dict(file):
    dir=str(pathlib.Path(__file__).parent.resolve())+"/"
    dict={}
    careers=[]
    try:
        f=open(dir+file)
    except:
        print("A critical error occured. Please try again")
        os._exit(1)
    
    for line in f.readlines():
        careers=[]
        words=line.split(",")
        interest=words[0]
        for i in range(1,len(words)):
            careers.append(words[i].replace("\n",""))
        dict[interest]=careers

    return dict

def user_career_csv_to_dict(file):
    dir=str(pathlib.Path(__file__).parent.resolve())+"/"
    dict={}
    careers=[]
    try:
        f=open(dir+file)
    except:
        print("A critical error occured. Please try again")
        os._exit(1)

    for line in f.readlines():
        careers_score=[]
        words=line.split(",")
        careers_score.append(words[0])
        interest=words[2]
        for i in range(3,len(words)):
            careers_score.append(words[i].replace("\n",""))
        dict[interest]=careers_score
    
    return dict

def record_user(file,user,interests):
    dir=str(pathlib.Path(__file__).parent.resolve())+"/"
    try:
        f=open(dir+file,'a')
    except:
        print("A critical error occured. Please try again")
        os._exit(1)
    
    istr=str(interests).replace("[","").replace("]","").replace("\'","").replace(" ","")
    text=user+","+istr
    f.write(text+"\n")

def record_user_careers(file,user,interest,careers):
    dir=str(pathlib.Path(__file__).parent.resolve())+"/"
    try:
        f=open(dir+file,'a')
    except:
        print("A critical error occured. Please try again")
        os._exit(1)
    
    cstr=str(careers).replace("[","").replace("]","").replace("\'","")
    text="0"+","+user+","+interest+","+cstr
    f.write(text+"\n")

def update_score(file,interest,change):
    dir=str(pathlib.Path(__file__).parent.resolve())+"/"
    try:
        f=open(dir+file,'r')
    except:
        print("A critical error occured. Please try again")
        os._exit(1)

    lines=f.readlines()
    f.close()
    f=open(dir+file,"w")
    #We first copied everyhting from the file and then we will write this again into the file
    #because python cannot open a file normally for some reason and it deletes everything when
    #I use the 'w' option. So, this is a workaround
    for l in lines:
        m=l.split(",")
        s=""
        if m[2]==interest:
            m[0]=str(int(m[0])+change)
        for i in range(0,len(m),1):
            if i!=len(m)-1:
                s=s+m[i]+","
            else:
                s=s+m[i]
        f.write(s)

def display_careers(ms):
    dir=str(pathlib.Path(__file__).parent.resolve())+"/static/"
    rt=dir+"results_template.html"
    r=dir+"results.html"
    f=open(rt,"r")
    ts=""
    bs=""

    for l in f.readlines():
        if l.strip()=="<!--End of top section-->":
            ts+=l
            break
        else:
            ts+=l
    f.close()
    f=open(rt,"r")
    c=False
    for l in f.readlines():        
        if l.strip()=="<!--Start of bottom section-->":
            c=True
        if c:
            bs+=l
    
    f.close()
    f=open(r,"w")
    s=ts+"\n"+ms+"\n"+bs
    f.write(s)