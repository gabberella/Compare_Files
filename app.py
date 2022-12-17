import streamlit as st
import pandas as pd


st.header("Excel File Comparison Tool")

file1 = st.file_uploader("Choose the first Excel file", type="xlsx")
file2 = st.file_uploader("Choose the second Excel file", type="xlsx")

try:

    # Read the Excel files into dataframes
    if file1 and file2:
        df1 = pd.read_excel(file1)
        df2 = pd.read_excel(file2)

        # Compare the dataframes and display the differences
        diff = df1.merge(df2, indicator=True, how='outer')
        diff = diff[diff['_merge'] != 'both']
        diff = diff.rename(columns={'_merge': 'source'})
        diff['source'] = diff['source'].replace({'left_only': "file1", 'right_only': "file2"})
        st.write("Differences:")
        st.dataframe(diff)

    # Create a button to download the CSV file
    csv_button = st.button("Download CSV")
    if csv_button:
        st.download(diff.to_csv(index=False), "differences.csv", encoding="utf-8")


except Exception as e:
    # Display a pretty error message
    st.write("Unfortunately, an error occurred:")
    st.error(e)
