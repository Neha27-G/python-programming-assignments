import threading
import concurrent.futures


def Addition(Elements) :
    sum = 0
    for i in Elements :
        sum = sum + i
                    
    return sum


def Product(Elements) :
    Mult = 1

    for i in Elements :
        Mult = Mult * i
                    
    return Mult


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

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor :
        future1 = executor.submit(Addition,Data)
        future2 = executor.submit(Product,Data)

    result1 = future1.result()
    result2 = future2.result()

    print("Addition is : ",result1)
    print("Product is : ",result2)
    
    print("Exit from main")
    

if __name__ == "__main__" :
    main()