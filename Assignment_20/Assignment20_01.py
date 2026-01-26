import threading

def PrintEven() :
    i = 1
    No = 10*2

    print("Even numbers : ")
    while(No != 0) :
        if(i%2 == 0) :
            print(i, end = "\t")
        i = i + 1
        No = No-1
        
    print("")

def PrintOdd() :
    i = 1
    No = 10*2

    print("Odd numbers : ")
    while(No != 0) :
        if(i%2 != 0) :
            print(i, end = "\t")
        i = i + 1
        No = No-1
        
    print("")   


def main() :
    Even = threading.Thread(target = PrintEven)
    Odd = threading.Thread(target = PrintOdd)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()
    
if __name__ == "__main__" :
    main()