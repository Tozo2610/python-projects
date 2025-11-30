while True:
    b1=int(input("Enter the base(greater than 1 and less than 37) in which you want to enter your number: "))
    if b1<2 or b1>36:
        print("Base must be greater than or equal to 2 and less than or equal to 36")
    else:
        n1=(input(f"Enter the number in base {b1}: "))
        nums=[]
        letters=[]
        c=0
        for i in range(len(n1)):
            a=ord(n1[i])
            if a>=48 and a<=57: #its a number
                nums.append(int(chr(a)))
            elif (a>=65 and a<=90) or (a>=97 and a<=122): # its a letter
                letters.append(ord(chr(a).upper()))
            else:
                print("Invalid number")
                c=1
                break

        if c!=1:
            for n in nums:
                if n>=b1:
                    print("Invalid number")
                    c=1
                    break

            for l in letters:
                if b1<11:
                    print("Invalid number")
                    c=1
                    break
                else:
                    if l>(54+b1):
                        print("Invalid number")
                        c=1
                        break
                if c==1:
                    break
        if c==0:
            break

### Convert to decimal
d=0
if b1!=10:
    c=0
    for i in range(len(n1)-1,-1,-1):
        x=n1[i]
        a=ord(x.upper())
        if a>=48 and a<=57: #its a number
            d=d+int(x)*(b1**c)
        elif (a>=65 and a<=90): # its a letter
            d=d+(a-55)*(b1**c)
        c=c+1
else:
    d=int(n1)

tmp=d
for b2 in range(2,37):
    ###Convert to required base from decimal
    n2=""
    d=tmp
    while (d>0):
        r=d%b2
        d=d//b2
        if r>=10:
            char=chr(r+55)
        else:
            char=chr(r+48)
        n2=n2+char

    n2r=""
    for i in range(len(n2)-1,-1,-1):    
        n2r=n2r+n2[i]

    print(f"The number {n1} in base {b1} is {n2r} in base {b2}")