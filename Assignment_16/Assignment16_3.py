def Add(No1,No2):
    Ans=No1+No2

    return Ans
    

def main():
    num1=int(input("Enter the Number 1: "))
    num2=int(input("Enter the Number 2: "))
    Result=Add(num1,num2)
    print("Addition is :",Result)

if __name__=="__main__":
    main()