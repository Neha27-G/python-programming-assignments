def main():
    minimum= lambda a,b : a if a<b else b

    x=int(input("Enter the First Number: "))
    y=int(input("Enter the Second Number: "))
    print("Minimum Number is :",minimum(x,y))

if __name__=="__main__":
    main()