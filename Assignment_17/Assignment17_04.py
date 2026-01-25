def AddFactors(No):
    fact=0
    for i in range(1,No): #excluding itself 
        if No%i==0:
            fact+=i
    return fact

def main():
    Num=int(input("Enter the Number: "))
    Result=AddFactors(Num)
    print("Factorial is :",Result)
   
if __name__=="__main__":
    main()