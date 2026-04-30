import math

def mse(y_true, y_pred):
    total = 0
    n = len(y_true)
    
    for i in range(n):
        total += (y_true[i] - y_pred[i]) ** 2
    
    return total / n


def bce(y_true, y_pred):
    total = 0
    n = len(y_true)
    
    for i in range(n):
        pred = max(min(y_pred[i], 1 - 1e-15), 1e-15)
        total += y_true[i] * math.log(pred) + (1 - y_true[i]) * math.log(1 - pred)
    
    return -total / n


def main():
    y_true = [1, 0, 1, 0]
    y_pred = [0.9, 0.2, 0.8, 0.1]

    print("Mean Squared Error:", mse(y_true, y_pred))
    print("Binary Cross Entropy:", bce(y_true, y_pred))


if __name__ == "__main__":
    main()