import threading
 
def ChkPrime(No) :
    sum = 0

    for i in range (1,No) :
        if (No%i == 0) :
            sum = sum+1
    
    if(sum == 1) :
        return True
    else :
        return False


def Prime(Elements) :
    i = 0
    Ret = False
    PrimeElements = list()

    for i in Elements :
            Ret = ChkPrime(i) 

            if(Ret == True) :
                PrimeElements.append(i)
                    
    print("Prime Elements : ",PrimeElements)
    print("--------------------------------------------------------------------------")


def NonPrime(Elements) :
    i = 0
    Ret = False
    NonPrimeElements = list()

    for i in Elements :
            Ret = ChkPrime(i) 

            if(Ret == False) :
                NonPrimeElements.append(i)
                    
    print("Non Prime Elements : ",NonPrimeElements)  
    print("--------------------------------------------------------------------------")  

def main() :
    Value = 0
    i = 0
    Data = list()

    print("Number of elements you want in list : ")
    Size = int(input())
    
    print("Enter numbers : ")
    for i in range (Size) :
        Value = int(input())
        Data.append(Value)

    T1 = threading.Thread(target = Prime, args = (Data,))
    T2 = threading.Thread(target = NonPrime, args = (Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")
    

if __name__ == "__main__" :
    main()