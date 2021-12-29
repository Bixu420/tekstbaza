x=int(input())
i=0
if x<0 or x>100:
    quit()
while x!=1:
    if x%2==0:
        x=x/2
        print(x)
    else:
        x=3*x+1
        print(x)
    i=i+1
print("zajelo to", i ,"obliczen")