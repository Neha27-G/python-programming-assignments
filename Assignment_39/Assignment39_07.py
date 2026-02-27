import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def main():

    Border="-"*100
    print(Border)
    
    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Features and Target
    X = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    # Create Model
    model = DecisionTreeClassifier()

    # Train Model
    model.fit(X_train, y_train)

    print("Model trained successfully.\n")

    print(Border)
#-----------------------------------------------------------------
    print("Train model to predict result")
    y_pred = model.predict(X_test)

    print("Predicted Values:", y_pred[:10])
    print("Actual Values   :", y_test.values[:10])

    print(Border)

#---------------------------------------------------------------------------
    print("Model Accuracy \n")
    accuracy = accuracy_score(y_test, y_pred)

    print("Model Accuracy: {:.2f}%".format(accuracy * 100))

    print(Border)

#--------------------------------------------------------------------------
    print("Confusion Matrix \n")
    cm = confusion_matrix(y_test, y_pred)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.show()

    print("""
    True Positive (TP): Predicted Pass & Actually Pass
    True Negative (TN): Predicted Fail & Actually Fail
    False Positive (FP): Predicted Pass but Actually Fail
    False Negative (FN): Predicted Fail but Actually Pass
    """)

    print(Border)
#--------------------------------------------------------------------------------------
    print("Training accuracy vs Testing accuracy")

    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, y_pred)

    print("Training Accuracy: {:.2f}%".format(train_acc * 100))
    print("Testing Accuracy : {:.2f}%".format(test_acc * 100))

    if train_acc > test_acc:
        print("Model may be Overfitting.")
    elif train_acc < test_acc:
        print("Model may be Underfitting.")
    else:
        print("Model is well balanced.")

    print(Border)

#---------------------------------------------------------------------------------------------

    print("Train three Decision Tree model ")

    depths = [1, 3, None]

    for depth in depths:
        temp_model = DecisionTreeClassifier(max_depth=depth, random_state=42)
        temp_model.fit(X_train, y_train)
        temp_pred = temp_model.predict(X_test)
        acc = accuracy_score(y_test, temp_pred)

        print("Testing Accuracy (max_depth={}): {:.2f}%".format(depth, acc * 100))
    
    print(Border)

#-----------------------------------------------------------------------------------

    print("Predict new student data\n")

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

    print(Border)

#-------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()



