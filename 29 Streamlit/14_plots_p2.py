# Core Pkgs
import streamlit as st 

# Load EDA Pkgs
import pandas as pd 
import numpy as np

# Load Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg') # TkAgg
import seaborn as sns

import altair as alt


def main():
	st.title("Plotting with st.pyplot")
	df = pd.read_csv("data/lang_data.csv")

	st.dataframe(df.head())


	lang_list = df.columns.tolist()
	lang_choices = st.multiselect("Choose Language",
			       				 lang_list,
								 default="Python")
	
	new_df = df[lang_choices]
	
	st.line_chart(new_df)

	st.area_chart(new_df, use_container_width=True)

	# Altair
	df = pd.DataFrame(
	np.random.randn(200, 3),
	columns=['a', 'b', 'c'])
	c = alt.Chart(df).mark_circle().encode(
   	 x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
	st.dataframe(df.head())

	# Method 1
	st.write(c)

	# Method 2
	st.altair_chart(c, use_container_width=True)





if __name__ == "__main__":
	main()