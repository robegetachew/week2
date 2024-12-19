import sys
import os

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src.data_cleaning import clean_and_aggregate

if __name__ == "__main__":
    # Use correct file paths
    input_file = os.path.join(project_root, "data", "telecom_data.csv")
    output_file = os.path.join(project_root, "data", "cleaned_task1_output.csv")
    
    clean_and_aggregate(input_file, output_file)
    print("Task 1 analysis completed successfully!")
