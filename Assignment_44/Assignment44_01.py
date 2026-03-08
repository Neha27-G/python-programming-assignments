
def main():

    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression

    print("Advertising Dataset Machine Learning Application")

    # Step 1: Get Data
    
    data = pd.read_csv("Advertising.csv", index_col=0)

    print("\nFirst 5 Records of Dataset:")
    print(data.head())

    # Step 2: Clean and Prepare Data

    # Input Features
    X = data[['TV', 'radio', 'newspaper']]

    # Output Feature
    Y = data['sales']

    # Step 3: Train Data
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.5, random_state=42
    )

    model = LinearRegression()

    # Train the model
    model.fit(X_train, Y_train)

    # Step 4: Test Data
    predictions = model.predict(X_test)

    # Step 5: Display results
    print("\nExpected Sales vs Predicted Sales\n")

    for i in range(len(predictions)):
        print("Expected:", Y_test.iloc[i], " Predicted:", round(predictions[i], 2))


if __name__ == "__main__":
    main()