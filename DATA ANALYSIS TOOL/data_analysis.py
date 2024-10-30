import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

print(f'data overview\n {data}')

mean_age = np.mean(data['Age'])
mdn_salary = np.median(data['Salary'])
stdev_salary = np.std(data['Salary'])

print(f"\nMean Age: {mean_age}")
print(f"Median Salary: {mdn_salary}")
print(f"Standard Deviation of Salary: {stdev_salary}")

plt.figure(figsize=(10, 5))

# Age Distribution
plt.subplot(1, 2, 1)
plt.hist(data['Age'], bins=5, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Salary Distribution
plt.subplot(1, 2, 2)
plt.hist(data['Salary'], bins=5, color='lightgreen', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')

# Show plots
plt.tight_layout()
plt.show()
