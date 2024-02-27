# Data Cleaner


## Overview
Data Cleaner is a Streamlit-based application designed to provide users with a convenient interface for cleaning and processing tabular data files (CSV, XLS, XLSX). This application allows users to perform various data cleaning operations easily.

## Set Up

Clone this repository to your local machine.
````bash
https://github.com/SiddhantDembi/Data-Cleaning.git
````
Install the required dependencies using 
````bash
pip install -r requirements.txt
````

Run the Streamlit application locally using
````bash
streamlit run data.py
````
or 
````bash
python -m streamlit run data.py
````

## Features

- **Replace Null Values:** Replace missing (null) values with a custom value.
- **Remove Duplicate Rows:** Eliminate duplicate rows from the dataset.
- **Remove Missing Values:** Remove rows containing missing values.
- **Convert to Lowercase:** Convert text columns to lowercase.
- **Delete Columns:** Select and delete specific columns from the dataset.
- **Sort Column:** Sort a column in ascending or descending order based on lexicographical order.
- **Capitalize Columns:** Capitalize the first letter of elements in selected columns.

## How to Use

1. **Upload File:** Upload an Excel (XLS, XLSX) or CSV file.
2. **Select Sheet (for Excel files):** If uploading an Excel file, select the sheet you want to clean.
3. **Choose Cleaning Options:** Select the cleaning options you want to apply to your data.
4. **Download Cleaned File:** Download the cleaned data in the same format as your input file or in CSV format.

## Example

To demonstrate the functionality of Data Cleaner, a sample CSV file (`sample.csv`) is provided. You can download the sample file by clicking the "Download Test Sample" button within the application.

