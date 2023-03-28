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

def main():
	st.title("Plotting with st.pyplot")
	df = pd.read_csv("data/iris.csv")


	## OLD Method
	st.dataframe(df.head())
	df["species"].value_counts().plot(kind="bar")
	st.pyplot()

	plt.scatter(*np.random.random(size=(2,100)))
	st.pyplot()

	##NEW METHOD
	fig,ax = plt.subplots()
	ax.scatter(*np.random.random(size=(2,100)))
	st.pyplot(fig)

	fig = plt.figure()
	df["species"].value_counts().plot(kind=("bar"))
	st.pyplot(fig)

	
	# Bar chart
	st.dataframe(df.head())

	st.bar_chart(df["sepal_length"])
	st.bar_chart(df[["sepal_length","petal_length"]])




if __name__ == "__main__":
	main()