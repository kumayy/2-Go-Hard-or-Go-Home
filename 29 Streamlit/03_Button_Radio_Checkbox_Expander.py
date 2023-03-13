# core pkgs
import streamlit as st

# working with widgets
# Buttons/Radio/Checkbox/Select/

# Working with Buttons
name = "Harder"

if st.button("push me"):
    st.write("go on my boi: {}".format(name.upper()))

if st.button("push me", key="new02"):
    st.write("go on my boi: {}".format(name.upper()))

# Radiobutton
status = st.radio("What is your status", ("Dead","Alive"))
if status == "Alive":
    st.success("Lovely")
else:
    st.error("Sad")

# checkbox
if st.checkbox("Show/Hide"):
    st.text("Show me")

# Working beta expander
with st.expander("Pokémon"):
    st.info("gotta catch em all")