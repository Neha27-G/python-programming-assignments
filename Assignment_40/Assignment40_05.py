import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-"*100

    # ================================================================
    # 1. FEATURE IMPORTANCE
    # ================================================================
    print(Border)
    print("1.FEATURE IMPORTANCE ")
    print(Border)


    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    
    #---------------------------------------------------------------------------------------------
    importances = model.feature_importances_

    for feature, importance in zip(X.columns, importances):
        print(feature, ":", importance)

    # Most Important Feature
    print("\nMost Important Feature:",
        X.columns[importances.argmax()])

    # Least Important Feature
    print("Least Important Feature:",
        X.columns[importances.argmin()])
    
    # ================================================================
    # 2.REMOVE SLEEPHOURS & RETRAIN
    # ================================================================
    print(Border)
    print("2.REMOVE SLEEPHOURS & RETRAIN ")
    print(Border)

    X_new = df.drop(["FinalResult", "SleepHours"], axis=1)
    y = df["FinalResult"]

    X_train2, X_test2, y_train2, y_test2 = train_test_split(
        X_new, y, test_size=0.3, random_state=42)

    model2 = DecisionTreeClassifier(random_state=42)
    model2.fit(X_train2, y_train2)

    y_pred2 = model2.predict(X_test2)

    print("New Accuracy:",accuracy_score(y_test2, y_pred2) * 100)

    # ================================================================
    # 3. Train Using Only StudyHours & Attendance
    # ================================================================
    print(Border)
    print("3. Train Using Only StudyHours & Attendance")
    print(Border)

    X_small = df[["StudyHours", "Attendance"]]
    y = df["FinalResult"]

    X_train3, X_test3, y_train3, y_test3 = train_test_split(
        X_small, y, test_size=0.3, random_state=42)

    model3 = DecisionTreeClassifier(random_state=42)
    model3.fit(X_train3, y_train3)

    y_pred3 = model3.predict(X_test3)

    print("Accuracy with 2 features:",
        accuracy_score(y_test3, y_pred3) * 100)
    
    # ================================================================
    # 4.Predict 5 New Students
    # ================================================================
    print(Border)
    print("4.Predict 5 New Students")
    print(Border)

    new_students = pd.DataFrame([
        [5, 80, 70, 6, 7],
        [2, 60, 45, 3, 6],
        [7, 90, 85, 9, 8],
        [4, 75, 50, 5, 6],
        [6, 88, 72, 8, 7]
    ], columns=X.columns)

    predictions = model.predict(new_students)

    new_students["Prediction"] = predictions
    print(new_students)

    # ================================================================
    # 5. Manual Accuracy Calculation
    # ================================================================
    print(Border)
    print("5. Manual Accuracy Calculation")
    print(Border)

    correct = 0

    for actual, predicted in zip(y_test, y_pred):
        if actual == predicted:
            correct += 1

    manual_accuracy = correct / len(y_test)

    print("Manual Accuracy:", manual_accuracy * 100)
    print("Sklearn Accuracy:",accuracy_score(y_test, y_pred) * 100)

if __name__=="__main__":
    main()
