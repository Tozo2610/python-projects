emojis = [
    "\U0001F538",  # 🔸 Small Orange Diamond 0
    "\U0001F539",  # 🔹 Small Blue Diamond   1
    "\U0001F31F",  # 🌟 Glowing Star         2
    "\U0001F4A0",  # 💠 Diamond with a Dot   3
    "\U0001F4AB",  # 💫 Dizzy Symbol         4
    "\u2728",      # ✨ Sparkles             5
    "\U0001F308"   # 🌈 Rainbow              6
]

'''
ssssssss🔸🌟🔸 8            020
ssssss🔹🌟💠🌟🔹 6          12321
ssss🔸🌟💠💫💠🌟🔸 4        0234320
ss🔹🌟💠💫✨💫💠🌟🔹 2      123454321
🔸🌟💠💫✨🌈✨💫💠🌟🔸 0    02345654320
ss🔹🌟💠💫✨💫💠🌟🔹 2      123454321
ssss🔸🌟💠💫💠🌟🔸 4        0234320
ssssss🔹🌟💠🌟🔹 6          12321
ssssssss🔸🌟🔸 8            020

'''

while (True):
    n=int(input("Enter a number lesser than or equal to 5:"))
    #The limit is because only this big of a pattern can be printed with the available emojis
    if n<0 or n>5:
        print("Please enter valid input")
    else:
        break

m=2*n
for i in range(1,m,1):
    for j in range(2*abs(n-i)):
        print(" ",end="")
    print(emojis[abs((i%2)-1)],end="") #first emoji done
    for j in range(n-abs(n-i)):
        print(emojis[n-abs(n-j)+2],end="")

    #Now just run it in reverse

    for j in range(n-abs(n-i)-1,0,-1):
        print(emojis[n-abs(n-j)+1],end="")

    print(emojis[abs((i%2)-1)],end="") #last emoji done
    print()