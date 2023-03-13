# core pkgs
import streamlit as st

# Text
st.text("This is the way")

name = "Baby Yoda"

st.text("Hello {}".format(name))

# Header
st.header("this is a header")
st.subheader("this is a subheader")
st.title("TITLE")

# Markdown
st.markdown("## markdown bu şekilde yazilir")

# Colored Text / Bootstrap Alert
st.success("successful")
st.warning("Dangerous")
st.info("This is information")
st.error("Error !!")
st.exception("Exception")

# Superfunction
st.write("```### This is a test```")
st.write(5+8)
st.write("yazı")
st.write(dir(st))

# help
st.help(range)

