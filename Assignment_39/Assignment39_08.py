# ================================================================
# STUDENT PERFORMANCE PREDICTION USING DECISION TREE
# ================================================================

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

def main():

    Border = "-"*100

    # ================================================================
    # 1. LOAD DATASET
    # ================================================================
    print(Border)
    print("1. Loading Dataset")
    print(Border)

    df = pd.read_csv("student_performance_ml.csv")
    print(df.head())

    # ================================================================
    # 2. BASIC DATA ANALYSIS
    # ================================================================
    print(Border)
    print("2. Basic Analysis")
    print(Border)

    print("Total Students:", len(df))
    print("Passed Students:", df[df["FinalResult"]==1].shape[0])
    print("Failed Students:", df[df["FinalResult"]==0].shape[0])

    print("\nAverage Study Hours:", df["StudyHours"].mean())
    print("Average Attendance:", df["Attendance"].mean())

    # ================================================================
    # 3. VISUALIZATION
    # ================================================================
    print(Border)
    print("3. Visualization")
    print(Border)

    # Histogram
    plt.figure()
    plt.hist(df["StudyHours"], bins=10)
    plt.title("Histogram of Study Hours")
    plt.xlabel("StudyHours")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter Plot
    plt.figure()
    plt.scatter(df[df["FinalResult"]==1]["StudyHours"],
                df[df["FinalResult"]==1]["FinalResult"],
                color="green", label="Pass")

    plt.scatter(df[df["FinalResult"]==0]["StudyHours"],
                df[df["FinalResult"]==0]["FinalResult"],
                color="red", label="Fail")

    plt.title("StudyHours vs FinalResult")
    plt.xlabel("StudyHours")
    plt.ylabel("FinalResult")
    plt.legend()
    plt.show()

    # ================================================================
    # 4. TRAIN-TEST SPLIT
    # ================================================================
    print(Border)
    print("4. Train-Test Split")
    print(Border)

    X = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    print("Training Size:", len(X_train))
    print("Testing Size:", len(X_test))

    # ================================================================
    # 5. MODEL TRAINING
    # ================================================================
    print(Border)
    print("5. Decision Tree Model Training")
    print(Border)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # ================================================================
    # 6. PREDICTION
    # ================================================================
    y_pred = model.predict(X_test)

    print("\nPredicted Values:", y_pred[:10])
    print("Actual Values   :", y_test.values[:10])

    # ================================================================
    # 7. ACCURACY CALCULATION
    # ================================================================
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, y_pred)

    print("\nTraining Accuracy: {:.2f}%".format(train_acc*100))
    print("Testing Accuracy : {:.2f}%".format(test_acc*100))

    # ================================================================
    # 8. CONFUSION MATRIX
    # ================================================================
    print(Border)
    print("Confusion Matrix")
    print(Border)

    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.show()

    print("""
    True Positive (TP): Model predicted Pass and student actually Passed.
    True Negative (TN): Model predicted Fail and student actually Failed.
    False Positive (FP): Model predicted Pass but student Failed.
    False Negative (FN): Model predicted Fail but student Passed.
    """)

    # ================================================================
    # 9. OVERFITTING CHECK
    # ================================================================
    print(Border)
    print("Overfitting / Underfitting Check")
    print(Border)

    if train_acc > test_acc:
        print("Model may be slightly overfitting.")
    elif train_acc < test_acc:
        print("Model may be underfitting.")
    else:
        print("Model is well balanced.")

    # ================================================================
    # 10. DEPTH COMPARISON
    # ================================================================
    print(Border)
    print("Depth Comparison")
    print(Border)

    depths = [1, 3, None]

    for depth in depths:
        temp_model = DecisionTreeClassifier(max_depth=depth, random_state=42)
        temp_model.fit(X_train, y_train)
        temp_pred = temp_model.predict(X_test)
        acc = accuracy_score(y_test, temp_pred)
        print("Testing Accuracy (max_depth={}): {:.2f}%".format(depth, acc*100))

    print("\nObservation:")
    print("Low depth may underfit.")
    print("Very high depth may overfit.")
    print("Moderate depth often gives balanced performance.")

    # ================================================================
    # 11. NEW STUDENT PREDICTION
    # ================================================================
    print(Border)
    print("New Student Prediction")
    print(Border)

    new_student = pd.DataFrame([[6, 85, 66, 7, 7]],
                            columns=["StudyHours",
                                    "Attendance",
                                    "PreviousScore",
                                    "AssignmentsCompleted",
                                    "SleepHours"])

    result = model.predict(new_student)

    if result[0] == 1:
        print("Prediction: Student will PASS")
    else:
        print("Prediction: Student will FAIL")

    # ================================================================
    # 12. FINAL CONCLUSION
    # ================================================================
    print(Border)
    print("Final Conclusion")
    print(Border)

    print("""
    Study hours, attendance, assignments, and previous score
    significantly influence final results.

    Decision Tree model can effectively predict student performance.
    Proper depth selection is important to avoid overfitting.
    """)

# ================================================================
# MAIN FUNCTION CALL
# ================================================================
if __name__ == "__main__":
    main()