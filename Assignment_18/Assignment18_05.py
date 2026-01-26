import MarvellousNum

def ListPrime(lst):
    total=0

    for num in lst:
        if MarvellousNum.chkPrime(num):
            total=total+num
    return total

def main():
    n=int(input("Enter the Number of Elements :"))
    number=[]
    

    for i in range(n):
        num=int(input("Enter the Element :"))
        number.append(num)

    result=ListPrime(number)
    print("Addition of prime Numbers is :",result)

if __name__=="__main__":
    main()
