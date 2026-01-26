import threading
import os


def ChkSmall(Elements) :
    i = 0
    Sum = 0

    for i in Elements :
        if (i >= 'a' and i<= 'z') :
            Sum = Sum + 1

    print("Sum of small elements is : ",Sum)

    print("Small Thread id : ",threading.get_ident())
    print("Thread name : ",threading.current_thread().name)

    print("----------------------------------------------------------------")


def ChkCapital(Elements) :
    i = 0
    Sum = 0

    for i in Elements :
        if (i >= 'A' and i<= 'Z') :
            Sum = Sum + 1

    print("Sum of capital elements is : ",Sum)

    print("Capital Thread id : ",threading.get_ident())
    print("Thread name : ",threading.current_thread().name)

    print("----------------------------------------------------------------")


def ChkNumbers(Elements) :
    i = 0
    Sum = 0

    for i in Elements :
        if (i >= '0' and i<= '9') :
            Sum = Sum + 1

    print("Sum of numeric elements is : ",Sum)

    print("Numbers Thread id : ",threading.get_ident())
    print("Thread name : ",threading.current_thread().name)

    print("----------------------------------------------------------------")
        


def main() :
    Data = ""
    
    print("Enter String : ")
    Data = (input())

    Small = threading.Thread(target = ChkSmall, args = (Data,))
    Capital = threading.Thread(target = ChkCapital, args = (Data,))
    Numbers = threading.Thread(target = ChkNumbers, args = (Data,))

    Small.start()
    Small.join()

    Capital.start()
    Capital.join()

    Numbers.start()
    Numbers.join()

    print("Exit from main")
    

if __name__ == "__main__" :
    main()