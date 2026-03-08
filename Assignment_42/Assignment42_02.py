import numpy as np

def main():

    # Dataset
    X = np.array([1,2,3,4,5])
    Y = np.array([3,4,2,4,5])

    n = len(X)

    # Mean
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("Mean of X =", mean_x)
    print("Mean of Y =", mean_y)

    # Calculate slope
    num = np.sum((X-mean_x)*(Y-mean_y))
    den = np.sum((X-mean_x)**2)

    m = num/den

    # Calculate intercept
    c = mean_y - m*mean_x

    print("Slope (m) =", round(m,2))
    print("Intercept (c) =", round(c,2))

    print("Regression Equation: Y =",round(m,2),"X +",round(c,2))

    # Predict Y values
    Y_pred = m*X + c

    print("\nPredicted Y values:")
    for i in range(n):
        print("X =",X[i],"Actual Y =",Y[i],"Predicted Y =",round(Y_pred[i],2))

    # Calculate MSE
    mse = np.mean((Y - Y_pred)**2)

    print("\nMean Squared Error (MSE) =", round(mse,2))

    # Calculate R2 Score
    ss_res = np.sum((Y - Y_pred)**2)
    ss_tot = np.sum((Y - mean_y)**2)

    r2 = 1 - (ss_res/ss_tot)

    print("R2 Score =", round(r2,2))


if __name__ == "__main__":
    main()