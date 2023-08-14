import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('amazon.xlsx')

# Access the data using the correct column names
years = df['year']
states = df['state']
months = df['month']
fires = df['number']

# Group the data by year and calculate the total fires per year
yearly_fires = df.groupby('year')['number'].sum()

# Plot the evolution of fires over the years
plt.plot(yearly_fires.index, yearly_fires.values, marker='o')
plt.xlabel('Year')
plt.ylabel('Number of Fires')
plt.title('Evolution of Forest Fires Over the Years')
plt.grid(True)
plt.show()
