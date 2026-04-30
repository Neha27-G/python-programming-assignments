def main():
    # Inputs
    x = 2
    y_true = 1
    w = 0.5
    b = 0.1
    lr = 0.1

    # Forward pass
    y_pred = x * w + b
    print("Prediction:", y_pred)

    # Error
    error = y_true - y_pred
    print("Error:", error)

    # Weight update (gradient descent)
    w_old = w
    b_old = b

    w = w + lr * error * x
    b = b + lr * error

    print("Old Weight:", w_old)
    print("Updated Weight:", w)
    print("Old Bias:", b_old)
    print("Updated Bias:", b)


if __name__ == "__main__":
    main()