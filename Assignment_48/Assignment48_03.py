import numpy as np
from sklearn.preprocessing import StandardScaler

def scale_features(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data

def main():
    # Dataset
    data = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
    ])

    # Feature scaling
    scaled_data = scale_features(data)

    print("Original Dataset:")
    print(data)

    print("\nScaled Dataset:")
    print(scaled_data)

if __name__ == "__main__":
    main()