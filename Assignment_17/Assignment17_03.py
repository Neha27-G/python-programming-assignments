def Factorial(No):
    fact=1
    for i in range(1,No+1):
        fact=fact*i
    return fact

def main():
    Num=int(input("Enter the Number: "))
    Result=Factorial(Num)
    print("Factorial is :",Result)
   
if __name__=="__main__":
    main()