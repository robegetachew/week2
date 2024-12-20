import sys
import os

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src.task2_user_engagement import aggregate_user_engagement

if __name__ == "__main__":
    input_file = os.path.join(project_root, "data", "telecom_data.csv")
    output_file = os.path.join(project_root, "data", "engagement_metrics.csv")

    aggregate_user_engagement(input_file, output_file)
