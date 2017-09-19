x=1
y=20
z=int(y/2)
a=int(y/2)
for i in range(x, y):
    if(i == z):
        print("*"*(y-1))

    if(i<z):
        print(" "*((z-1)-i), "*"*x)
        x+=2

    if(i>z):
        print(" "*(i-z-1), "*"*(y-3))
        y-=2

