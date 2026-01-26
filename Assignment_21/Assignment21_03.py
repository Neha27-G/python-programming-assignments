import threading

Counter = 0

def Increment(Elements) :
    global Counter 

    for i in range(5) :
        with threading.Lock() :
            Counter = Counter + 1


def Decrement(Elements) :
    global Counter 

    for i in range(3) :
        with threading.Lock() :
            Counter = Counter - 1


def main() :
    Value = 0
    global Counter
    
    print("Enter number : ")
    Value = int(input())

    T1 = threading.Thread(target = Increment, args = (Value,))
    T2 = threading.Thread(target = Decrement, args = (Value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Shared variable value at the end : ",Counter)

    print("Exit from main")
    

if __name__ == "__main__" :
    main()