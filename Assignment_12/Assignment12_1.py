def main():
    ch=input("Enter the Character : ").lower()

    if ch in 'aeiou':
        print("It is vowel")
    else:
        print("It is Consonant")

if __name__=="__main__":
    main()