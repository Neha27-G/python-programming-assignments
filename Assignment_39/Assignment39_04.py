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

if __name__=="__main__":
    main()



