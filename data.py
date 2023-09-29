import streamlit as st
import pandas as pd
import io
import re

# Streamlit UI
st.title("Clean your file")

# Function to download the cleaned DataFrame
def download(cleaned_file, input_file_name, file_extension):
    default_cleaned_file_name = f"{input_file_name}_cleaned.{file_extension}"
    st.download_button(
        label="Download Cleaned File",
        data=cleaned_file,
        key="cleaned_file",
        file_name=default_cleaned_file_name,
    )

# Function to replace null values in the DataFrame
def replace(df):
    custom_value = st.text_input("Enter a value to replace nulls:", "NULL")
    df = df.fillna(custom_value)
    return df

# Function to remove duplicate rows in the DataFrame
def remove_duplicates(df):
    return df.drop_duplicates(keep='first')

# Function to remove rows with missing values
def remove_missing_values(df):
    return df.dropna()

# Function to convert selected columns to lowercase
def convert_to_lowercase(df, selected_columns):
    for column in selected_columns:
        if column in df.columns:
            if df[column].dtype == 'object':
                df[column] = df[column].str.lower()
            else:
                st.error(f"Column '{column}' is not of string data type. Select a string column to convert to lowercase.")
                return df
    return df

uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["xls", "xlsx", "csv"])

if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    try:
        if uploaded_file.name.endswith(('xls', 'xlsx')):
            # Load Excel file using openpyxl
            xls = pd.ExcelFile(uploaded_file)
            sheet_names = xls.sheet_names
            selected_sheet = st.selectbox("Select a sheet:", sheet_names)
            df = pd.read_excel(xls, sheet_name=selected_sheet)
        else:
            df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error: {e}")
    
    st.success("File uploaded successfully!")

    # List of radio buttons for cleaning options with multiselect
    clean_options = st.multiselect("Select cleaning options:", ["Replace", "Remove Duplicate", "Remove Missing Values", "Convert to Lowercase"])

    if "Replace" in clean_options:
        df = replace(df)
    if "Remove Duplicate" in clean_options:
        df = remove_duplicates(df)
        st.success("Duplicate rows removed successfully.")
    if "Remove Missing Values" in clean_options:
        df = remove_missing_values(df)
        st.success("Rows with missing values removed successfully.")
    if "Convert to Lowercase" in clean_options:
        selected_columns = st.multiselect("Select columns to convert to lowercase:", df.columns)
        df = convert_to_lowercase(df, selected_columns)

    # Allow users to download the cleaned file in the same format as the input file
    cleaned_file = io.BytesIO()
    if uploaded_file.name.endswith(('xls', 'xlsx')):
        with pd.ExcelWriter(cleaned_file, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=selected_sheet, index=False)
        file_extension = "xlsx"
    else:
        df.to_csv(cleaned_file, index=False)
        file_extension = "csv"
    
    # Get the name of the uploaded file without the extension
    input_file_name = uploaded_file.name.rsplit('.', 1)[0]

    download(cleaned_file, input_file_name, file_extension)

    # If uploaded file is XLS or XLSX, add a button to download as CSV
    if uploaded_file.name.endswith(('xls', 'xlsx')):
        csv_file = io.BytesIO()
        df.to_csv(csv_file, index=False)
        st.download_button(
            label="Download Cleaned File (CSV)",
            data=csv_file,
            key="cleaned_file_csv",
            file_name=f"{input_file_name}_cleaned.csv",
        )

    # Display the cleaned DataFrame
    st.dataframe(df)

# Add text to the sidebar area (at the edge of the screen)
st.sidebar.text("Created by Siddhant Dembi")

# Add a note explaining the features and aim of the project in the sidebar
st.sidebar.markdown("### Project Description")
st.sidebar.markdown("""
This project provides a user-friendly interface for cleaning and processing tabular data files (CSV, XLS, XLSX). 
You can perform the following operations on your data:

- **Replace Null Values:** Replace missing (null) values with a custom value.
- **Remove Duplicate Rows:** Eliminate duplicate rows from your dataset.
- **Remove Missing Values:** Remove rows containing missing values.
- **Convert to Lowercase:** Convert text columns to lowercase.

You can download the cleaned data in the same format as your input file or in CSV format.
""")
