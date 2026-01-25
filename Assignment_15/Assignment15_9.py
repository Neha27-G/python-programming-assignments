from functools import reduce

def product_of_number(num):
    return reduce(lambda a,b: a*b,num)

def main():
    Number=[10,20,30,10,20]
    Result=product_of_number(Number)
    print("Product of all the element is:",(Result))

if __name__=="__main__":
    main()