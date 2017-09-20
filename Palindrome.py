#Palindrome
x=input("input word: ")
x=x.casefold()
reversex=reversed(x)
if list(x) == list(reversex):
    print ("True")
else:
    print ("False")

#Fibbonaci
x=[0, 1]
for i in range(1, 15):
    lol=x[i-1] + x[i]
    x.append(lol)
print(x)




