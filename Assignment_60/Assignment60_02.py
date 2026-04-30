import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

# Activation functions
sigmoid = 1 / (1 + np.exp(-x))
relu = np.maximum(0, x)
tanh = np.tanh(x)

# Plotting
plt.figure(figsize=(8,5))

plt.plot(x, sigmoid, label="Sigmoid")
plt.plot(x, relu, label="ReLU")
plt.plot(x, tanh, label="Tanh")

plt.title("Activation Functions")
plt.legend()
plt.grid()
plt.show()