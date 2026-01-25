def main():
    maximum= lambda a,b : a if a>b else b

    x=int(input("Enter the First Number: "))
    y=int(input("Enter the Second Number: "))
    print("Maximum Number is :",maximum(x,y))

if __name__=="__main__":
    main()