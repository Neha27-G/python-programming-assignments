
import threading


def SumEvenFactors(No) :
    i = 0
    sum = 0

    for i in range (1,(No+1)) :
        if (No%i == 0) :
            if (i%2 == 0) :
                sum = sum + i
    
    print("Sum of Even Factors is : ",sum)


def SumOddFactors(No) :
    i = 0
    sum = 0

    for i in range (1,(No+1)) :
        if (No%i == 0) :
            if (i%2 != 0) :
                sum = sum + i
    
    print("Sum of Odd Factors is : ",sum)      


def main() :
    Value = 0

    print("Enter number : ")
    Value = int(input())

    EvenFactors = threading.Thread(target = SumEvenFactors, args = (Value,))
    OddFactors = threading.Thread(target = SumOddFactors, args = (Value,))

    EvenFactors.start()
    OddFactors.start()

    EvenFactors.join()
    OddFactors.join()

    print("Exit from main")
    

if __name__ == "__main__" :
    main()