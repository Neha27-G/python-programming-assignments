def main():

    image = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [1,1,1,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]

    kernel = [
        [-1,-1,-1],
        [ 0, 0, 0],
        [ 1, 1, 1]
    ]

    k = 3
    output = []

    print("----- Convolution Steps -----\n")

    for i in range(len(image) - k + 1):
        row = []
        for j in range(len(image[0]) - k + 1):

            sum_val = 0
            print(f"Region ({i},{j}):")

            for ki in range(k):
                for kj in range(k):
                    img = image[i+ki][j+kj]
                    ker = kernel[ki][kj]
                    prod = img * ker
                    sum_val += prod

                    print(f"{img} * {ker} = {prod}")

            print("Sum =", sum_val)
            print("-------------------")

            row.append(sum_val)

        output.append(row)

    print("\nFeature Map:")
    for r in output:
        print(r)


if __name__ == "__main__":
    main()