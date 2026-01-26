
import threading


def Display() :
    i = 0

    for i in range(1,(50+1)) :
        print(i,end = "\t")

    print("")
    print("----------------------------------------------------------------------------------------------")

def DisplayReverse() :
    i = 0

    for i in range(50,0,-1) :
        print(i,end = "\t")

    print("")
    print("----------------------------------------------------------------------------------------------")

def main() :
    t1 = threading.Thread(target = Display)
    t2 = threading.Thread(target = DisplayReverse)

    t1.start()
    t1.join()

    t2.start()
    t2.join()
    

if __name__ == "__main__" :
    main()