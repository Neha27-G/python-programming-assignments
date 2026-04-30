import math

# Inputs
x1 = 2
x2 = 3

# Weights and bias
w1 = 0.4
w2 = 0.6
bias = 0.5

# 1. Weighted sum
weighted_sum = (x1 * w1) + (x2 * w2) + bias
print("Weighted Sum:", weighted_sum)

# 2. Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

output = sigmoid(weighted_sum)

# 3. Final output
print("Final Output (Sigmoid):", output)

# 4. Interpretation
if output > 0.5:
    print("Output is close to 1 (High activation)")
else:
    print("Output is close to 0 (Low activation)")