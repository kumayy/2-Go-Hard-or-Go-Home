# core pkgs
import streamlit as st

# load EDA pkgs
import pandas as pd

# display data
df = pd.read_csv("data/iris.csv")

# Data display
# st.dataframe(df,200,100)
# st.dataframe(df) 
# st.table(df) # static table
# st.write(df)

# Style
st.dataframe(df.style.highlight_max(axis=0))

# display Json
st.json({"data" : "name"})

# display code
mycode="""
def saymyname():
    print("heisenberg")
end
"""
st.code(mycode, language='python')
