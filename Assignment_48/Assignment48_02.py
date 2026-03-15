import numpy as np
from sklearn.preprocessing import StandardScaler

def calculate_statistics(data):
    scaler = StandardScaler()
    scaler.fit(data)

    variance = scaler.var_[0]
    std_dev = np.sqrt(variance)

    return variance, std_dev


def main():
    # Dataset
    data = np.array([6,7,8,9,10,11,12]).reshape(-1,1)

    # Calculate variance and standard deviation
    variance, std_dev = calculate_statistics(data)

    print("Dataset:", data.flatten())
    print("Variance:", variance)
    print("Standard Deviation:", std_dev)


if __name__ == "__main__":
    main()