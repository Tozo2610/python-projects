import random
import functions

def output(name,interests):
    careers=functions.career_csv_to_dict("careers.csv")
    user_careers=functions.user_career_csv_to_dict("user_careers.csv")
    suggestions1=[]
    suggestions2={}
    unknown_interests=[]
    functions.record_user("users.csv",name,interests)
    final_string=""
    print(interests,type(interests))
    interests=interests.split(",")
    print(interests,type(interests))
    for interest in interests:
        if interest in careers:
            c=careers[interest]
            random.shuffle(c)
            for x in c:
                suggestions1.append(x)
        elif interest in user_careers:
            del user_careers[interest][0]
            c=user_careers[interest]
            random.shuffle(c)
            suggestions2[interest]=c
        else:
            unknown_interests.append(interest)

    if suggestions1!=[]:
        final_string+="Here are some suggestions for your career based on your interests:\n"
        for x in suggestions1:
            final_string+="\t- "+x+"\n"

    if suggestions2!={}:
        final_string+="The careers suggestions for these interests have been provided by other users:\n"
        for l in suggestions2.keys():
            final_string+="Career suggestions for interest: "+l+"\n"
            for x in suggestions2[l]:
                final_string+="\t- "+x+"\n"
                
    return final_string
