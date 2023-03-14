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

# Select
my_lang = ["Python","Julia","Go","Rust"]

choice = st.selectbox("Language", my_lang)
st.write("you selected {}".format(choice))

# Multiple Select
spoken_lang = {"English","French","Japan","Turkish"}
my_spoken = st.multiselect("Spoken Language:", spoken_lang)
my_spoken = st.multiselect("Spoken Language:", spoken_lang, default="Turkish")

# Slider
age = st.slider("Age",1,100) # numbers

color = st.select_slider("Choose Color",
     options=["yellow","red","blue","black","green"])

colors = st.select_slider("Choose Color",
     options=["yellow","red","blue","black","green"],
     value=("yellow","blue"))