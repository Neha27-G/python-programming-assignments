
def main():
    a=int(input("Enter the number: "))
    if(a%3==0 and a%5==0):
        print("Divisible by 3 and 5: ",a)
    else:
        print("Not Divisible by 3 and 5: ",a)

if __name__ == "__main__":
    main()