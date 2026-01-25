def addition(No1,No2):
    Ans=No1+No2
    return Ans

def Subtraction(No1,No2):
    Ans=No1-No2
    return Ans

def Multiplication(No1,No2):
    Ans=No1*No2
    return Ans

def Division(No1,No2):
    if No2==0:
        return "Cannot divide by zero"
    return No1 / No2

def main():
    No1=int(input("Enter the 1st Number :"))
    No2=int(input("Enter the 2nd Number :"))

    print("Addition is :",addition(No1,No2))
    print("Subtraction is :",Subtraction(No1,No2))
    print("Multiplication is :",Multiplication(No1,No2))
    print("Division is :",Division(No1,No2))

if __name__=="__main__":
    main()
