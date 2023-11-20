import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the dataset
data = pd.read_csv("/Users/abhudaysingh/Downloads/linear_regression_dataset.csv")

# Extract features and target variable
y = data['TOTCHG']
x1 = data['AGE']
x2 = data['FEMALE']
x3 = data['LOS']
x4 = data['RACE']
x5 = data['APRDRG']

# Normalization function
def normalization(feature_values):
    min_value = min(feature_values)
    max_value = max(feature_values)
    if min_value == max_value:
        normalized_values = [0.0 for _ in feature_values]
    else:
        normalized_values = [(x - min_value) / (max_value - min_value) for x in feature_values]

    return normalized_values

# Normalize features
x1 = normalization(x1)
x2 = normalization(x2)
x3 = normalization(x3)
x4 = normalization(x4)
x5 = normalization(x5)
#y = normalization(y)

# Gradient Descent function
def gradient_descent(x, y, m, c, learning_rate, num_iterations):
    n = len(y)  # Number of data points

    for i in range(num_iterations):
        # Initialize partial derivatives with respect to m and c
        dm = 0
        dc = 0

        for j in range(n):
            # Calculate the predicted value
            y_pred = m * x[j] + c

            # Update the partial derivatives
            dm += (2 / n) * x[j] * (y_pred - y[j])
            dc += (2 / n) * (y_pred - y[j])

        # Update m and c using the learning rate
        m -= learning_rate * dm
        c -= learning_rate * dc

        mse = 0
        for j in range(n):
            mse += (1 / n) * (y[j] - (m * x[j] + c)) ** 2
    return m, c

# Initial guesses and hyperparameters
initial_m = 0.0  # Initial guess for the slopes, assuming 5 features
initial_c = 0.0  # Initial guess for the intercept
learning_rate = 0.05
num_iterations = 500

m1, c = gradient_descent(x1, y, initial_m, initial_c, learning_rate, num_iterations)
m2, c = gradient_descent(x2, y, initial_m, initial_c, learning_rate, num_iterations)
m3, c = gradient_descent(x3, y, initial_m, initial_c, learning_rate, num_iterations)
m4, c = gradient_descent(x4, y, initial_m, initial_c, learning_rate, num_iterations)
m5, c = gradient_descent(x5, y, initial_m, initial_c, learning_rate, num_iterations)
# Convert lists to NumPy arrays
#print(x4)
x1 = np.array(x1)
x2 = np.array(x2)
x3 = np.array(x3)
x4 = np.array(x4)
x5 = np.array(x5)
#print(m1*x1)
a = m1*x1 + m2*x2 + m3*x3 + m5*x5 + c
#print(a) this is working
# Scatter plot
plt.scatter(data.TOTCHG, a, color="black")

# Plot the regression line
plt.plot( a,a, color="red")

# Display the plot
plt.show()
