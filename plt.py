import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('path_to_your_csv_file.csv')

# Bar chart
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
df['column_name'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Bar Chart')

# Histogram
plt.subplot(2, 2, 2)
df['column_name'].plot(kind='hist', bins=30, color='green', edgecolor='black')
plt.title('Histogram')

# Scatter plot
plt.subplot(2, 2, 3)
plt.scatter(df['x_column'], df['y_column'], color='red')
plt.title('Scatter Plot')

# Box plot
plt.subplot(2, 2, 4)
df.boxplot(column='column_name')
plt.title('Box Plot')

plt.tight_layout()
plt.show()
