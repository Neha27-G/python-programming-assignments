import numpy as np
from sklearn.preprocessing import StandardScaler

def main():

    # Dataset
    data = np.array([[6], [7], [8], [9], [10], [11], [12]])

    # Create scaler object
    scaler = StandardScaler()

    # Fit scaler to data
    scaler.fit(data)

    # Mean of dataset
    mean_value = scaler.mean_[0]

    print("Dataset:", data.flatten())
    print("Mean:", mean_value)


if __name__ == "__main__":
    main()