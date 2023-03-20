import streamlit as st
import pandas as pd

def run_eda_app():
    st.subheader("FROM EDA")
    df = pd.read_csv("data/diabetes_data_upload.csv")
    st.dataframe(df)

    