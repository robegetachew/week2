import pandas as pd
import numpy as np
from scipy.stats import zscore
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

def clean_and_aggregate(input_file, output_file):
    """Clean the dataset and perform user-level aggregation."""
    print("Loading data...")
    data = pd.read_csv(input_file)

    # Step 1: Clean column names
    print("Cleaning column names...")
    data.columns = data.columns.str.strip()

    # Step 2: Fill missing values
    print("Handling missing values...")
    for col in ['Dur. (ms)', 'Total DL (Bytes)', 'Total UL (Bytes)']:
        data[col].fillna(data[col].mean(), inplace=True)

    # Step 3: Outlier treatment
    print("Handling outliers...")
    for col in ['Dur. (ms)', 'Total DL (Bytes)', 'Total UL (Bytes)']:
        z_scores = zscore(data[col])
        data = data[np.abs(z_scores) < 3]

    # Step 4: Aggregate user data
    print("Aggregating user data...")
    aggregated_data = data.groupby('MSISDN/Number').agg({
        'Dur. (ms)': 'sum',
        'Total DL (Bytes)': 'sum',
        'Total UL (Bytes)': 'sum',
    }).reset_index()

    aggregated_data['Total Volume (Bytes)'] = aggregated_data['Total DL (Bytes)'] + aggregated_data['Total UL (Bytes)']
    print(f"Saving aggregated data to {output_file}...")
    aggregated_data.to_csv(output_file, index=False)

def handset_analysis(input_file):
    """Identify top handsets and manufacturers."""
    print("\nAnalyzing handsets and manufacturers...")
    data = pd.read_csv(input_file)

    # Top 10 handsets
    top_handsets = data['Handset Type'].value_counts().head(10)
    print("\nTop 10 handsets:")
    print(top_handsets)

    # Top 3 manufacturers
    top_manufacturers = data['Handset Manufacturer'].value_counts().head(3)
    print("\nTop 3 handset manufacturers:")
    print(top_manufacturers)

    # Top 5 handsets per manufacturer
    print("\nTop 5 handsets per top 3 manufacturers:")
    for manufacturer in top_manufacturers.index:
        top_handsets_mfg = data[data['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
        print(f"\nManufacturer: {manufacturer}")
        print(top_handsets_mfg)

def explore_data(input_file):
    """Perform full exploratory data analysis."""
    print("\nStarting Exploratory Data Analysis...")
    data = pd.read_csv(input_file)

    # Describe dataset
    print("\nDescribing dataset...")
    print(data.describe())

    # Decile segmentation based on 'Dur. (ms)'
    print("\nSegmenting users into deciles...")
    data['Decile'] = pd.qcut(data['Dur. (ms)'], 5, labels=False)
    print(data.groupby('Decile')['Total Volume (Bytes)'].sum())

    # Correlation analysis
    print("\nCorrelation Analysis...")
    correlation_columns = ['Total DL (Bytes)', 'Total UL (Bytes)', 'Dur. (ms)']
    correlation_matrix = data[correlation_columns].corr()
    print(correlation_matrix)

    # Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

    # PCA
    print("\nPerforming PCA for dimensionality reduction...")
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(data[correlation_columns])
    print("Explained Variance Ratio:", pca.explained_variance_ratio_)

    # Plot PCA results
    plt.scatter(pca_result[:, 0], pca_result[:, 1])
    plt.title("PCA Analysis")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.show()
