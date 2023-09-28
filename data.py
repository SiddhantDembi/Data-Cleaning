import streamlit as st
import pandas as pd
import io

# Streamlit UI
st.title("Clean your file")

# Function to download the cleaned DataFrame
def download(cleaned_file):
    st.download_button(
        label="Download Cleaned File",
        data=cleaned_file,
        key="cleaned_file",
        file_name="cleaned_file.csv",
    )

# Function to replace null values in the DataFrame
def replace(df):
    # Allow users to input the custom value to replace nulls
    custom_value = st.text_input("Enter a value to replace nulls:", "NULL")
    
    # Replace null values with the custom value
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
            df[column] = df[column].str.lower()
    return df

uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["xls", "xlsx", "csv"])

if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    try:
        df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(('xls', 'xlsx')) else pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error: {e}")
    
    st.success("File uploaded successfully!")

    # List of radio buttons for cleaning options with multiselect
    clean_options = st.multiselect("Select cleaning options:", ["Replace", "Remove Duplicate", "Remove Missing Values", "Convert to Lowercase"])

    if "Replace" in clean_options:
        # Replace null values in the DataFrame
        df = replace(df)
    if "Remove Duplicate" in clean_options:
        # Remove duplicate rows in the DataFrame
        df = remove_duplicates(df)
        st.success("Duplicate rows removed successfully.")
    if "Remove Missing Values" in clean_options:
        # Remove rows with missing values
        df = remove_missing_values(df)
        st.success("Rows with missing values removed successfully.")
    if "Convert to Lowercase" in clean_options:
        # Convert selected columns to lowercase
        selected_columns = st.multiselect("Select columns to convert to lowercase:", df.columns)
        df = convert_to_lowercase(df, selected_columns)

    # Allow users to download the cleaned file
    cleaned_file = df.to_csv(index=False).encode()
    download(cleaned_file)

    # Display the cleaned DataFrame
    st.dataframe(df)
else:
    st.info("Please upload a file.")
