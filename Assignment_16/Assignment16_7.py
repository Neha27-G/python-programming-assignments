def DivisibleNum(No):
    return  No % 5==0
         
def main():
    num=int(input("Enter the Number :"))
    Result=DivisibleNum(num)
    print(Result)
   
if __name__=="__main__":
    main()


