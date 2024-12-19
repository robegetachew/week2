import pandas as pd
import numpy as np
from scipy.stats import zscore

def clean_and_aggregate(input_file, output_file):
    """
    Function to clean and aggregate telecommunication data.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the cleaned and aggregated data.
    """

    # Step 1: Load the data
    print("Loading data...")
    data = pd.read_csv(input_file)

    # Step 2: Clean column names (remove leading/trailing spaces)
    print("Cleaning column names...")
    data.columns = data.columns.str.strip()
    print("Columns:", data.columns)

    # Step 3: Fill missing values
    print("Handling missing values...")
    numeric_columns = [
        'Dur. (ms)', 'Total DL (Bytes)', 'Total UL (Bytes)',
        'Social Media DL (Bytes)', 'Social Media UL (Bytes)',
        'Google DL (Bytes)', 'Google UL (Bytes)'
    ]
    
    for col in numeric_columns:
        if col in data.columns:
            print(f"Filling missing values in column: {col}")
            data[col].fillna(data[col].mean(), inplace=True)  # Fill numeric columns with the mean

    # Step 4: Remove duplicates (if any)
    print("Removing duplicate records...")
    data.drop_duplicates(inplace=True)

    # Step 5: Outlier Detection and Treatment
    print("Handling outliers using Z-score...")
    for col in ['Dur. (ms)', 'Total DL (Bytes)', 'Total UL (Bytes)']:
        if col in data.columns:
            z_scores = zscore(data[col])
            data = data[(np.abs(z_scores) < 3)]  # Keep data within 3 standard deviations

    # Step 6: Group and aggregate the data
    print("Aggregating data...")
    aggregated_data = data.groupby('MSISDN/Number').agg({
        'Dur. (ms)': 'sum',
        'Total DL (Bytes)': 'sum',
        'Total UL (Bytes)': 'sum',
        'Social Media DL (Bytes)': 'sum',
        'Social Media UL (Bytes)': 'sum',
        'Google DL (Bytes)': 'sum',
        'Google UL (Bytes)': 'sum',
    }).reset_index()

    # Step 7: Save the cleaned and aggregated data
    print(f"Saving the cleaned data to {output_file}...")
    aggregated_data.to_csv(output_file, index=False)

    print("Data cleaning and aggregation completed successfully!")


if __name__ == "__main__":
    # Example usage
    input_file = "../data/telecom_data.csv"  # Update path as necessary
    output_file = "../data/cleaned_task1_output.csv"

    clean_and_aggregate(input_file, output_file)
