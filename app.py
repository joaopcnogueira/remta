import pandas as pd
import streamlit as st

st.write("""
# REMTA - Raman Spectroscopy Multi Tool Analyzer
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

if uploaded_file:
    input_df = pd.read_csv(uploaded_file)
    # st.write(input_df)
    st.line_chart(input_df.drop(['x', 'y'], axis=1))


unique_spectra = input_df.drop(['x', 'y'], axis=1).columns.tolist()
selected_spectra = st.sidebar.multiselect('Spectra', unique_spectra, unique_spectra)

if len(selected_spectra) < input_df.shape[1]:
    st.line_chart(input_df.drop(['x', 'y'] + [spectra for spectra in unique_spectra if spectra not in selected_spectra], axis=1))