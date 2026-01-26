
import threading


def SumEven(Elements) :
    i = 0
    sum = 0

    for i in  Elements :
            if (i%2 == 0) :
                sum = sum + i
    
    print("Sum of Even Elements is : ",sum)


def SumOdd(Elements):
    i = 0
    sum = 0

    for i in Elements :
            if (i%2 != 0) :
                sum = sum + i
    
    print("Sum of Odd Elements is : ",sum)      


def main() :
    Value = 0
    i=0
    Data=list()

    print("Enter elements which want in list : ")
    Size = int(input())
 
    print("Enter numbers : ")
    for i in range (Size) :
        Value = int(input())
        Data.append(Value)

    T1 = threading.Thread(target = SumEven, args = (Data,))
    T2 = threading.Thread(target = SumOdd, args = (Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")
if __name__ == "__main__" :
    main()