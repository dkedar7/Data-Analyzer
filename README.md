# Data Analyzer

[![CircleCI](https://img.shields.io/circleci/build/github/dkedar7/Data-Analyzer)](https://circleci.com/gh/dkedar7/Data-Analyzer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/dkedar7/Data-Analyzer/flask)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/dkedar7/Data-Analyzer/dash)

![Data Analyzer Demo](https://github.com/dkedar7/Data-Analyzer/blob/master/Analyzer/assets/Demo.png?raw=true)

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

#### Step 1. Clone this repository by running

    git clone https://github.com/dkedar7/Data-Analyzer
    
#### Step 2. Create a virtual environement by running

    python -m venv DataAnalyzer
        
#### Step 3. Active this environment, on Windows:

    DataAnalyzer\Source\Activate

MacOS or Linux:

    source DataAnalyzer/bin/activate
    
#### Step 4. Open the directory and install dependencies

    cd Analyzer/
    pip install -r requirements.txt
    
#### Step 5. Launch the web application

    python run.py
    
Use `localhost:8080` to interact with the application.

## About the demo deployment

The [demo deployment](https://data-analyzer-hpn4y2dvda-uc.a.run.app/) utilizes Google Build to containerize the application, Google Container Registry for storing and managing a container and Google Cloud Run to deploy it as a web endpoint.

![Cloud Run Architecture](https://github.com/dkedar7/Data-Analyzer/blob/master/Analyzer/assets/architecture.png?raw=true)

[More about Google Cloud Run](https://cloud.google.com/run/docs/)

## Limitations
* Data Analyzer currently only supports tabular data, in either a .csv, .xlsx, or .xls formats
* Upload fails if there are any inconsistencies with the input file
* The app's ability to handle large data depends on memory allocated by the host machine. The [demo deployment](#https://data-analyzer-hpn4y2dvda-uc.a.run.app/) of the app may crash if memory exceeds
* Pandas Profiling can sometimes fail to auto-infer the `datetime` datatype.

## License
Data analyzer uses the [MIT license](https://github.com/dkedar7/Data-Analyzer/blob/master/LICENSE).

## Dependencies

You need [Python 3](https://python3statement.org/) to run this application. Other dependencies can be found in the [requirements.txt](https://github.com/dkedar7/Data-Analyzer/blob/master/Analyzer/requirements.txt) file.
