import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


border = "-" * 50

#-------------------------------------------------------------------------------------
# Step 1: Load dataset
#=====================================================================================

print(border)
print("Step 1: Load Dataset")
print(border)

df = pd.read_csv("student-mat.csv", sep=";")

print("Shape :", df.shape)
print(df.head())

#-------------------------------------------------------------------------------------
# Step 2: Select required features
#=====================================================================================

print(border)
print("Step 2: Feature Selection")
print(border)

features = ["G1", "G2", "G3", "studytime", "failures", "absences"]

df = df[features]

print("Selected Features:")
print(df.head())

#-------------------------------------------------------------------------------------
# Step 3: Feature Scaling
#=====================================================================================

print(border)
print("Step 3: Feature Scaling")
print(border)

scaler = StandardScaler()
X = scaler.fit_transform(df)

print("Scaling applied")

#-------------------------------------------------------------------------------------
# Step 4: Apply K-Means Clustering
#=====================================================================================

print(border)
print("Step 4: K-Means Clustering")
print(border)

kmeans = KMeans(n_clusters=3, random_state=42)

df["Cluster"] = kmeans.fit_predict(X)

print("Clustering completed")

#-------------------------------------------------------------------------------------
# Step 5: Analyze clusters
#=====================================================================================

print(border)
print("Step 5: Cluster Analysis")
print(border)

print(df.groupby("Cluster").mean())

#-------------------------------------------------------------------------------------
# Step 6: Display cluster counts
#=====================================================================================

print(border)
print("Step 6: Cluster Distribution")
print(border)

print(df["Cluster"].value_counts())

#-------------------------------------------------------------------------------------
# Step 7: Cluster Interpretation
#=====================================================================================

print(border)
print("Step 7: Cluster Interpretation")
print(border)

print("Cluster 0 → Top Performers")
print("Cluster 1 → Average Students")
print("Cluster 2 → Struggling Students")

print(border)
print("Execution Completed Successfully")
print(border)