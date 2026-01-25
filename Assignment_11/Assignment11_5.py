def Palindrome(n):
    temp = n
    rev = 0

    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10

    if temp == rev:
        print("It is palindrome")
    else:
        print("It is Not palindrome")

def main():
    n=int(input("Enter the Number: "))
    Palindrome(n)

if __name__=="__main__":
    main()