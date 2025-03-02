import streamlit as st
import pandas as pd

# Define the URL of the raw CSV file in the GitHub repository
GITHUB_URL = "https://github.com/daveondecks/table_test.git/data_table/data.csv"

@st.experimental_connection
def fetch_data():
    # Fetch the data from the GitHub URL
    data = pd.read_csv(GITHUB_URL)
    return data

def main():
    st.title("GitHub Data Connection Example")

    # Fetch the data
    data = fetch_data()

    # Display the data in a table
    st.write(data)

if __name__ == "__main__":
    main()
