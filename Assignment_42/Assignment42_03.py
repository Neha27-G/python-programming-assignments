import numpy as np
import matplotlib.pyplot as plt

# Dataset
X = np.array([1,2,3,4,5])
Y = np.array([20000,25000,30000,35000,40000])

# Mean
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Slope
num = np.sum((X-mean_x)*(Y-mean_y))
den = np.sum((X-mean_x)**2)

m = num/den

# Intercept
c = mean_y - m*mean_x

print("Slope:",m)
print("Intercept:",c)

# Predict salary for 6 years
x_new = 6
y_pred = m*x_new + c

print("Predicted Salary for 6 Years Experience:",y_pred)

# Plot graph
plt.scatter(X,Y,label="Data Points")
plt.plot(X,m*X+c,color='red',label="Regression Line")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.legend()
plt.show()


# ---------------------------------------------------------
# THEORY QUESTIONS
# ---------------------------------------------------------

# 4. Why is KNN called a lazy learner?
# KNN is called a lazy learner because it does not build a model during
# the training phase. It simply stores the training data and performs
# computations only when a new prediction is required.

# 5. What happens if K is too small?
# If K is very small (e.g., K = 1), the model becomes sensitive to noise
# in the dataset and may overfit the data.

# 6. What happens if K is too large?
# If K is very large, many distant points influence the prediction,
# which may lead to underfitting and less accurate results.

# 7. Why does linear regression minimize squared error?
# Linear regression minimizes squared error because squaring removes
# negative signs and penalizes larger errors more strongly. It also
# allows easier mathematical optimization.

# 8. What is the difference between MSE and R²?
# MSE (Mean Squared Error) measures the average squared difference
# between actual and predicted values. Lower MSE means better accuracy.
# R² (R-squared) measures how well the regression model explains
# the variance in the data. Higher R² means a better model.

# 9. Why R² cannot be greater than 1?
# R² cannot be greater than 1 because it represents the proportion
# of variance explained by the model, which cannot exceed 100%.

# 10. Can KNN be used for regression?
# Yes, KNN can be used for regression by taking the average value
# of the K nearest neighbors instead of majority voting.
