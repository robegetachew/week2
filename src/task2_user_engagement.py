import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def ensure_directory(directory):
    """Ensure the directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def aggregate_user_engagement(input_file, output_file):
    """
    Perform user engagement analysis:
    - Aggregate metrics
    - Normalize data
    - Run K-means clustering
    - Determine optimal K using elbow method
    - Visualize results
    """

    # Step 1: Load dataset
    print("Loading data...")
    df = pd.read_csv(input_file)

    # Step 2: Aggregate metrics per user
    print("Aggregating user engagement metrics...")
    engagement_metrics = df.groupby('MSISDN/Number').agg({
        'Bearer Id': 'count',  # Sessions frequency
        'Dur. (ms)': 'sum',    # Session duration
        'Total DL (Bytes)': 'sum',  # Total download
        'Total UL (Bytes)': 'sum'   # Total upload
    }).rename(columns={
        'Bearer Id': 'session_count',
        'Dur. (ms)': 'total_duration',
        'Total DL (Bytes)': 'total_download',
        'Total UL (Bytes)': 'total_upload'
    }).reset_index()

    engagement_metrics['total_traffic'] = engagement_metrics['total_download'] + engagement_metrics['total_upload']

    # Save aggregated data
    print(f"Saving aggregated data to {output_file}...")
    ensure_directory('data')
    engagement_metrics.to_csv(output_file, index=False)

    # Step 3: Normalize metrics
    print("Normalizing metrics...")
    scaler = MinMaxScaler()
    normalized_data = engagement_metrics[['session_count', 'total_duration', 'total_traffic']]
    normalized_data = pd.DataFrame(scaler.fit_transform(normalized_data),
                                   columns=['session_count', 'total_duration', 'total_traffic'])

    # Step 4: K-means clustering
    print("Running K-means clustering...")
    kmeans = KMeans(n_clusters=3, random_state=42)
    engagement_metrics['engagement_cluster'] = kmeans.fit_predict(normalized_data)

    # Step 5: Elbow Method for optimal K
    print("Running Elbow Method for optimal K...")
    distortions = []
    K_range = range(1, 10)

    for k in K_range:
        km = KMeans(n_clusters=k, random_state=42)
        km.fit(normalized_data)
        distortions.append(km.inertia_)

    # Ensure visualizations folder exists
    ensure_directory('visualizations')

    # Save and plot the elbow method
    plt.figure(figsize=(8, 5))
    plt.plot(K_range, distortions, marker='o')
    plt.xlabel('Number of clusters (K)')
    plt.ylabel('Distortion')
    plt.title('Elbow Method for Optimal K')
    plt.savefig('visualizations/elbow_method.png')
    plt.show()

    # Step 6: Cluster Statistics
    print("Computing cluster statistics...")
    cluster_stats = engagement_metrics.groupby('engagement_cluster').agg({
        'session_count': ['min', 'max', 'mean', 'sum'],
        'total_duration': ['min', 'max', 'mean', 'sum'],
        'total_traffic': ['min', 'max', 'mean', 'sum']
    })
    print(cluster_stats)

    # Step 7: Most Engaged Users per Application
    print("Identifying top 10 most engaged users per application...")
    app_columns = ['Social Media DL (Bytes)', 'Google DL (Bytes)', 'Email DL (Bytes)',
                   'Youtube DL (Bytes)', 'Netflix DL (Bytes)', 'Gaming DL (Bytes)']
    app_metrics = df.groupby('MSISDN/Number')[app_columns].sum().reset_index()

    # Find top 10 users per application
    top_users = {}
    for app in app_columns:
        top_users[app] = app_metrics.nlargest(10, app)

    # Step 8: Top 3 Most Used Applications
    print("Plotting top 3 most used applications...")
    app_totals = app_metrics[app_columns].sum().sort_values(ascending=False)
    top_3_apps = app_totals.head(3)

    plt.figure(figsize=(8, 6))
    sns.barplot(x=top_3_apps.index, y=top_3_apps.values)
    plt.title("Top 3 Most Used Applications")
    plt.ylabel("Total Data Consumption (Bytes)")
    plt.xticks(rotation=45)
    plt.savefig('visualizations/top_3_apps.png')
    plt.show()

    print("Task 2 analysis completed successfully!")

if __name__ == "__main__":
    # Input and output file paths
    input_file = "data/telecom_data.csv"
    output_file = "data/engagement_metrics.csv"

    aggregate_user_engagement(input_file, output_file)
