import pandas as pd

df = pd.read_excel('amazon.xlsx')
print(df.head())

fires_by_state = df.groupby('state')['number'].sum()
print(fires_by_state)

# Calculate the average number of forest fires per year
average_fires_per_year = df['number'].mean()
print(f"Average number of forest fires per year:{average_fires_per_year}")

# Calculate the maximum & minimum number of forest fires in states
max_state = fires_by_state.idxmax()
max_value = fires_by_state[max_state]

min_state = fires_by_state.idxmin()
min_value = fires_by_state[min_state]

# Display the state with the maximum & minimum number of forest fires and its value
print(f"State with the maximum number of forest fires: {max_state}")
print(f"Number of forest fires in {max_state} is {max_value}")

print(f"State with the minimum number of forest fires: {min_state}")
print(f"Number of forest fires in {min_state} is {min_value}")