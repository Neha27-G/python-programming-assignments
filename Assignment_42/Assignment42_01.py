import math

def main():

    # Dataset
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    n = len(X)

    # Mean of X
    mean_x = sum(X) / n

    # Mean of Y
    mean_y = sum(Y) / n

    # Calculate slope (m)
    numerator = 0
    denominator = 0

    for i in range(n):
        numerator += (X[i] - mean_x) * (Y[i] - mean_y)
        denominator += (X[i] - mean_x) ** 2

    m = numerator / denominator

    # Calculate intercept (c)
    c = mean_y - (m * mean_x)

    print("Mean of X =", mean_x)
    print("Mean of Y =", mean_y)

    print("Slope (m) =", round(m, 2))
    print("Intercept (c) =", round(c, 2))

    print("Regression Equation: Y =", round(m, 2), "X +", round(c, 2))

    # Predict Y for X = 6
    x_new = 6
    y_pred = m * x_new + c

    print("Predicted Y for X =", x_new, "=", round(y_pred, 2))


if __name__ == "__main__":
    main()