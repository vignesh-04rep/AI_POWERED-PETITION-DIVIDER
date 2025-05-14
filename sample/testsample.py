import pandas as pd

# Load the two CSV files
file1 = pd.read_csv('combined_file.csv')
file2 = pd.read_csv('petitions_dataset.csv')

# Concatenate the two dataframes vertically (you can also merge them horizontally if needed)
combined = pd.concat([file1, file2], ignore_index=True)

# Save the combined file into a new CSV file
combined.to_csv('combined_file.csv', index=False)

print("CSV files merged and saved as 'combined_file.csv'")