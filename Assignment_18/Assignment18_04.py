def main():
    n=int(input("Enter the Number of Elements :"))
    lst=[]

    for i in range(n):
        num=int(input("Enter the Element :"))
        lst.append(num)
   
    search=int(input("Enter the number to find the frequency :"))
    count=0

    for num in lst:
         if num==search:
             count=count+1

    print("Frequency of the Number is :",count)

if __name__=="__main__":
    main()