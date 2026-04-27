import pandas as pd

# 1. Simulating a raw/messy genomic dataset
# This represents data that might come from a hospital database
raw_data = {
    'Patient_Name': ['Lais', 'Anderson', 'John', 'Mary'],
    'Test_ID': [101, 102, 103, 104],
    'Mutation_Detected': ['BRCA1', 'TP53', 'None', 'BRCA2'],
    'Sequencing_Quality': [98, 45, 99, 30], # Simulated Phred Scores
    'Processing_Status': [' Completed ', 'pending', 'COMPLETED', ' error ']
}

# Loading data into a DataFrame (the standard tool for Data Analysts)
df = pd.DataFrame(raw_data)

print("--- Raw Dataset ---")
print(df)

# 2. DATA WRANGLING & CLEANING (Essential for Data Analysts)
# Standardizing text: removing white spaces and converting to lowercase
df['Processing_Status'] = df['Processing_Status'].str.strip().str.lower()

# 3. DATA FILTERING (Scientific Rigor)
# Filtering only high-quality sequencing results (Quality Score > 50)
high_quality_df = df[df['Sequencing_Quality'] > 50]

print("\n--- Processed Data (Quality Score > 50) ---")
print(high_quality_df)

# 4. DATA INSIGHTS
# Calculating the average quality score of the processed samples
avg_quality = high_quality_df['Sequencing_Quality'].mean()
print(f"\nPipeline Analysis Summary:")
print(f"Average Quality Score: {avg_quality}")
print("Status: Report generated successfully.")
