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


def Maximum(Elements) :
    Max = 0
    for i in Elements :
        if i > Max :
            Max = i
                    
    print("Maximum Element : ",Max)
    print("--------------------------------------------------------------------------")


def Minimum(Elements) :
    Min = Elements[0]

    for i in Elements :
        if i < Min :
            Min = i
                    
    print("Minmum Element : ",Min)
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

    T1 = threading.Thread(target = Maximum, args = (Data,))
    T2 = threading.Thread(target = Minimum, args = (Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")
    

if __name__ == "__main__" :
    main()