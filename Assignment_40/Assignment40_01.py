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

if __name__=="__main__":
    main()
