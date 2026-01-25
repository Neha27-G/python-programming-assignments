def primeNum(No):
    if No<=1:
        return False
    
    for i in range(2,No):
        if No%i==0:
            return False
    return True

def main():
    Num=int(input("Enter the Number: "))
    if primeNum(Num):
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")
   
if __name__=="__main__":
    main()