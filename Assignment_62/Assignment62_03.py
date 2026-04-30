def main():

    matrix = [
        [6, 4],
        [8, 6]
    ]

    # Flatten
    flatten = []
    for row in matrix:
        for val in row:
            flatten.append(val)

    print("Flatten Output:", flatten)

    # Fully Connected Layer (manual)
    weights = [0.5, 0.2, 0.1, 0.7]
    bias = 1

    output = 0
    for i in range(len(flatten)):
        output += flatten[i] * weights[i]

    output += bias

    print("Final Output:", output)


if __name__ == "__main__":
    main()