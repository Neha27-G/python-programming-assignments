def main():
    a=int(input("Enter the Number : "))
    
    Fact=1
    i=1

    while (i<=a):

        Fact=Fact*i
        i=i+1

    print("Factorial is :",Fact)

if __name__ == "__main__":
    main()