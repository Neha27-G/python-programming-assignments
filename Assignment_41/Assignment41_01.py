import math

def EucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans


def MarvellousKNeighborsClassifier():

    border = "-"*50

    data = [
        {'point':'A', 'X':1, 'Y':2, 'label':'Red'},
        {'point':'B', 'X':2, 'Y':3, 'label':'Red'},
        {'point':'C', 'X':3, 'Y':1, 'label':'Blue'},
        {'point':'D', 'X':6, 'Y':5, 'label':'Blue'}
    ]

    print(border)
    print("User Defined KNN")
    print(border)

    print("Training Dataset")
    for i in data:
        print(i)

    print(border)

    # User input
    x = int(input("Enter X coordinate: "))
    y = int(input("Enter Y coordinate: "))

    new_point = {'X':x, 'Y':y}

    # Calculate distance
    for d in data:
        d['distance'] = EucDistance(d, new_point)

    print(border)
    print("Calculated Distances")
    print(border)

    for d in data:
        print(d['point'], "Distance:", round(d['distance'],2))

    # Sort distances
    sorted_data = sorted(data, key=lambda item: item['distance'])

    # Select K nearest neighbors
    k = 3
    nearest = sorted_data[:k]

    print(border)
    print("Nearest Neighbors")
    print(border)

    for d in nearest:
        print(d['point'], "Distance:", round(d['distance'],2))

    # Voting
    votes = {}
    for neighbor in nearest:
        label = neighbor['label']
        votes[label] = votes.get(label,0) + 1

    predicted_class = max(votes, key=votes.get)

    print(border)
    print("Predicted Class:", predicted_class)
    print(border)


def main():
    MarvellousKNeighborsClassifier()


if __name__ == "__main__":
    main()