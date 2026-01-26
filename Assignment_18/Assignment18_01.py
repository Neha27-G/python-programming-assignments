def main():
    n=int(input("Enter the Number of Elements :"))
    lst=[]
    total=0

    for i in range(n):
        num=int(input("Enter the Element :"))
        lst.append(num)
        total=total+num

    print("Addition is :",total)

if __name__=="__main__":
    main()