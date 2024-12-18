# Telecommunication Data Analysis Project

## Overview
This project focuses on analyzing telecommunication user data to uncover insights and provide recommendations for business growth. The analysis includes user overview, engagement analysis, experience analytics, and satisfaction analysis using Python and data visualization tools.

## Objectives
1. **User Overview Analysis**
   - Identify top handsets, manufacturers, and usage patterns.
   - Aggregate session metrics (duration, download/upload data).
2. **User Engagement Analysis**
   - Track user engagement using session frequency, duration, and traffic.
   - Cluster users based on engagement levels.
3. **Experience Analytics**
   - Analyze user experience based on TCP retransmission, RTT, throughput, and handset types.
   - Segment users into experience clusters.
4. **Satisfaction Analysis**
   - Combine engagement and experience metrics to measure customer satisfaction.
   - Build regression models to predict satisfaction scores.
5. **Dashboard Development**
   - Design an interactive Streamlit dashboard to visualize insights.

## Folder Structure
```plaintext
project/
├── .vscode/
│   └── settings.json           # Editor settings
├── .github/
│   └── workflows/
│       └── unittests.yml       # CI/CD pipeline for unit tests
├── .gitignore                  # Ignore unnecessary files (e.g., venv, .pyc)
├── requirements.txt            # Required Python libraries
├── README.md                   # Project documentation (this file)
├── src/
│   ├── __init__.py             # Package initialization
│   └── data_cleaning.py        # Task 1: Data cleaning and aggregation
├── notebooks/
│   ├── __init__.py             # Notebook package initialization
│   └── README.md               # Notebook documentation
├── tests/
│   ├── __init__.py             # Unit test initialization
│   └── test_data_cleaning.py   # Unit tests for Task 1
└── scripts/
    ├── __init__.py             # Scripts initialization
    └── run_task1.py            # Script to run Task 1 analysis
```

## Technologies Used
- **Python**: Pandas, Numpy, Scikit-learn, Matplotlib, Seaborn
- **Streamlit**: For interactive dashboard development
- **PostgreSQL**: Database management
- **GitHub Actions**: CI/CD pipeline for unit testing
- **Docker**: Containerization for deployment

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/robegetachew/telecom-analysis.git
cd telecom-analysis
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Task 1 Analysis
```bash
python scripts/run_task1.py
```

### 5. Run Unit Tests
```bash
pytest tests/test_data_cleaning.py
```

### 6. Run the Streamlit Dashboard
```bash
streamlit run app.py
```

## Author
**Robe Getachew**  
GitHub: [robegetachew](https://github.com/robegetachew)

