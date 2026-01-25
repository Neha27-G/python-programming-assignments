def CountDigits(No):
    count = 0
    while No != 0:
        No = No // 10   # remove last digit
        count += 1
    return count

def main():
    Num = int(input("Enter the number: "))
    Result = CountDigits(Num)
    print("Number of digits is:", Result)

if __name__ == "__main__":
    main()
