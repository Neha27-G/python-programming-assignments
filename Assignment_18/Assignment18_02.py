def main():
    n=int(input("Enter the Number of Elements :"))
    lst=[]
    max_num=0

    for i in range(n):
        num=int(input("Enter the Element :"))
        lst.append(num)
   
    max_num=lst[0]
     
    for num in lst:
         if num> max_num:
            max_num=num

    print("Maximum Number is :",max_num)

if __name__=="__main__":
    main()