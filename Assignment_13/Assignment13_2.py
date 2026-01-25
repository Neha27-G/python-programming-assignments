def Area_circle(r):
    pi=3.14
    return pi*r**2


def main():
    r=int(input("Enter the radius:"))

    print("Area of Circle is is",Area_circle(r))
    
if __name__=="__main__":
    main()