"""
55 is a magic number
5+5=10
1+0=1
"""

def magic(n):
    m=0
    if n<10 and n!=1:
        print(n)
        return False
    
    while n>0:
        d=n%10
        m=m+d
        n=int(n/10)
        print(d,m,n)
    
    if m==1:
        return True
    else:
        print(m)
        magic(m)
    

n=int(input("Enter a number: "))
if magic(n)==True:
    print(str(n)+" is a magic number")
else:
    print(str(n)+" is not a magic number")
