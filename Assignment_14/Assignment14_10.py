def main():
    Largest= lambda a,b,c : a if (a>=b and a>=c) else (b if b>=c else c)

    x=int(input("Enter the First Number: "))
    y=int(input("Enter the Second Number: "))
    z=int(input("Enter the Third Number: "))
    print("Largest Number is :",Largest(x,y,z))

if __name__=="__main__":
    main()