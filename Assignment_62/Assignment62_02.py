def main():

    feature_map = [
        [3, 3, 3],
        [0, 0, 0],
        [-3, -3, -3]
    ]

    # ReLU
    relu_output = []
    for row in feature_map:
        new_row = []
        for val in row:
            if val < 0:
                new_row.append(0)
            else:
                new_row.append(val)
        relu_output.append(new_row)

    print("ReLU Output:")
    for r in relu_output:
        print(r)

    # Max Pooling (2x2)
    pooled = []
    size = 2

    for i in range(0, len(relu_output)-1, size):
        row = []
        for j in range(0, len(relu_output[0])-1, size):

            block = [
                relu_output[i][j],
                relu_output[i][j+1],
                relu_output[i+1][j],
                relu_output[i+1][j+1]
            ]

            max_val = max(block)
            row.append(max_val)

        pooled.append(row)

    print("\nMax Pooling Output:")
    for r in pooled:
        print(r)


if __name__ == "__main__":
    main()