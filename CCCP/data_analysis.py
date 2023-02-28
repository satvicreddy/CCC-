import pandas as pd
# Create a data frame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
# Filter the data frame by age
filtered_df = df[df['Age'] > 30]
# Print the filtered data frame
print(filtered_df)
