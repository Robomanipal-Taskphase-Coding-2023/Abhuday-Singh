import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\Users\\aadu7\\OneDrive\\linear_regression_dataset_new.csv")
#print(data)
y =  data['TOTCHG']
x1 = (data['AGE'])
x2 = (data['FEMALE'])
x3 = (data['LOS'])
x4 = (data['RACE'])
x5 = (data['APRDRG'])
#print(x1*x2)
#print(x1)
def normalisation(feature_values):
    min_value = min(feature_values)
    max_value = max(feature_values)
    if min_value == max_value:
        # Handle the case when all values are the same to avoid division by zero
        normalized_values = [0.0 for _ in feature_values]
    else:
        normalized_values = [(x - min_value) / (max_value - min_value) for x in feature_values]

    return normalized_values

x1 = normalisation(x1)
x2 = normalisation(x2)
x3 = normalisation(x3)
x4 = normalisation(x4)
x5 = normalisation(x5)
#print(x1)
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
initial_m = 0  # Initial guess for the slope
initial_c = 0  # Initial guess for the intercept
learning_rate = 0.01
num_iterations = 500
m1, c = gradient_descent(x1, y, initial_m, initial_c, learning_rate, num_iterations)
m2, c = gradient_descent(x2, y, initial_m, initial_c, learning_rate, num_iterations)
m3, c = gradient_descent(x3, y, initial_m, initial_c, learning_rate, num_iterations)
m4, c = gradient_descent(x4, y, initial_m, initial_c, learning_rate, num_iterations)
m5, c = gradient_descent(x5, y, initial_m, initial_c, learning_rate, num_iterations)
#print(m2)
m1 = float(m1)
m2 = float(m2)
m3 = float(m3)
m4 = float(m4)
m5 = float(m5)

#print(np.dot(m1,x1))
#data.AGE*data.LOS*data.RACE*data.APRDRG*data.FEMALE
o = np.dot(m1,x1) + np.dot(m2,x2) + np.dot(m3,x3) +np.dot(m4,x4) + np.dot(m5,x5)
print(o)
#plt.scatter(data.TOTCHG, data.AGE*data.LOS*data.RACE*data.APRDRG*data.FEMALE , color = "black")
plt.scatter(data.TOTCHG, data.AGE*data.LOS*data.RACE*data.APRDRG*data.FEMALE, color = "black")
plt.plot(list(range(0, 500)), [ m1*x1[i] + m2*x2[i] + m3*x3[i] + m4*x4[i] + m5*x5[i] + c for i in range(0, 500)], color="red")
#plt.plot(list(range(0,500)), [ m1*x1[x] + m2*x2[x] + m3*x3[x] + m4*x4[x] + m5*x5[x] + c for x in range(0,500)], color="red")
plt.show()
#final_m, final_c = gradient_descent(x, y, initial_m, initial_c, learning_rate, num_iterations)
