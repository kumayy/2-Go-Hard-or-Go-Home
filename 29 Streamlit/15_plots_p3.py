# Core Pkgs
import streamlit as st 

# Load EDA Pkgs
import pandas as pd 
import numpy as np

# Load Data Viz Pkgs
import plotly.express as px


def main():
	st.title("Plotting")
	df = pd.read_csv("data/prog_languages_data.csv")

	st.dataframe(df.head())

	fig = px.pie(df, values="Sum", names="lang", title="Pie Chart")
	st.plotly_chart(fig)

	fig2 = px.bar(df,x="lang", y="Sum")
	st.plotly_chart(fig2)



if __name__ == "__main__":
	main()