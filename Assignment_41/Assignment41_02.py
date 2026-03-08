import math

# Dataset
data = [
    {'point':'A','X':1,'Y':2,'label':'Red'},
    {'point':'B','X':2,'Y':3,'label':'Red'},
    {'point':'C','X':3,'Y':1,'label':'Blue'},
    {'point':'D','X':6,'Y':5,'label':'Blue'}
]

# Euclidean Distance Function
def distance(p1, p2):
    return math.sqrt((p1['X']-p2['X'])**2 + (p1['Y']-p2['Y'])**2)

# KNN Prediction Function
def predict(new_point, k):

    # calculate distance
    for d in data:
        d['dist'] = distance(d, new_point)

    # sort by distance
    sorted_data = sorted(data, key=lambda x: x['dist'])

    # take k neighbors
    neighbors = sorted_data[:k]

    # voting
    votes = {}
    for n in neighbors:
        label = n['label']
        votes[label] = votes.get(label,0)+1

    # predicted class
    prediction = max(votes, key=votes.get)
    return prediction


new_point = {'X':2,'Y':2}

print("Prediction Results")

print("K = 1 ->", predict(new_point,1))
print("K = 3 ->", predict(new_point,3))
print("K = 5 ->", predict(new_point,5))