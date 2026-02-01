# Starter Code: Claude Sonnet Python Exercise

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.csv')

# Show first rows
print(df.head())

# Calculate statistics
print(df.describe())

# Make a plot
df['column_name'].hist()
plt.show()
