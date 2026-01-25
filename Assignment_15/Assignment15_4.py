from functools import reduce

def AdditionReduce(num):
    return reduce(lambda a,b: a+b ,num)

def main():
    Number=[1,2,3,4,5,6,7,7,9,0]
    
    print("Addition of Elements are :",AdditionReduce(Number))

if __name__=="__main__":
    main()