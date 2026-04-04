import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#-------------------------------------------------------------------------------------
# Step 1: Load the dataset
#=====================================================================================

df = pd.read_csv("diabetes.csv")
print("Shape of dataset :", df.shape)
print("First 5 records :\n", df.head())

#-------------------------------------------------------------------------------------
# Step 2: Data preprocessing (handle zero values)
#=====================================================================================

cols = ["Glucose","BloodPressure","SkinThickness","Insulin","BMI"]

for col in cols:
    df[col] = df[col].replace(0, np.nan)
    df[col] = df[col].fillna(df[col].median())

#-------------------------------------------------------------------------------------
# Step 3: Separate features and label
#=====================================================================================

X = df.drop("Outcome", axis=1)
Y = df["Outcome"]

#-------------------------------------------------------------------------------------
# Step 4: Feature Scaling
#=====================================================================================

scaler = StandardScaler()
X = scaler.fit_transform(X)

#-------------------------------------------------------------------------------------
# Step 5: Split dataset into training and testing
#=====================================================================================

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

#-------------------------------------------------------------------------------------
# Step 6: Create Models
#=====================================================================================

model1 = LogisticRegression()
model2 = KNeighborsClassifier(n_neighbors=5)
model3 = DecisionTreeClassifier(random_state=42)

#-------------------------------------------------------------------------------------
# Step 7: Train Models
#=====================================================================================

model1.fit(X_train, Y_train)
model2.fit(X_train, Y_train)
model3.fit(X_train, Y_train)

#-------------------------------------------------------------------------------------
# Step 8: Test Models
#=====================================================================================

Y_pred1 = model1.predict(X_test)
Y_pred2 = model2.predict(X_test)
Y_pred3 = model3.predict(X_test)

#-------------------------------------------------------------------------------------
# Step 9: Evaluate Models
#=====================================================================================

print("\nLogistic Regression Accuracy :", accuracy_score(Y_test, Y_pred1))
print(confusion_matrix(Y_test, Y_pred1))

print("\nKNN Accuracy :", accuracy_score(Y_test, Y_pred2))
print(confusion_matrix(Y_test, Y_pred2))

print("\nDecision Tree Accuracy :", accuracy_score(Y_test, Y_pred3))
print(confusion_matrix(Y_test, Y_pred3))

#-------------------------------------------------------------------------------------
# Step 10: Classification Report (Best Model Example)
#=====================================================================================

print("\nClassification Report (Decision Tree):")
print(classification_report(Y_test, Y_pred3))

#-------------------------------------------------------------------------------------
# Step 11: Save Predictions
#=====================================================================================

output = pd.DataFrame({
    "Actual": Y_test,
    "Predicted": Y_pred3
})

output.to_csv("diabetes_predictions.csv", index=False)

print("\nPredictions saved successfully")