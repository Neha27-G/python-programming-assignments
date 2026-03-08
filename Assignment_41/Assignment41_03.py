import math

def EuclideanDistance(p1, p2):
    return math.sqrt((p1['hours'] - p2['hours'])**2 + (p1['attendance'] - p2['attendance'])**2)


def StudentResultKNN():

    border = "-"*50

    data = [
        {'hours':2, 'attendance':60, 'result':'Fail'},
        {'hours':5, 'attendance':80, 'result':'Pass'},
        {'hours':6, 'attendance':85, 'result':'Pass'},
        {'hours':1, 'attendance':50, 'result':'Fail'}
    ]

    print(border)
    print("Student Result Prediction using KNN")
    print(border)

    # User Input
    hours = int(input("Enter Study Hours: "))
    attendance = int(input("Enter Attendance: "))

    new_point = {'hours':hours, 'attendance':attendance}

    # Calculate distance
    for d in data:
        d['distance'] = EuclideanDistance(d, new_point)

    # Sort by distance
    sorted_data = sorted(data, key=lambda x: x['distance'])

    # Select K nearest neighbors
    k = 3
    nearest = sorted_data[:k]

    # Voting
    votes = {}

    for n in nearest:
        label = n['result']
        votes[label] = votes.get(label,0) + 1

    predicted = max(votes, key=votes.get)

    print(border)
    print("Predicted Result:", predicted)
    print(border)


def main():
    StudentResultKNN()


if __name__ == "__main__":
    main()