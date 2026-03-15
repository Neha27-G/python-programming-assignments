import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():

    # Dataset (StudyHours, SleepHours)
    X = np.array([
        [1,7],
        [2,6],
        [3,7],
        [4,6],
        [5,8]
    ])

    # Output (Marks)
    y = np.array([50,55,60,65,70])

    # Split dataset into training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create model
    model = LinearRegression()

    # Train model
    model.fit(X_train, y_train)

    # Print coefficients and intercept
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)

    # Predict marks for StudyHours=6 and SleepHours=7
    prediction = model.predict([[6,7]])
    print("Predicted Marks:", prediction[0])


if __name__ == "__main__":
    main()