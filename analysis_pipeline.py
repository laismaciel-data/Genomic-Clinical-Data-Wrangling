import pandas as pd
import numpy as np

# 1. SIMULATING DATA
raw_data = {
    'Patient_ID': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'Gene_Mutation': ['BRCA1', 'TP53', 'EGFR', 'None', 'BRCA2'],
    'Read_Quality': [98, 45, 88, np.nan, 32],
    'Status': [' Completed ', 'pending', 'COMPLETED', 'ERROR', ' complete ']
}

df = pd.DataFrame(raw_data)

# 2. CLEANING
df['Status'] = df['Status'].str.strip().str.upper()
mean_val = df['Read_Quality'].mean()
df['Read_Quality'] = df['Read_Quality'].fillna(mean_val)

# 3. FILTERING
filtered_df = df[(df['Read_Quality'] > 50) & (df['Status'] == 'COMPLETED')]

# 4. RESULTS
print("--- Processed Genomic Data ---")
print(filtered_df)
print("\nSuccess: Pipeline executed.")
