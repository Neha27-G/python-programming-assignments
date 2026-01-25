import Arithmatic

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition:", Arithmatic.add(num1, num2))
    print("Subtraction:", Arithmatic.sub(num1, num2))
    print("Multiplication:", Arithmatic.multi(num1, num2))
    print("Division:", Arithmatic.div(num1, num2))

if __name__ == "__main__":
    main()
