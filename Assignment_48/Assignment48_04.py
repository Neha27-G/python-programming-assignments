import numpy as np
from sklearn.preprocessing import StandardScaler

def main():

    # Define points
    point1 = np.array([25, 20000])
    point2 = np.array([30, 40000])

    # Calculate distance before scaling
    distance_before = np.linalg.norm(point1 - point2)

    # Dataset for scaling
    data = np.array([
        [25, 20000],
        [30, 40000]
    ])

    # Apply StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Calculate distance after scaling
    distance_after = np.linalg.norm(scaled_data[0] - scaled_data[1])

    # Print results
    print("Distance before scaling:", distance_before)
    print("Distance after scaling:", distance_after)


if __name__ == "__main__":
    main()