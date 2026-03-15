import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():

    # Dataset
    X = np.array([1,2,3,4,5]).reshape(-1,1)
    y = np.array([50,55,60,65,70])

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create model
    model = LinearRegression()

    # Train model
    model.fit(X_train, y_train)

    # Print coefficient and intercept
    print("Coefficient:", model.coef_[0])
    print("Intercept:", model.intercept_)

    # Predict marks for 6 study hours
    prediction = model.predict([[6]])
    print("Predicted Marks:", prediction[0])


if __name__ == "__main__":
    main()