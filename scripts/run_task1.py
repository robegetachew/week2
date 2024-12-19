import sys
import os

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src.data_cleaning import clean_and_aggregate, handset_analysis, explore_data

if __name__ == "__main__":
    input_file = os.path.join(project_root, "data", "telecom_data.csv")
    output_file = os.path.join(project_root, "data", "cleaned_task1_output.csv")

    # Clean and aggregate
    clean_and_aggregate(input_file, output_file)

    # Analyze handsets
    handset_analysis(input_file)

    # Perform exploratory data analysis
    explore_data(output_file)
