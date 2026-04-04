import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


border = "-" * 50

#-------------------------------------------------------------------------------------
# Step 1: Load both datasets
#=====================================================================================

print(border)
print("Step 1: Load Datasets")
print(border)

fake_df = pd.read_csv("Fake.csv")
true_df = pd.read_csv("True.csv")

print("Fake shape :", fake_df.shape)
print("True shape :", true_df.shape)

#-------------------------------------------------------------------------------------
# Step 2: Add label column
#=====================================================================================

print(border)
print("Step 2: Add Labels")
print(border)

fake_df["label"] = 0
true_df["label"] = 1

print("Labels added successfully")

#-------------------------------------------------------------------------------------
# Step 3: Combine datasets
#=====================================================================================

print(border)
print("Step 3: Combine Data")
print(border)

df = pd.concat([fake_df, true_df], ignore_index=True)

print("Combined dataset shape :", df.shape)

#-------------------------------------------------------------------------------------
# Step 4: Data preprocessing
#=====================================================================================

print(border)
print("Step 4: Data Preprocessing")
print(border)

df = df.dropna()

# Combine title + text (better accuracy)
df["content"] = df["title"] + " " + df["text"]

X = df["content"]
Y = df["label"]

print("Data cleaned and prepared")

#-------------------------------------------------------------------------------------
# Step 5: Feature Extraction (TF-IDF)
#=====================================================================================

print(border)
print("Step 5: TF-IDF Vectorization")
print(border)

vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(X)

print("Text converted to numerical features")

#-------------------------------------------------------------------------------------
# Step 6: Train-Test Split
#=====================================================================================

print(border)
print("Step 6: Train-Test Split")
print(border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("Data split successfully")

#-------------------------------------------------------------------------------------
# Step 7: Create Models
#=====================================================================================

print(border)
print("Step 7: Model Creation")
print(border)

lr = LogisticRegression()
dt = DecisionTreeClassifier()

# Hard Voting
hard_vote = VotingClassifier(
    estimators=[('lr', lr), ('dt', dt)],
    voting='hard'
)

# Soft Voting
soft_vote = VotingClassifier(
    estimators=[('lr', lr), ('dt', dt)],
    voting='soft'
)

print("Models created")

#-------------------------------------------------------------------------------------
# Step 8: Train Models
#=====================================================================================

print( border)
print("Step 8: Model Training")
print(border)

lr.fit(X_train, Y_train)
dt.fit(X_train, Y_train)
hard_vote.fit(X_train, Y_train)
soft_vote.fit(X_train, Y_train)

print("All models trained")

#-------------------------------------------------------------------------------------
# Step 9: Testing
#=====================================================================================

print( border)
print("Step 9: Model Testing")
print(border)

pred_lr = lr.predict(X_test)
pred_dt = dt.predict(X_test)
pred_hard = hard_vote.predict(X_test)
pred_soft = soft_vote.predict(X_test)

print("Predictions generated")

#-------------------------------------------------------------------------------------
# Step 10: Evaluation
#=====================================================================================

print(border)
print("Step 10: Evaluation")
print(border)

print("\nLogistic Regression Accuracy :", accuracy_score(Y_test, pred_lr))
print(confusion_matrix(Y_test, pred_lr))

print("\nDecision Tree Accuracy :", accuracy_score(Y_test, pred_dt))
print(confusion_matrix(Y_test, pred_dt))

print("\nHard Voting Accuracy :", accuracy_score(Y_test, pred_hard))
print(confusion_matrix(Y_test, pred_hard))

print("\nSoft Voting Accuracy :", accuracy_score(Y_test, pred_soft))
print(confusion_matrix(Y_test, pred_soft))

#-------------------------------------------------------------------------------------
# Step 11: Classification Report
#=====================================================================================

print(border)
print("Step 11: Classification Report")
print(border)

print("\nSoft Voting Report:")
print(classification_report(Y_test, pred_soft))

print("\n" + border)
print("Execution Completed Successfully")
print(border)