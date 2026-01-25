from functools import reduce

def MinReduce(num):
    return reduce(lambda a,b: a if a<=b else b,num)

def main():
    Number=[1,2,3,4,5,6,7,77,9]
    
    print("Minimum Element is :",MinReduce(Number))

if __name__=="__main__":
    main()