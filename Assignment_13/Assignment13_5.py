def main():
    marks=float(input("Enter the Marks: "))

    if marks>=75:
        grade="Distinction"

    elif marks>=60:
        grade="First Class"

    elif marks>=50:
        grade="Second Class"

    else:
        grade="Fail"

    print("Grade :",grade)
        
if __name__ == "__main__":
    main()
