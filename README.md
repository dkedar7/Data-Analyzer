# Data-Analyzer

![Data Analyzer Demo](https://github.com/dkedar7/Data-Analyzer/blob/master/Analyzer/assets/Demo.png?raw=true)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Data Analyzer is a web application built using Dash and Flask on Python that lets you analyze tabular data spreadsheets using [Pandas Profiler](https://github.com/pandas-profiling/pandas-profiling). It creates a report to describe each column in the tabular data using some commonly used statistical measures. The app also allows users to download this generated HTML report. Use the deployed application [here](https://data-analyzer-hpn4y2dvda-uc.a.run.app/) and follow these [steps](#Installation) to deploy this app locally.

For each column, the following statistical measures are generated:
* **Type inference**: detect the types of columns in a dataframe.
* **Essentials**: type, unique values, missing values
* **Quantile statistics** like minimum value, Q1, median, Q3, maximum, range, interquartile range
* **Descriptive statistics** like mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness
* **Most frequent values**
* **Histogram**
* **Correlations** highlighting of highly correlated variables, Spearman, Pearson and Kendall matrices
* **Missing values** matrix, count, heatmap and dendrogram of missing values
* **Text analysis** learn about categories (Uppercase, Space), scripts (Latin, Cyrillic) and blocks (ASCII) of text data.

## Installation

You can clone this repository by running

    git clone https://github.com/dkedar7/Data-Analyzer
Create a virtual environement by running

    python -m venv DataAnalyzer
        
Active this environment
Windows:

    TesterMatchingApp\Source\Activate

MacOS or Linux:

    source TesterMatchingApp/bin/activate
    
Open the directory and install dependencies

    cd DataAnalyzer/
    pip install -r requirements.txt
    
Launch the web application

    python run.py
    
Use `localhost:8080` to interact with the application