import random
import functions

careers=functions.career_csv_to_dict("careers.csv")
user_careers=functions.user_career_csv_to_dict("user_careers.csv")
suggestions1=[]
suggestions2={}
unknown_interests=[]

print("Welcome to Career Bot!")
print("A program developed by Jishnu Das(https://github.com/Tozo2610)")
name=input("Please enter your name: ")
print("Hello ",name,"!\nPlease enter your interests (in comma seperated form) from the following: ",sep="")
print("Technology, Art, Science, Business, Communication, Health, Education, Law, Environment, Sports, Engineering, Social Services, Culture")
interests=input("Your interests: ").split(",")
interests=[x.strip().lower() for x in interests]
functions.record_user("users.csv",name,interests)
for interest in interests:
    if interest in careers:
        c=careers[interest]
        random.shuffle(c)
        for x in c:
            suggestions1.append(x)
    elif interest in user_careers:
        uc_score=user_careers[interest][0]
        del user_careers[interest][0]
        c=user_careers[interest]
        random.shuffle(c)
        suggestions2[interest]=c
    else:
        unknown_interests.append(interest)

if suggestions1!=[]:
    print("Here are some suggestions for your career based on your interests:")
    for x in suggestions1:
        print("\t-",x)

if suggestions2!={}:
    print("The careers suggestions for these interests have been provided by other users: ")
    for l in suggestions2.keys():
        print("Career suggestions for interest:",l)
        for x in suggestions2[l]:
            print("\t-",x)
    
    c=input("Could you please tell whether these recommendations were good or not? Your vote will help create a better platform for all users.(Y/N): ")
    if c.lower()=="y":
        print("Thanks! Here's how to vote:\nEnter E for Excellent\nEnter G for Good\nEnter F for Fair\nEnter B for Bad\nEnter T for Terrible")
        for l in suggestions2.keys():
            v=input(f"Please enter your vote for the recommendations on {l}: ")
            v=v.lower()
            match v:
                case 'e':
                    score=3
                case 'g':
                    score=2
                case 'f':
                    score=1
                case 'b':
                    score=-1
                case 't':
                    score=-2
            functions.update_score("user_careers.csv",l,score)
    else:
        print("Okay, no problem.")

if unknown_interests!=[]:
    c=input("I could not understand a few of your interests. Would you like to help me know about them? (Y/N): ")
    if c.lower()=="y":
        for i in unknown_interests:
            print("Could you please tell me some careers related to your interest in",i+"?")
            uc=input("The careers: ").split(",")
            functions.record_user_careers("user_careers.csv",name,i,uc)
            
        print("Thank you very much. This information will surely help others looking for suggestions.")
    else:
        print("Okay, no problem. Bye!")
