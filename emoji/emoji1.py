emojis=["\U0001F31F"]
n=int(input("Enter a number: "))
m=2*n
for i in range(1,m,1):
    for j in range(abs(n-i)):
        print(" ",end="")
    for j in range(n-abs(n-i)):
        print(emojis[0],end="")
    print()
    