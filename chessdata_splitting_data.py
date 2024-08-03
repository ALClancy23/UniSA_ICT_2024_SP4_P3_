import pandas as pd
from sklearn.model_selection import train_test_split
import os

# Define the file path
file_path = 'C:\Users\jenni\Desktop\jn\uni\capstone 1\chessdata.csv'  

# Ensure the output directory exists
output_dir = 'C:\Users\jenni\Desktop\jn\uni\capstone 1\output'
os.makedirs(output_dir, exist_ok=True)

# Load dataset
df = pd.read_csv(file_path)

# Split the dataset into training and test sets (70/30)
train_df, test_df = train_test_split(df, test_size=0.3, random_state=42)

# Save the splits to CSV files
train_csv = os.path.join(output_dir, 'train_dataset.csv')
test_csv = os.path.join(output_dir, 'test_dataset.csv')
train_df.to_csv(train_csv, index=False)
test_df.to_csv(test_csv, index=False)

# Display the first few rows of the training and test sets
print("Training Set:")
print(train_df.head())
print("\nTest Set:")
print(test_df.head())
