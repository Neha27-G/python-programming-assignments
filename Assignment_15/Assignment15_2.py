def EvenFilter(num):
    return list(filter(lambda a : a% 2==0 ,num))

def main():
    Number=[1,2,3,4,5,6,7,7,9,0]
    print("Even Numbers are :",EvenFilter(Number))

if __name__=="__main__":
    main()