"""
6804 is a multiple Harshad number
6804=6+8+0+4=18
6804/18=378
378=3+7+8=18
378/18=21
21=2+1=3
21/3=7
"""

def is_harshad(n,c=0):
    m=n
    s=0
    while n>0:
        d=n%10
        s=s+d
        n=int(n/10)
    
    if m%s==0:
        if m/s<10:
            print(c)
            return True,c
        else:
            is_harshad(m/s,c+1)
    else:
        return False,c

n=int(input("Enter a number: "))
r=is_harshad(n)
print(r)
if r[0]==True and r[1]>1: # type: ignore
    print(str(n)+" is a multiple Harshad number.")
else:
    print(str(n)+" is not a multiple Harshad number.")