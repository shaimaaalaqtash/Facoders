print("Numbers from 1 to 10")
x=6
m=int(input("Guess the number: "))
while m!=x and m>=1 and m<=10 :
    m=int(input("Guess the number:"))
if m==x :
    print("Great! you did it! ")
