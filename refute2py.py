def checkHarshad(n):
    x = sum(int(i) for i in str(n))
    return n%x == 0 
    

while a != "y":
    n =  int(input(" Enter the number you want to check : "))
    if checkHarshad(n):
        print ("the entered number is a Harshad number")
    else:
        print ("the entered number is not a Harshad number")

        a = input("do you want continue ? (y/n):")
