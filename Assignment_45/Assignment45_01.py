def main():

    # Necessary Imports
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score

    print("Wine Classification Machine Learning Application")

    # Step 1: Get Data
    data = pd.read_csv("WinePredictor.csv")

    print("\nFirst 5 Records of Dataset:")
    print(data.head())

    # Step 2: Clean, Prepare and Manipulate Data

    # Features (all columns except Class)
    X = data.drop("Class", axis=1)

    # Target variable
    Y = data["Class"]

    # Step 3: Train Data
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.3, random_state=42
    )

    # KNN model with K = 3
    model = KNeighborsClassifier(n_neighbors=3)

    # Train model
    model.fit(X_train, Y_train)

    # Step 4: Test Data
    predictions = model.predict(X_test)

    print("\nPredicted Classes:")
    print(predictions)

    print("\nActual Classes:")
    print(Y_test.values)

    # Step 5: Calculate Accuracy
    accuracy = accuracy_score(Y_test, predictions)

    print("\nAccuracy of Model:", round(accuracy * 100, 2), "%")


if __name__ == "__main__":
    main()