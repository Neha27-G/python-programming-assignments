import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

border = "-" * 50

#-------------------------------------------------------------------------------------
# Step 1: Load dataset
#=====================================================================================

print(border)
print("Step 1: Load Dataset")
print(border)

df = pd.read_csv("bank-full.csv" , sep=";")
print("Shape of dataset :", df.shape)
print("First 5 records :\n", df.head())

#-------------------------------------------------------------------------------------
# Step 2: Handle missing / unknown values
#=====================================================================================

print( border)
print("Step 2: Data Cleaning")
print(border)

df.replace("unknown", pd.NA, inplace=True)
df=df.fillna("missing")

print("Missing values handled successfully")

#-------------------------------------------------------------------------------------
# Step 3: Encode categorical variables
#=====================================================================================

print(border)
print("Step 3: Encoding")
print(border)

le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype(str) 
        df[col] = le.fit_transform(df[col])

print("Categorical data encoded successfully")

#-------------------------------------------------------------------------------------
# Step 4: Separate features and label
#=====================================================================================

print(border)
print("Step 4: Feature & Target Split")
print(border)

X = df.drop("y", axis=1)
Y = df["y"]

print("Features and target separated")

#-------------------------------------------------------------------------------------
# Step 5: Feature Scaling
#=====================================================================================

print(border)
print("Step 5: Feature Scaling")
print(border)

scaler = StandardScaler()
X = scaler.fit_transform(X)

print("Feature scaling applied")

#-------------------------------------------------------------------------------------
# Step 6: Split dataset
#=====================================================================================

print(border)
print("Step 6: Train-Test Split")
print(border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("Training and testing data created")

#-------------------------------------------------------------------------------------
# Step 7: Create models
#=====================================================================================

print(border)
print("Step 7: Model Creation")
print(border)

model1 = LogisticRegression()
model2 = KNeighborsClassifier(n_neighbors=5)
model3 = RandomForestClassifier(n_estimators=10, random_state=42)

print("Models created successfully")

#-------------------------------------------------------------------------------------
# Step 8: Train models
#=====================================================================================

print( border)
print("Step 8: Model Training")
print(border)

model1.fit(X_train, Y_train)
model2.fit(X_train, Y_train)
model3.fit(X_train, Y_train)

print("Models trained successfully")

#-------------------------------------------------------------------------------------
# Step 9: Test models
#=====================================================================================

print(border)
print("Step 9: Model Testing")
print(border)

Y_pred1 = model1.predict(X_test)
Y_pred2 = model2.predict(X_test)
Y_pred3 = model3.predict(X_test)

print("Predictions generated")

#-------------------------------------------------------------------------------------
# Step 10: Evaluate models
#=====================================================================================

print(border)
print("Step 10: Model Evaluation")
print(border)

print("\nLogistic Regression Accuracy :", accuracy_score(Y_test, Y_pred1))
print(confusion_matrix(Y_test, Y_pred1))
print("ROC-AUC :", roc_auc_score(Y_test, Y_pred1))

print("\nKNN Accuracy :", accuracy_score(Y_test, Y_pred2))
print(confusion_matrix(Y_test, Y_pred2))
print("ROC-AUC :", roc_auc_score(Y_test, Y_pred2))

print("\nRandom Forest Accuracy :", accuracy_score(Y_test, Y_pred3))
print(confusion_matrix(Y_test, Y_pred3))
print("ROC-AUC :", roc_auc_score(Y_test, Y_pred3))

#-------------------------------------------------------------------------------------
# Step 11: Classification Report
#=====================================================================================

print(border)
print("Step 11: Classification Report")
print(border)

print("\nClassification Report (Random Forest):")
print(classification_report(Y_test, Y_pred3))

print("\n" + border)
print("Execution Completed Successfully")
print(border)