import streamlit as st
import pandas as pd

# Define the URL of the raw CSV file in the GitHub repository
GITHUB_URL = "https://raw.githubusercontent.com/daveondecks/table_test/main/data_table/data.csv"

def fetch_data():
    # Fetch the data from the GitHub URL
    data = pd.read_csv(GITHUB_URL)
    return data

def main():
    st.title("GitHub Data Table Example")

    # Fetch the data
    data = fetch_data()

    # Display the data in a table
    st.write(data)

if __name__ == "__main__":
    main()
