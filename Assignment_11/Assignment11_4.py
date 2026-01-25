def reverseNumber(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev

def main():
    n=int(input("Enter the number"))
    print("Reverse Number is :",reverseNumber(n))

if __name__=="__main__":
    main()

