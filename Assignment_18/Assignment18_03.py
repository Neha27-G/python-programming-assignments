def main():
    n=int(input("Enter the Number of Elements :"))
    lst=[]
    

    for i in range(n):
        num=int(input("Enter the Element :"))
        lst.append(num)

    minimum_num=lst[0]

    for num in lst:    
        if num<minimum_num:
            minimum_num=num

    print("Minimum Number is :",minimum_num)

if __name__=="__main__":
    main()