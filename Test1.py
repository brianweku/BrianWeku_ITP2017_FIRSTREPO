x=2000
y=3200
number=[]
for i in range (x, y+1):
    if(i%7==0 and i%5!=0):
        print(i, end=(", "))

