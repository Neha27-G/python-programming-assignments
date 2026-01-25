def SumDigits(No):
    total = 0
    while No != 0:
        total += No % 10   # get last digit and add to total
        No = No // 10      # remove last digit
    return total

def main():
    Num = int(input("Enter the number: "))
    Result = SumDigits(Num)
    print("Sum of digits is:", Result)

if __name__ == "__main__":
    main()
