import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def CheckAccuracy(X,Y):

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=1)

    print("\nAccuracy for different K values\n")

    for k in range(1,6):

        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train,Y_train)

        Y_pred = model.predict(X_test)

        acc = accuracy_score(Y_test,Y_pred)

        print("K =",k,"Accuracy =",round(acc*100,2),"%")


def main():

    # Step 1 : Load Dataset
    data = pd.read_csv("PlayPredictor.csv")

    # Remove index column
    data = data.drop(data.columns[0], axis=1)

    print("Dataset\n")
    print(data)

    # Step 2 : Label Encoding
    le_w = LabelEncoder()
    le_t = LabelEncoder()
    le_p = LabelEncoder()

    data['Whether'] = le_w.fit_transform(data['Whether'])
    data['Temperature'] = le_t.fit_transform(data['Temperature'])
    data['Play'] = le_p.fit_transform(data['Play'])

    X = data[['Whether','Temperature']]
    Y = data['Play']

    # Step 3 : Train Model
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X,Y)

    # Step 4 : Test Data
    # Test Data
    w = input("Enter Whether (Sunny/Overcast/Rainy): ")
    t = input("Enter Temperature (Hot/Mild/Cool): ")

    w_val = le_w.transform([w])[0]
    t_val = le_t.transform([t])[0]

    test_df = pd.DataFrame([[w_val, t_val]], columns=['Whether','Temperature'])

    prediction = model.predict(test_df)

    result = le_p.inverse_transform(prediction)

    print("Prediction:", result[0])

    # Step 5 : Accuracy
    CheckAccuracy(X,Y)


if __name__ == "__main__":
    main()