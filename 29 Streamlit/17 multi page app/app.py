# Core Pkgs
import streamlit as st 


def main():
	st.title("Multi Page")
	st.subheader("Main Page")

	choice = st.sidebar.selectbox("Sub Menu", ["Pandas","Numpy"])








if __name__ == "__main__":
	main()